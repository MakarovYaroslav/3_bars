import json


def load_data(filepath):
    data =[]
    with open(filepath) as data_file:    
        data = json.load(data_file)
    return data

def get_biggest_bar(data):
    seat_count = data[0]['Cells']['SeatsCount']
    for bar in data:
        if bar['Cells']['SeatsCount']>seat_count:
            seat_count = bar['Cells']['SeatsCount']
            biggest_bar = bar['Cells']['Name']
    return biggest_bar


def get_smallest_bar(data):
    seat_count = data[0]['Cells']['SeatsCount']
    for bar in data:
        if bar['Cells']['SeatsCount']<seat_count:
            seat_count = bar['Cells']['SeatsCount']
            smallest_bar = bar['Cells']['Name']
    return smallest_bar


def get_closest_bar(data, longitude, latitude):
    difference = abs(longitude-data[0]['Cells']['geoData']['coordinates'][0]) + abs(latitude-data[0]['Cells']['geoData']['coordinates'][1])
    closest_bar = data[0]['Cells']['Name']
    for bar in data:
        if (abs(longitude-bar['Cells']['geoData']['coordinates'][0])+abs(latitude-bar['Cells']['geoData']['coordinates'][1])) < difference:
            difference = abs(longitude-bar['Cells']['geoData']['coordinates'][0])+abs(latitude-bar['Cells']['geoData']['coordinates'][1])
            closest_bar = bar['Cells']['Name']
    return closest_bar    
            

if __name__ == '__main__':
    #проверка работоспособности
    print(get_biggest_bar(load_data('bars.json')))
    print(get_smallest_bar(load_data('bars.json')))
    longitude = float(input('Input your gps coordinates(longitude):'))
    latitude = float(input('Input your gps coordinates(latitude):'))
    print(get_closest_bar(load_data('bars.json'),longitude,latitude))
