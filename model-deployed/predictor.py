from catboost import CatBoostRegressor

def housing_prediction(
    model: CatBoostRegressor,
    input_info: dict,
    bathrooms: int,
    bedrooms: int,
    fee: int,
    has_photo : str,
    square_feet: float,
    cityname: str,
    state: str,
    latitude: int,
    longitude: int,
    time: str,
    amenities: list[str],
    pets: list[str]
):
    array = [bathrooms, bedrooms, fee, has_photo, square_feet, cityname, state, latitude, longitude, input_info['time'](time)]
    
    for am in input_info['amenities']:
        if am in amenities:
            array.append(1)
        else:
            array.append(0)
            
    for pet in input_info['pets']:
        if pet in pets:
            array.append(1)
        else:
            array.append(0)
    
    predicted_price = model.predict(array)
    
    return f'${predicted_price:.3f}' 
    