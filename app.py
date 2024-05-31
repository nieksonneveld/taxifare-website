import streamlit as st
import requests

'''
# TaxiFareModel front
'''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

'''
## Please provide details of your trip below
'''

pickup_datetime = st.text_input("Date and time", value="2014-07-06 19:18:00")
pickup_longitude = st.text_input("Pickup longitude", value=-73.950655)
pickup_latitude = st.text_input("Pickup latitude", value=40.783282)
dropoff_longitude = st.text_input("Dropoff longitude", value=-73.984365)
dropoff_latitude = st.text_input("Dropoff latitude", value=40.769802)
passenger_count = st.slider("Passenger count",1,6,1)

url = 'https://taxifare-d236uvw5wa-ew.a.run.app/predict'

params = {'pickup_datetime':pickup_datetime,
            'pickup_longitude':pickup_longitude,
            'pickup_latitude':pickup_latitude,
            'dropoff_longitude':dropoff_longitude,
            'dropoff_latitude':dropoff_latitude,
            'passenger_count':passenger_count}



if st.button("Calculate my fare",type="primary"):
    results = requests.get(url,params).json()
    prediction = round(results["fare"],2)
    st.write(f"Your fare prediction is ${prediction}")
