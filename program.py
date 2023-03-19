import json
import urllib.request

map_city_to_coords = {
    'Abuja': 'lat=9.02&lon=7.31',
    'Nairobi': 'lat=1.3&lon=36.85',
    'Accra': 'lat=5.63&lon=0.39W'
}

# showing weather in a more friendly way
def show_weather_to_user(weather_data_list):
    for weather_data in weather_data_list:
        hour_number = weather_data['timepoint']
        temperature = weather_data['temp2m']
        print(f'On day {hour_number},')
        if hour_number == 24:
            print('(in one day)')
        elif hour_number == 48:
            print('(in two days)')
        elif hour_number == 72:
            print('(in three days)')
            
        print(f'The temperature is {temperature}')

def show_weather():
    
    city_name = input('Enter a city: ')
    if city_name not in map_city_to_coords:
        print('We do not have coordinates for that city.')
    else:
        get_api_results(city_name)
        with open('api_output.json', 'r') as f:
            all_data = json.load(f)
            weather_data_list = all_data['dataseries']
            
        show_weather_to_user(weather_data_list)



def get_api_results(city):
    # city = 'Abuja'
    coords = map_city_to_coords[city]
    url = ('https://www.7timer.info/bin/astro.php?' + f'{coords}&ac=0&unit=metric&output=json')
    results = urllib.request.urlopen(url)
    json_content = results.read().decode('utf-8')
    # with open('api_output.json', 'w') as f:
    #     f.write(json_content)
    return json_content
        
        
show_weather()
        


# Getting the new coordinated format

# This is the initial program. The walkthrough shows how to modify this code.
# At the end of the walkthrough, this code will read and write to a json file.
#
# You can see the completed code after the walkthrough by going here,
# https://github.com/kibo-programming-2-jan-23/walkthroughs/tree/main/show-weather-from-file/end

## Change the current city
# At the end of the program, ask the user if they would like to change the current city. If they type yes, let them type in a city, and then store that as the current city.
