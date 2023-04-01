
import requests

# https://geolocation-db.com/json/{ip}&position=true
# https://ipdata.co/flags/{country_code}.png
ip = ''

def get_flag(ip):
	res = requests.get(f'https://geolocation-db.com/json/{ip}&position=true')
	country_code = res.json()['country_code'].lower()
	return f'https://ipdata.co/flags/{country_code}.png'

print(get_flag(ip))
