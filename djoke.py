import requests as R

url = "https://icanhazdadjoke.com/"

payload={ }
headers = { 'Accept': 'application/json'}
joke = R.request("GET", url, headers=headers, data=payload)

print(joke.text)
print("Dad joke retrieved. Thank you for using our service.")
