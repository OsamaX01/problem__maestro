import os
import openai
import json

from dotenv import load_dotenv, find_dotenv

from .messeges import messages

_ = load_dotenv(find_dotenv())
openai.api_key  = os.environ['OPENAI_API_KEY']

client = openai.OpenAI()

def get_completion(messages, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content

def request_problem(user_message):
    messages.append({"role": "user", "content": user_message})
    response = get_completion(messages)
    try:
        data_dict = json.loads(response)
        return data_dict
    except:
        return None #TODO