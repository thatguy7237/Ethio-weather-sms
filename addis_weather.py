import requests 
from bs4 import BeautifulSoup

url = "https://www.timeanddate.com/weather/ethiopia/addis-ababa"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    # This is the current temperature 
    temp_div = soup.find("div", class_="h2")
    temp = temp_div.text.strip() if temp_div else "N/A"

    # Weather description
    desc_p = soup.find("p", class_="my-city__weather-desc")
    desc = desc_p.text.strip() if desc_p else "N/A"

    print("🌤 Addis Ababa Weather Today 🌤")
    print(f"Temperature: {temp}")
    print(f"Condition: {desc}")
else:
    print("Failed to retrieve weather data.")
