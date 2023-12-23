import json
import joblib
import numpy as np

__data_columns = None
__locations = None
__model = None


def load_saved_artifacts():
    print("Loading saved artifacts...")
    global __data_columns
    global __locations
    if __data_columns is None or __locations is None:
        with open("./artifacts/columns.json", "r") as f:
            __data_columns = json.load(f)['data_columns']
            __locations = __data_columns[3:] #* Since first three are sqft, bath, bhk

    global __model
    if __model is None:
        __model = joblib.load("./artifacts/banglore_home_prices_model.pkl")


def get_locations():
    return __locations

def get_data_columns():
    return __data_columns

def get_predicted_price(total_sqft, bath, bhk, location):
    num_of_data_cols = len(__data_columns)

    try:
        location_index = __data_columns.index(location.lower())
    except:
        return "location not found"

    X = np.zeros(num_of_data_cols)
    X[0] = total_sqft
    X[1] = bath
    X[2] = bhk
    X[location_index] = True

    return round(__model.predict([X])[0], 2)


if __name__ == "__main__":
    load_saved_artifacts()
    print(__data_columns)
    print(__locations)
    print(get_predicted_price(1000, 3, 3,'1st Phase JP Nagar'))

