import streamlit as st
import requests
from nominatim import Nominatim
from streamlit_folium import st_folium
import folium

api = Nominatim()
'''
# TaxiFareModel
'''

'''
## Please provide details of your trip below:
'''

pickup_datetime = st.text_input("Date and time", value="2014-07-06 19:18:00")

pickup_query = st.text_input("Pickup location", value='Empire State Building, New York')
dropoff_query = st.text_input("Dropoff location", value='Central Park, New York')

pickup_location = api.query(pickup_query)
dropoff_location = api.query(dropoff_query)

pickup_longitude = pickup_location[0]['lon']
pickup_latitude = pickup_location[0]['lat']
dropoff_longitude = dropoff_location[0]['lon']
dropoff_latitude = dropoff_location[0]['lat']

print(type(pickup_longitude))

passenger_count = st.slider("Passenger count",1,5,2)

midpoint = [(float(pickup_latitude) + float(dropoff_latitude)) / 2, (float(pickup_longitude) + float(dropoff_longitude)) / 2]
print(midpoint)

url = 'https://taxifare.lewagon.ai/predict'

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

st.session_state['map'] = folium.Map(location=midpoint, zoom_start=12)
folium.Marker([pickup_latitude, pickup_longitude], popup=pickup_query,
    tooltip=pickup_query).add_to(st.session_state['map'])
folium.Marker([dropoff_latitude, dropoff_longitude], popup=dropoff_query,
    tooltip=dropoff_query).add_to(st.session_state['map'])
print([pickup_latitude, pickup_longitude], [dropoff_latitude, dropoff_longitude])
folium.PolyLine(locations=[[float(pickup_latitude), float(pickup_longitude)], [float(dropoff_latitude), float(dropoff_longitude)]], color='blue').add_to(st.session_state['map'])
# folium.PolyLine(locations=[[pickup_latitude, pickup_longitude], [dropoff_latitude, dropoff_longitude]], color='blue').add_to(st.session_state['map'])

# call to render Folium map in Streamlit
st_data = st_folium(st.session_state['map'], width = 725)
