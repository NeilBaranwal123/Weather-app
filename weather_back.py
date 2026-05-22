from fastapi import FastAPI
app = FastAPI() ## creating fastapi app
#creatine the dummy database:
weather_db={"Delhi":{"temp":35,"condition":"Hot"},
"Mumbai":{"temp":30,"condition":"Humid"},"Bangalore":{"temp":25,"condition":"Pleasant"}}
##API ENDPOINT
@app.get("/get_weather/{city}")
def get_weather(city: str):
    data=weather_db.get(city)
    if data :
        return {"status": "success", "data": data}
    else:
        return {"status": "error", "message": "city not found"}
