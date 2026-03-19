import tkinter as tk
from tkinter import messagebox
import requests

api="8f8b32d259279e4bb9e3b6c657078809"

def getweather():
    city1=cityentry.get().strip()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city1},US&appid={api}&units=imperial"
    respone=requests.get(url)
    data=respone.json()

    
    name = data["name"] 
    weather = data["weather"][0]["description"].capitalize()
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]


    result = (
    f"City: {name}, USA\n"
    f"Weather: {weather}\n"
    f"Temperature: {temp} °F\n"
    f"Humidity: {humidity}%\n"
    f"Wind Speed: {wind} mph"   
    )
    messagebox.showinfo("Weather Tracker",result)
root=tk.Tk()
root.title('WEATHER TRACKER')
root.geometry("350x200")
root.resizable(False,False)
weather=tk.Label(root,text="Weather Tracker",font=("Arial",20))
weather.grid(row=0,column=0,columnspan=2)
city=tk.Label(root,text="City",font=("Arial",20))
city.grid(row=1,column=0,padx=10,pady=10)
cityentry=tk.Entry(root,font=("Arial",15))
cityentry.grid(row=1,column=1)
button=tk.Button(root,text="Get weather",font=("Arial",15),command=getweather)
button.grid(row=2,column=0,columnspan=2)
root.mainloop()