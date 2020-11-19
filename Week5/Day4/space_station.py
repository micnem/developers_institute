import requests
from time import sleep
# Get the people currently in space
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()
people = data['people']
print("People in Space\n")
for astronaut in people:
	print(f"{astronaut['name']} is onboard {astronaut['craft']}\n")
# Get the current position of the space station
print("The Space Station is at:\n")
for i in range(5):
	response = requests.get('http://api.open-notify.org/iss-now.json')
	data = response.json()
	print(f"{data['iss_position']['latitude']}, {data['iss_position']['longitude']}\n")
	sleep(1)
#Request a search of astronaut from google and save the html response into a file
query = "astronaut"
url = f"https://www.google.com/search?q={query}"
response = requests.get(url)
with open("mypage.html", "w") as f:
	f.write(response.text)