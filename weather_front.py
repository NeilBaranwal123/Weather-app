import streammlit as st
import requests
st.title("Weather app")
city = st.text_input("enter the city")
if st.button("check weather"):
    url = f"http://127.0.0.1:8000/get_weather/{city}"
    try:
        response=requests.get(url)
        result=response.json()
        if result["status"]=="success":
            st.success(f"Temperature: {result["data"]["Temp"]}C")
            st.info(f"Condition: {result["data"]["condition"]}")
        else:
            st.error(result["message"])
    except:
        st.error("backend not running")
