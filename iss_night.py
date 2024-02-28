import requests
import datetime as DT


My_latitude = 51.458540
My_longitude = -0.333660


parameters = {
    'lat': My_latitude,
    'lng': My_longitude,
    'formatted': 0
}




def locationsISS():

    iss_loc = requests.get("http://api.open-notify.org/iss-now.json")
    iss= iss_loc.json()
    latitude= float(iss["iss_position"]["latitude"])
    longitude = float(iss["iss_position"]["longitude"])

    if -5+ My_latitude <= latitude <= 5 + My_latitude and -5+ My_longitude <= longitude <= 5 + My_longitude :

    # Your code here if the condition is True
        print("Latitude and longitude are within the specified range.")
        return True

    else:
    # Your code here if the condition is False
        print("Latitude and/or longitude are outside the specified range.")
        return False





def sunrise_sunset():

    sunrise_sunset = requests.get("https://api.sunrise-sunset.org/json",parameters )

    sunrise_sunset_data= sunrise_sunset.json()


    #sunrise time
    full_sunrise= sunrise_sunset_data['results']['sunrise']
    sunrise =full_sunrise.split("T")
    time_sunrise  = sunrise[1].split("+")[0]
    
          
    # sunset time
    full_sunset= sunrise_sunset_data['results']['sunset']
    sunset =full_sunset.split("T")
    time_sunset  = sunset[1].split("+")[0]

    time_data = DT.datetime.now()
    formatted_time = time_data.strftime("%Y-%m-%d %H:%M:%S")
    date_part, now_time = formatted_time.split(" ")

    time_format = "%H:%M:%S"

# Convert strings to datetime objects
    time_sunrise =DT.datetime.strptime(time_sunrise, time_format).time()
    time_sunset = DT.datetime.strptime(time_sunset, time_format).time()
    now_time = DT.datetime.strptime(now_time, time_format).time()

    if time_sunset < now_time or now_time < time_sunrise:
        return True
    else:
        return False




if sunrise_sunset() and locationsISS():
    print("Latitude and longitude are within the specified range and time you will be able see ISS")
else:
    print("Latitude and/or longitude are outside the specified range and time, you won't able to see ISS.")




