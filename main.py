import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")

url = "https://api.restcountries.com/countries/v5?q=egypt"

headers = {
    "Authorization": API_KEY
}

response = requests.get(url, headers=headers)

print(response.status_code)
data = response.json()

country=data["data"]["objects"][0]

country_name = country["names"]["common"]
capital = country["capitals"][0]["name"]
country_code = country["codes"]["alpha_2"]
flag = country["flag"]["description"][0:85]

class Country:
    def __init__(self,country_name,capital,country_code,flag):
        self.country_name=country_name
        self.capital=capital
        self.country_code=country_code
        self.flag=flag

    def display(self):
        print("\n====== country Information ======")
        print(f"country_name      : {self.country_name}")
        print(f"capital           : {self.capital}")
        print(f"country_code      : {self.country_code}")
        print(f"flag              : {self.flag}")
        print("=============================")


country_obj = Country( country_name, capital, country_code, flag)
country_obj.display()
