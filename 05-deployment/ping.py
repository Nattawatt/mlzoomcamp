from flask import Flask, request, redirect, url_for
app = Flask('ping')


@app.route('/ping', methods=['GET'])
def ping():
    return "PONG55"

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port = 9696)