import requests

def execute_code_api(code, language, input_data):
    payload = {
        'code': code,
        'language': language,
        'input': input_data
    }

    response = requests.post('https://api.codex.jaagrav.in', data=payload)
    result = response.json()
    return result