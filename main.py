import csv
import sys
import os
import asyncio
import googlemaps
from google.maps import places_v1
from google.type import latlng_pb2
from google.api_core.client_options import ClientOptions
from dotenv import load_dotenv


def nearby_search(lat_, lng_, radius_, key_):
    lat = lat_
    lng = lng_
    radius_meters = radius_ * 1609

    center_point = latlng_pb2.LatLng(latitude=lat, longitude=lng)

    circle_area = places_v1.Circle(center=center_point, radius=radius_meters)

    location_restriction = places_v1.SearchNearbyRequest.LocationRestriction(circle=circle_area)

    client = places_v1.PlacesClient(client_options=ClientOptions(api_key=key_))

    request = places_v1.SearchNearbyRequest(location_restriction=location_restriction, included_types=["restaurant"])

    fieldMask = "places.formattedAddress,places.displayName"

    response = client.search_nearby(request=request, metadata=[("x-goog-fieldmask", fieldMask)])

    return response

def main():
    # Get API key
    load_dotenv()
    API_Key = os.environ.get("GOOGLE_API_KEY")

    # Check API key 
    if API_Key:
        print("\nKey has been loaded first 5 char's:", API_Key[:5], "\n")
    else:
        print("Key not loaded\n")


    # Command line args for zip and search radius 
    zipCode = int(sys.argv[1])
    radiusMiles = int(sys.argv[2])
    api_mode = sys.argv[3]

    print("zip entered was", zipCode, "and radius in miles was", radiusMiles, "\n")

    if(api_mode == 'T'):
        print('API is being used in this run\n')
        # Initialize google maps API to convert zip code to lat and lng
        gmaps = googlemaps.Client(key=str(API_Key))

        #geocode_result = gmaps.geocode(str(zipCode))
        geocode_result = gmaps.geocode('', components={'postal_code': str(zipCode), 'country': 'US'})

        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            lat = location['lat']
            lng = location['lng']
            print(f"latitude: {lat}, longitude: {lng}\n")
        else:
            print("No results found\n")
        
        print(nearby_search(lat, lng, radiusMiles, API_Key))
        
    else:
        print('Not using API for this run\n')





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

if __name__ == "__main__":
    main()




