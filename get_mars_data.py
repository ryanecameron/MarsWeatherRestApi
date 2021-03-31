import requests
import secrets

BASE = "http://127.0.0.1:5000/mars_weather_data/"
FINAL_URL = f'https://api.nasa.gov/insight_weather/?api_key={secrets.api_key}&feedtype=json&ver=1.0'
sol_data = {}


def get_data():
    response = requests.get(FINAL_URL)
    if response.status_code != 200:
        print(response.text)
        return []
    json_data = response.json()
    available_sols = json_data["sol_keys"]
    print(available_sols)

    for sols in available_sols:
        current_sol_data = {}
        sol_json_data = json_data[sols]
        sol_data["sol_id"] = sols
        if "AT" in sol_json_data:
            current_sol_data["temperature"] = sol_json_data["AT"]["av"]
        else:
            current_sol_data["temperature"] = None
        if 'PRE' in sol_json_data:
            current_sol_data["pressure"] = sol_json_data["PRE"]['av']
        else:
            current_sol_data["pressure"] = None
        if 'HWS' in sol_json_data:
            current_sol_data["horizontal_wind_speed"] = sol_json_data["HWS"]['av']
        else:
            current_sol_data["horizontal_wind_speed"] = None

        if 'Season' in sol_json_data:
            current_sol_data["season"] = sol_json_data['Season']
        else:
            current_sol_data["season"] = None

        #print(str(sols), current_sol_data)
        results = str(sols), current_sol_data
        #response = requests.delete(BASE + str(sols))
        #response = requests.put(BASE + str(sols), current_sol_data)
    return results

def main():
    print(get_data())



