import requests
import time


def getStreetNameFromApi(point, apikey):
        parameters = {
            "key": apikey,
            "location": str(point.lat) + "," + str(point.lon),
            "includeRoadMetadata" : "true",
            "includeNearestIntersection" : "true"
        }
        response = requests.get(
            "http://www.mapquestapi.com/geocoding/v1/reverse",
            params=parameters)
        try:
            addy = str(response.json()['results'][0]['locations'][0]['street'])

            #we need to strip the numbers from the street name
            try:
                word = addy.split()[0]
                #print("word is: ", word, " ", all(i.isdigit() for i in word), " ", type(addy))
                if(all(i.isdigit() for i in word)):
                    addy = addy.split(' ', 1)[1]
                    #print("new address: " ,addy)
            except:
                print("couldnt be parsed")
        except:
            print(response)

        return addy
