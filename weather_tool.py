from geopy.geocoders import Nominatim
import argparse
import geocoder

from setup import get_hourly_response

parser = argparse.ArgumentParser()

parser.add_argument("location", help="this is the location of the app, default is 'here'", nargs='*')

args = parser.parse_args()

if args.location:
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(" ".join(args.location))
    params = {
        'latitude': location.latitude,
        'longitude': location.longitude,
        'hourly': ["temperature_2m", "precipitation_probability", "rain", "wind_speed_10m"]
    }

else:
    latlng = geocoder.ip('me').latlng
    print(latlng)
    params = {
        'latitude': '43.464951',
        'longitude': '-80.523911',
        'hourly': ["temperature_2m", "precipitation_probability", "rain", "wind_speed_10m"]
    }

out_df = get_hourly_response(params)
out_df = out_df.rename(columns={"temperature_2m": "Temp (oC)", "precipitation_probability": "Chance of Rain (%)", "wind_speed_10m": "wind"})
print(out_df.loc[:, out_df.columns != 'date'])