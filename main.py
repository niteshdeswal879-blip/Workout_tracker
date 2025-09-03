import os.path
import requests
import datetime as dt
import pandas

WEIGHT=76
HEIGHT=180
AGE=19

exercise=input("Enter the exercise you have done")

headers={
    "x-app-id":os.getenv("APP_ID"),
    "x-app-key":os.getenv("APP_KEY"),
}

params={
    "query":exercise,
    "weight_kg":WEIGHT,
    "height_cm":HEIGHT,
    "age":AGE,
    "gender": "male"
}


response = requests.post(url='https://trackapi.nutritionix.com/v2/natural/exercise',json=params,headers=headers)
result = response.json()
today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

token={
    "Authorization":os.getenv("TOKEN")
}


for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"  ]
        }
    }

    jesponse=requests.post("https://api.sheety.co/972d98c041c28eeee5dfc5e74ff6a4e5/myWorkout/sheet1",json=sheet_inputs,headers=token)


why=requests.get("https://api.sheety.co/972d98c041c28eeee5dfc5e74ff6a4e5/myWorkout/sheet1", headers=token)
print(why.json())
