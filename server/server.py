from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    return "Hello!"


if __name__ == '__main__':
    print("Starting Flask App...")
    app.run()