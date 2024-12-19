from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_API_KEY')

def reminder(ethnicity, age, sex):
    client = OpenAI(
        api_key=OPENAI_KEY
    )

    if sex == 'M':
        pronoun = 'his'
        gender = 'male'
    else:
        pronoun = 'her'
        gender = 'female'

    prompt = f"""
                What are some questions, a {age} year old {ethnicity} {gender} should ask 
                their doctors due to ethnicity based conditions that {gender} may be 
                predisposed to. Keep the message friendly and short enough to 
                fit a subheader.

                1. Start the message with something friendly or motivating similar to 'Empower your health: '
                2. The message should be short and to the point
                3. The point is to mke the patient aware of hereditary risks that come with the ethnicity
                
            """
    
    print(prompt)
    
    llm_response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}            
            ]
        )
        
    llm_response = llm_response.choices[0].message.content.strip()

    return llm_response

def main():
    #reminder('black', 21, 'M')
    print(reminder('black', 21, 'M'))


if __name__ == '__main__':
    main()
