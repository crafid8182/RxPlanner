import pytesseract
from PIL import Image
import cv2

from icalendar import Calendar, Event, Alarm
from datetime import datetime, timedelta
from pathlib import Path
import os
import pytz
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv('server/.env')

OPENAI_KEY = os.getenv('OPENAI_API_KEY')
ROOT_DIREC = os.getenv('ROOT_DIREC')

# takes preprocess img
def process_img(img):

    #convert to greyscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #gets rid of noise
    denoised = cv2.fastNlMeansDenoising(gray, h=30)

    processed_img = cv2.adaptiveThreshold(denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 11, 2)

    return processed_img



# gets processed img and get the string
def img_to_string(processed_img):

    #convert to PIL (cuz pytesseract needs PIL)
    img = Image.fromarray(processed_img)

    text = pytesseract.image_to_string(img)

    return text



# def pass string to gpt api to get formatted string
def gpt_parser(s):

    client = OpenAI(
        api_key=OPENAI_KEY
    )

    prompt = f"""
            I did OCR on the following prescription: {s} \n\n
            Within this text, there is information about the medication, dosage, time, and refill date.
            Please format the prescription in the following structure: "\"MEDICINE NAME | DOSAGE | TIME TO TAKE | REFILL DATE"\"
            1. The Medicine Name should not be so specific like "Metformin HCL 750 mg (extended-release) generic for Glucophage XR" but rather a simple "Metformin HCL 750 mg" or "Metformin" is fine.
            2. The Dosage should be "num D/H" for example every day would be "1D" every 6 hours would be "6H" or 6H
            3. The time to take should be a specific time like "0900" if 9:00 AM or "1700" if 5PM. The Refill date should be in format MM/DD/YYYY
            Return only the formatted string, nothing else
        """ 
    llm_response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
    llm_response = llm_response.choices[0].message.content.strip()

    return llm_response


#def to get frequency of ical
def set_recurrence_rule(event, dosage, refill_date):
    # Parse the dosage string
    if dosage.endswith('D'):
        days = int(dosage[:-1])  # Extract the number before 'D'
        if days == 1:
            # Daily recurrence
            event.add('rrule', {
                'freq': 'daily',
                'until': refill_date
            })
        else:
            # Every N days
            event.add('rrule', {
                'freq': 'daily',
                'interval': days,  # Set interval to N days
                'until': refill_date
            })
    elif dosage.endswith('H'):
        hours = int(dosage[:-1])  # Extract the number before 'H'
        event.add('rrule', {
            'freq': 'hourly',
            'interval': hours,  # Set interval to N hours
            'until': refill_date
        })

# def pass string in gpt api and ask it to generate ical details

def generate_ical(formatted_string):
    cal = Calendar()
    event = Event()

    # format: Metformin HCL 750 mg | 1 D | 0900 | 06/21/2024
    string_split = [s.strip() for s in formatted_string.split('|', 3)]
    medicine = string_split[0]
    dosage = string_split[1]
    time = string_split[2]
    refill_date = string_split[3]

    refill_date_obj = datetime.strptime(refill_date, '%m/%d/%Y')

    
    tz = pytz.timezone('America/New_York')
    start_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, int(time[:2]), int(time[-2:]), 0, tzinfo=tz)

    event.add('summary', medicine)
    event.add('dtstart', start_time)
    event.add('dtend', start_time + timedelta(hours=1))


    set_recurrence_rule(event, dosage, refill_date_obj)



    alarm = Alarm()
    alarm.add('action', 'DISPLAY')
    alarm.add('description', f'Reminder: Take {medicine} at {time}')
    alarm.add('trigger', timedelta(minutes=-15))

    event.add_component(alarm)
    cal.add_component(event)

    med_name_path = medicine.lower().replace(" ", "-")
    local_path = f"/data/ical/{med_name_path}-reminder.ics"
    ics_path = ROOT_DIREC + local_path
    with open(ics_path, 'wb') as f:
        f.write(cal.to_ical())

    return local_path


# def plug in to make ical

# main

def main(img_path):
    try:
        # img_path = "/data/img/prescription.jpg"
        full_img_path = ROOT_DIREC + img_path
        print('ROOT_DIREC: '+ROOT_DIREC)
        print('Full Path:' + full_img_path)
        raw_img = cv2.imread(full_img_path)
        
        processed_img = process_img(raw_img)
        parsed_string = img_to_string(processed_img)

        formatted_string = gpt_parser(parsed_string)
        print(formatted_string)
        #print('Metformin | 1D | 0900 | 12/14/2024')


        ics_path = generate_ical(formatted_string)
        return ics_path
    
    except Exception as e:
        return False


# if __name__ == '__main__':
#     # run main function
#     main()


# backend/img-directory/IMG_5211.jpeg
