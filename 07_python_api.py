import requests

#Constants

BASE_URL = 'https://api.github.com'

response = requests.get(BASE_URL)
print(response)

#username = input('Give me a github username:\t')
