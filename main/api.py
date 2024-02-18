# api.py
import requests

def get_ski_resort_forecast(resort_id, app_id, app_key, forecast_api_url, hourly_interval=None, num_of_days=None):
    # Construct the base URL
    params = {
        "app_id": app_id,
        "app_key": app_key
    }
    # Add optional parameters if provided
    if hourly_interval:
        params["hourly_interval"] = hourly_interval
    if num_of_days:
        params["num_of_days"] = num_of_days

    # Construct the full URL with optional parameters
    full_api_url = f"{forecast_api_url}/api/resortforecast/{resort_id}"
    
    # Make the request with parameters
    response = requests.get(full_api_url, params=params, headers={"Accept": "application/json"})
#   
    if response.status_code == 200:
        return response.json()  # Return the parsed JSON response
    else:
        # Log error or handle it based on your application's needs
        print(f"Error fetching forecast: {response.status_code}")
        return None

