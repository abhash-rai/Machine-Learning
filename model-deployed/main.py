import datetime
import streamlit as st
from catboost import CatBoostRegressor

from constants import input_info
from predictor import housing_prediction




cb_model = CatBoostRegressor()
cb_model.load_model('./catboost_model.cbm')



st.title('💰Monthly Appartment Rent Predictor💰')

st.write('If you wish to delve into the model training please explore my notebook-> https://www.kaggle.com/code/abhashrai/monthly-rental-prediction')
st.markdown("---")

for feature_name, val in input_info.items():

    if feature_name == 'bathrooms':
        bathrooms = st.selectbox(
            f"Select number of {feature_name}:",
            val,
            index=None,
            placeholder="Please select an option..."
        )

    elif feature_name == 'bedrooms':
        bedrooms = st.selectbox(
            f"Select number of {feature_name}:",
            val,
            index=None,
            placeholder="Please select an option..."
        )

    elif feature_name == 'fee':
        fee = st.selectbox(
            f"Select number of {feature_name}:",
            val,
            index=None,
            placeholder="Please select an option..."
        )

    elif feature_name == 'has_photo':
        has_photo = st.selectbox(
            f"Select whether posting has photo:",
            val,
            index=None,
            placeholder="Please select an option..."
        )

    elif feature_name == 'square_feet':
        start_value = val.start
        end_value = val.stop
        square_feet = st.slider(f"Select area ({feature_name}):", start_value, end_value, start_value)

    elif feature_name == 'cityname':
        cityname = st.selectbox(
            f"Select {feature_name}:",
            val,
            index=None,
            placeholder="Please select an option..."
        )

    elif feature_name == 'state':
        state = st.selectbox(
            f"Select {feature_name}:",
            val,
            index=None,
            placeholder="Please select an option..."
        )

    elif feature_name == 'latitude':
        start_value = val.start
        end_value = val.stop
        latitude = st.number_input(f"Enter {feature_name}:", min_value=float(start_value), max_value=float(end_value), step=None)

    elif feature_name == 'longitude':
        start_value = val.start
        end_value = val.stop
        longitude = st.number_input(f"Enter {feature_name}:", min_value=float(start_value), max_value=float(end_value), step=None)

    elif feature_name == 'time':
        time = None
        datetime_str = st.text_input("Enter date and time (format: YYYY-MM-DD HH:MM:SS):", placeholder ="2020-01-01 12:00:00")
        # Validate and parse the datetime
        if datetime_str:
            try:
                datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
                time = datetime_str
            except ValueError:
                st.error(f"Please enter the datetime in the correct format: YYYY-MM-DD HH:MM:SS")

    elif feature_name == 'amenities':
        amenities = st.multiselect(f"Choose {feature_name}:", options=val, default='missing', placeholder="Please select one or multiple option...")
        
        # Logic to ensure only "missing" or other amenities are selected
        if amenities == []:
            amenities = None
        elif "missing" in amenities and len(amenities) > 1:
            st.error("You cannot select other options when 'missing' is selected. Please remove 'missing' option from selection then select other options.")
            
    elif feature_name == 'pets':
        pets = st.multiselect(f"Choose {feature_name} allowed:", val, default ='missing', placeholder="Please select one or multiple option...")

        # Logic to ensure only "missing" or other amenities are selected
        if pets == []:
            pets = None
        elif "missing" in pets and len(pets) > 1:
            st.error("You cannot select other options when 'missing' is selected. Please remove 'missing' option from selection then select other options.")
            


st.markdown("---")
if st.button("Predict Price"):
    # Collect all inputs into a list and check for None values
    inputs = {
        "bathrooms": bathrooms,
        "bedrooms": bedrooms,
        "fee": fee,
        "has_photo": has_photo,
        "square_feet": square_feet,
        "cityname": cityname,
        "state": state,
        "latitude": latitude,
        "longitude": longitude,
        "time": time,
        "amenities": amenities,
        "pets": pets
    }

    # Check if all inputs have values
    if all(value is not None for value in inputs.values()):
        
        predicted_price_text = housing_prediction(
            model = cb_model,
            input_info = input_info,
            bathrooms = bathrooms,
            bedrooms = bedrooms,
            fee = fee,
            has_photo = has_photo,
            square_feet = square_feet,
            cityname = cityname,
            state = state,
            latitude = latitude,
            longitude = longitude,
            time = time,
            amenities = amenities,
            pets = pets
        )
        st.metric(label="Predicted price per month", value=predicted_price_text)
    else:
        st.error("Please fill in all fields before predicting.")

