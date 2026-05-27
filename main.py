import csv
import sys
import os
import googlemaps
from dotenv import load_dotenv

# Get API key
load_dotenv()
API_Key = os.environ.get("GOOGLE_API_KEY")

# Check API key 
if API_Key:
    print("Key has been loaded first 10 char's:", API_Key[:10])
else:
    print("Key not loaded")


# Command line args for zip and search radius 
zipCode = sys.argv[1]
radiusMiles = sys.argv[2]

# Initialize google maps API to convert zip code to lat and lng
gmaps = googlemaps.Client(key=str(API_Key))

#geocode_result = gmaps.geocode(str(zipCode))
geocode_result = gmaps.geocode('', components={'postal_code': str(zipCode), 'country': 'US'})

if geocode_result:
    location = geocode_result[0]['geometry']['location']
    lat = location['lat']
    lng = location['lng']
    print(f"latitude: {lat}, longitude: {lng}")
else:
    print("No results found")


print("zip entered was", zipCode, "and radius in miles was", radiusMiles)




#csv test
headers = ["Test1", "Test2", "Test3"]
rows = [
    ["1", "2", "3"],
    ["4", "5", "6"]
]

with open("output.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(rows)