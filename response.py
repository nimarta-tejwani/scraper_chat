import requests

def get_response(param1: str, param2: str) -> str:

    param1_encoded = requests.utils.quote(param1)
    param2_encoded = requests.utils.quote(param2)

    url = f"http://127.0.0.1:8000/generate_response/{param1_encoded}/{param2_encoded}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data["response"]
    else:
        return f"Failed to get response from FastAPI. Status code: {response.status_code}"



# param1_value = "what is my city name?"
# param2_value = "I'm Nimarta and I live in Sukkur and I'm a CSian"

# response_text = get_response_from_fastapi(param1_value, param2_value)
# print(response_text)