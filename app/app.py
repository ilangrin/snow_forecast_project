from flask import Flask, render_template
import mysql.connector
import os
from dotenv import load_dotenv
from api import get_ski_resort_forecast  # Make sure api.py is in the same directory

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

# Variables for API
FORECAST_API_URL = os.getenv('FORECAST_API_URL')
API_KEY = os.getenv('API_KEY')  # Your API key

@app.route('/')
def home():
    # Fetch resort data from MySQL
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Resorts")
    resorts = cursor.fetchall()
    cursor.close()
    cnx.close()

    # Assume 'resort_id' is determined here. You may need a way to obtain this dynamically or as part of the request
    resort_id = "999001"  # Example resort ID, replace or adjust as needed

    # Fetch forecast data using the external API function
    forecasts = get_ski_resort_forecast(resort_id, os.getenv('APP_ID'), API_KEY, FORECAST_API_URL)

    return render_template('index.html', resorts=resorts, forecasts=forecasts if forecasts else [])

if __name__ == '__main__':
    app.run(debug=True)