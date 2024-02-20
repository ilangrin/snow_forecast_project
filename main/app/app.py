from flask import Flask, render_template
import mysql.connector
from api import get_ski_resort_forecast

app = Flask(__name__)

@app.route('/')
def home():
    # Direct database configuration
    db_config = {
        'user': 'ilangrin',
        'password': 'Uri@2604198200',
        'host': 'localhost',
        'database': 'snowresortdb'
    }
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Resorts")
    resorts = cursor.fetchall()
    cursor.close()
    cnx.close()

    
    resort_id = "124"  
    forecasts = get_ski_resort_forecast(resort_id, '5e1b5987', '7f5ccb4dcebb3e586aeb5a50f06d9d18', 'https://api.weatherunlocked.com', hourly_interval=6, num_of_days=3)

    return render_template('index.html', resorts=resorts, forecasts=forecasts if forecasts else [])

if __name__ == '__main__':
    app.run(debug=True)
