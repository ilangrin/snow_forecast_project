from flask import Flask, render_template, jsonify
import mysql.connector
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Database Configuration from Environment Variables
db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

# API Endpoint and Key from Environment Variables
FORECAST_API_URL = os.getenv('FORECAST_API_URL', 'https://api.weatherunlocked.com')
App_name = os.getenv('App_name')
App_ID = os.getenv('App_ID')
API_KEY = os.getenv('API_KEY')

@app.route('/')
def home():
    # Fetch resort data from MySQL
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Resorts")
    resorts = cursor.fetchall()
    cursor.close()
    cnx.close()

    # Construct full API request URL with key if needed
    full_api_url = f"{FORECAST_API_URL}?app_id={API_KEY}"

    # Fetch forecast data from API
    api_response = requests.get(full_api_url)
    api_forecasts = response.json() if response.status_code == 200 else []

    return render_template('index.html', resorts=resorts, forecasts=forecasts)

if __name__ == '__main__':
    app.run(debug=True)


    # Fetch forecast data from API
    api_response = requests.get(FORECAST_API_URL)
    api_forecasts = response.json() if response.status_code == 200 else []

    return render_template('index.html', resorts=resorts, forecasts=forecasts)

if __name__ == '__main__':
    app.run(debug=True)
