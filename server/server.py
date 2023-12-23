from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)
print("Starting Flask App...")
util.load_saved_artifacts()


@app.route('/get_locations', methods=['GET'])
def get_locations():
    locations = util.get_locations()
    res = jsonify([location.title() for location in locations])

    return res

@app.route('/get_predicted_price', methods=['POST'])
def get_predicted_price():
    data = request.get_json()

    sqft = data['sqft']
    bath = data['bath']
    bhk = data['bhk']
    location = data['location']

    price = util.get_predicted_price(sqft, bath, bhk, location)
    res = jsonify({
        "price": price
    })

    return res

if __name__ == '__main__':
    app.run()