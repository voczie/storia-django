import requests

API_URL = "https://api-inference.huggingface.co/models/Felipehonorato/storIA"
headers = {"Authorization": "Bearer api_CwzaLVoNBMVQhviuBtnxxdVoXvQgjuTEmW"}

def remove_token(text):
  return " ".join(text.split()[1:])

def check_token(input):
  token = '<|startoftext|> '
  if input.split()[0] != token:
    return token + input
  else:
    return input

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()