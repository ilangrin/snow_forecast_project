from flask import Flask, render_template
import os
from dotenv import load_dotenv
from main.api import get_ski_resort_forecast
import mysql.connector
# Load environment variables
load_dotenv()
app = Flask(__name__)

@app.route('/')


def home():
    # Fetch resort data from MySQL
    db_config = {
        'user': os.getenv('DB_USER', 'myapp'),  # It's good practice to also use environment variables for these
        'password': os.getenv('DB_PASSWORD', 'secret'),
        'host': os.getenv('DB_HOST', 'localhost'),
        'database': os.getenv('DB_NAME', 'resorts')
    }
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Resorts")
    resorts = cursor.fetchall()
    cursor.close()
    cnx.close()

    # Assume 'resort_id' is determined here. You may need a way to obtain this dynamically or as part of the request
    resort_id = "54887871"  # This should be dynamically determined based on your application's logic
    forecasts = get_ski_resort_forecast(resort_id, os.getenv('APP_ID'), os.getenv('API_KEY'), os.getenv('FORECAST_API_URL'), hourly_interval=6, num_of_days=3)

    return render_template('index.html', resorts=resorts, forecasts=forecasts if forecasts else [])



if __name__ == '__main__':
    app.run(debug=True)