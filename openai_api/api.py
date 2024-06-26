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
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return {"error": "There was an issue processing the response. Please try again."}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"error": "An unexpected error occurred. Please try again later."}