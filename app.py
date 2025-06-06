import streamlit as st
import datetime
import requests
import pandas as pd


'''
# TaxiFareModel front
'''


'''
### Please provide the following information to predict the fare amount
'''

with st.form(key='fare_prediction_form'):
    date = st.date_input("Date of your travel",)
    time = st.time_input('Time of your travel',)
    pickup_longitude = st.number_input('Pickup Longitude')
    pickup_latitude = st.number_input('Pickup Latitude')
    dropoff_longitude = st.number_input('Dropoff Longitude')
    dropoff_latitude = st.number_input('Dropoff Latitude')
    passenger_count = st.number_input('How many Passengers?')
    submit_button = st.form_submit_button(label='Predict Fare')



if submit_button:

    '''
    ## Result
    '''

    url = 'https://api-460605772486.europe-west3.run.app'
    predict_url = f"{url}/predict"

    call_dict = {
        'pickup_datetime' : f"{date} {time}",
        'pickup_longitude': pickup_longitude,
        'pickup_latitude' : pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude' : dropoff_latitude,
        'passenger_count' : passenger_count,
    }

    response = requests.get(predict_url, params=call_dict)


    f"""
    Your trip will cost probably around

    $ {response.json()['fare']}
    """


    def get_map_data():
        return pd.DataFrame(
            [
                {'lat': pickup_latitude, 'lon': pickup_longitude},
                {'lat': dropoff_latitude, 'lon': dropoff_longitude}
            ]
        )
    df = get_map_data()

    st.map(df)
