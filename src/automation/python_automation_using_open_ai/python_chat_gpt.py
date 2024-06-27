# This file gets the response from the open AI/ Chat-Gpt

import openai
import requests
import os
from dotenv import load_dotenv

# from openai import OpenAI

load_dotenv()
api_endpoint = 'https://api.openai.com/v1/completions'
api_key = os.getenv('OPENAI_API_KEY')
client = openai.OpenAI()


def main():
    print('hello open ai')
    headers = {
        'Content-Type: application/json',
        'Authorization: Bearer ' + api_key
    }
    requests.post(api_endpoint, )
    response = ''
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Who won the world series in 2020?"},
                {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
                {"role": "user", "content": "Where was it played?"}
            ]
        )
        if response.status_code == 200:
            print(response.json())
        else:
            print(f'Request failed with status code : {response.status_code}')

    except openai.OpenAIError as e:
        print('Error occurred.. '+response)


main()
