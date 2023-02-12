import requests
from typing import Dict

# connect to a "real" API

## Example: OpenWeatherMap
#URL = "https://api.openweathermap.org/data/2.5/weather"
URL = "https://www.reddit.com/dev/api/"

# TODO: get an API key from openweathermap.org and fill it in here!
API_KEY = "213be797bae0c72c8f1f27bb11f2888f"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY})
    return res.json()
    
def get_connection() -> Dict:
	secret_token = "k8ZKQSOkc2LpKYd-mrg_iya1PE84IQ"
	personal_use_script = "3q3oF8AdxgMTxbWpuMoJFQ"
	
	auth = requests.auth.HTTPBasicAuth(personal_use_script, secret_token)
	
	data = {'grant_type': 'password',
		'username': 'csw5011',
		'password': '1999November'}
		
	headers = {'User-Agent': 'EE250 Lab 3/0.0.1'}
	
	res = requests.post('https://www.reddit.com/api/v1/access_token',
				auth = auth, data = data, headers = headers)
				
	return res.json()
	
	
# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)

def main():
    temp = get_weather("London")
    print(temp)

if __name__ == "__main__":
    response = get_connection()
    print(response)
