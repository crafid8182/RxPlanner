from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_API_KEY')

def reminder(name, ethnicity, age, height, weight):
    client = OpenAI(
        api_key=OPENAI_KEY
    )

    prompt = f"""
                What are some questions, a {weight}lbs {height} tall {age}year old {ethnicity} person should ask 
                their doctors due to ethnicity based conditions that person may be 
                predisposed to. Keep the message friendly and short enough to 
                fit a subheader.

                1. Start the message with 'Hey {name}, ' then something friendly or motivating similar to 'Empower your health! '
                2. The message should be short and concise. About 2 sentences.
                3. The point is to mke the patient aware of hereditary risks that come with the ethnicity
                
            """
    
    print(prompt)
    
    llm_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}            
            ]
        )
        
    llm_response = llm_response.choices[0].message.content.strip()

    return llm_response

def main():
    #reminder('black', 21, 'M')
    print(reminder('bengali', 22, '67', '135'))


if __name__ == '__main__':
    main()
