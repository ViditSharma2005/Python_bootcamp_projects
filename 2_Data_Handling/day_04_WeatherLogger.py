import os
import csv
from datetime import datetime
import requests
from dotenv import load_dotenv

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(DIR_PATH)
load_dotenv(os.path.join(ROOT_DIR, ".env"))
FILENAME = os.path.join(DIR_PATH, "weather_logs.csv")

API_KEY = os.getenv("WEATHER_API_KEY", "")

if not os.path.exists(FILENAME):
    with open(FILENAME,"w",newline='',encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerow(['Date','City','Temperature','Condition'])

def log_weather():
    city = input("Enter your city name: ").strip()
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILENAME,"r",newline='',encoding="utf-8") as f:
        reader=csv.DictReader(f)
        for row in reader:
            if row["Date"]==date and row['City'].lower()==city.lower():
                print("duplicate entry")
                return
    try:
        URL=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response=requests.get(URL)
        data=response.json()

        if response.status_code !=200:
            print(f"API ERROR")
            return
        temp=data["main"]["temp"]
        condition= data["weather"][0]["main"]

        with open(FILENAME,"a",newline='',encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerow([date,city.title(),temp,condition])
            print(f"Logged: {temp} {condition} in {city.title()} on {date}")
    except Exception as e:
        print(f"Failed to make a Request: {e}")

def view_logs():
    with open(FILENAME,"r",encoding="utf-8") as f:
        reader = list(csv.reader(f))
        if(len(reader)<=1):
            print("No new entry ")
            return
        for row in reader[1:]:
            print(f"{row[0]} : {row[1]} : {row[2]} : {row[3]}")

def main():
    while True:
        print("Real time weather logger")
        print("1.Add weather log.")
        print("2.View weather logs.")

        choice = input("Choose an option").strip()

        match choice:
            case "1":log_weather()
            case "2":view_logs()
            case _ : print("Wrong choice")

if __name__=="__main__":
    main()


