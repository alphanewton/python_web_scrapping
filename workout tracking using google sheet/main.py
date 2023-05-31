from datetime import datetime
import requests

APP_ID = "962771b3"
API_KEY = "6a44d3383b68abe57f5942e7253a8864"
USERNAME = "newton"
PASSWORD = "newtonnarzary"

GENDER = "male"
WEIGHT_KG = 53
HEIGHT_CM = 170
AGE = 20

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": input("What exercise did you do today?"),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()

today = datetime.now()
date_string = today.strftime("%d/%m/%Y")
time_string = today.strftime("%X")

sheety_endpoint = "https://api.sheety.co/f244aa6da3b13bc81798d4038dff9d21/myWorkoutsTracker/workouts"

sheety_header = {
    "Authorization": "Basic bmV3dG9uOm5ld3Rvbm5hcnphcnk="
}

for exercise in result['exercises']:
    data = {
        "workout": {
            "date": date_string,
            "duration": exercise["duration_min"],
            "exercise": exercise["name"].title(),
            "calories": exercise["nf_calories"],
            "time": time_string
        }
    }
    sheet_response = requests.post(url=sheety_endpoint, json=data, auth=(USERNAME, PASSWORD))
    print(sheet_response.content)




