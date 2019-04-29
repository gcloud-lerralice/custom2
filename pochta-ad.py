import requests
import json

url = "https://otpravka-api.pochta.ru/1.0/clean/address"

payload = data
data['address'] = []
data['address'].append({ 
        "id": "adr 1",
        "original-address": "Москва, Варшавское шоссе, 37"
}),
data['address'].append({
        "id": "adr 2",
        "original-address": "ул. Мясницкая, д. 26, г. Москва"
})

with open('data.txt', 'w') as outfile:  
    json.dump(data, outfile)
    
        
headers = {
    'Authorization': "AccessToken hTsU9frdoY0sqNGg0ru_14aHLEa1txyl",
    'X-User-Authorization': "Basic aW5mb0BuYS1sb3ZjYS5ydTpQb2NodGFwYXJ0aW9uMjAxNw==",
    'Accept': "application/json;charset=UTF-8",
    'Content-Type': "application/json",
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)