# We will be using MatPlotLib
import csv
from collections import defaultdict
import matplotlib.pyplot as plt


FILENAME="weather_logs.csv"

def visualize_weather():
    dates=[]
    temps=[]
    conditions=defaultdict(int)

    with open(FILENAME,"r",encoding="utf-8") as f:
        reader=csv.DictReader(f)
        for row in reader:
            try:
                dates.append(row["Date"])
                temps.append(float(row["Temperature"]))
                conditions[row["Condition"]]+=1
            except:
                print("Caught Error")
                continue
    if not dates:
        print("No data is available")
        return
    
    plt.figure(figsize=(10,7))
    plt.plot(dates,temps,marker='o')
    plt.title("temperature over time")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.tight_layout()
    plt.grid(True)
    plt.show()
    
    plt.figure(figsize=(10,7))
    plt.bar(conditions.keys(),conditions.values(),color='skyblue')
    plt.xlabel("Condition")
    plt.ylabel("Days")
    plt.show()

visualize_weather()

