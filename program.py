import json
import urllib.request

map_city_to_coords = {
    'Abuja': 'lat=9.02&lon=7.31',
    'Nairobi': 'lat=1.3&lon=36.85',
    'Accra': 'lat=5.63&lon=0.39W'
}

# showing weather in a more friendly way - updated version
def show_weather_to_user(weather_data_list):
    output_str = ""
    for weather_data in weather_data_list:
        hour_number = weather_data['timepoint']
        temperature = weather_data['temp2m']
        output_str += f'On day {hour_number},\n'
        if hour_number == 24:
            output_str += '(in one day)\n'
        elif hour_number == 48:
            output_str += '(in two days)\n'
        elif hour_number == 72:
            output_str += '(in three days)\n'
        output_str += f'The temperature is {temperature}\n'
    return output_str

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
        


# testing output `show_weather_to_user` without actually printing to the console
output_str = show_weather_to_user(weather_data_list)
print(output_str) 
