from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    return "Hello!"

@app.route('/get_locations', methods=['GET'])
def get_locations():
    locations = util.get_locations()
    res = jsonify([location.title() for location in locations])
    res.headers.add('Access-Control-Allow-Origin', '*')

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
    res.headers.add('Access-Control-Allow-Origin', '*')


    return res

if __name__ == '__main__':
    print("Starting Flask App...")
    util.load_saved_artifacts()
    app.run()