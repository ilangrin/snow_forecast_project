from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv
print(os.getcwd())
# Load environment variables
load_dotenv()


app = Flask(__name__)

@app.route('/home')
def home():
    
    app_id = os.getenv('APP_ID', '5e1b5987')
    api_key = os.getenv('API_KEY', '7f5ccb4dcebb3e586aeb5a50f06d9d18')
    forecast_api_url = os.getenv('FORECAST_API_URL', 'https://api.weatherunlocked.com')
    ski_resort_id = '124' 

    request_url = f"{forecast_api_url}/api/resortforecast/{ski_resort_id}?app_id={app_id}&app_key={api_key}"

    response = requests.get(request_url)
    
    if response.status_code == 200:
        forecast_data = response.json()
        return render_template('forecast.html', resort=forecast_data, error=None)
    else:
        error_message = f"Failed to fetch forecast data. Status Code: {response.status_code}"

        return render_template('forecast.html', resort=None, error=error_message)



if __name__ == '__main__':
    app.run(debug=True)
