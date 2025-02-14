import json
from friends.models import user

if __name__ == '__main__':
    main()
def main():
    data_string='''
    {
    "people":[
    {"latitude": "12.986375", "user_id": 12, "name": "Chris", "longitude": "77.043701"},
    {"latitude": "11.92893", "user_id": 1, "name": "Alice", "longitude": "78.27699"},
    {"latitude": "11.8856167", "user_id": 2, "name": "Ian", "longitude": "78.4240911"},
    {"latitude": "12.3191841", "user_id": 3, "name": "Jack", "longitude": "78.5072391"},
    {"latitude": "13.807778", "user_id": 28, "name": "Charlie", "longitude": "76.714444"},
    {"latitude": "13.4692815", "user_id": 7, "name": "Frank", "longitude": "-9.436036"},
    {"latitude": "14.0894797", "user_id": 8, "name": "Eoin", "longitude": "77.18671"},
    {"latitude": "13.038056", "user_id": 26, "name": "Stephen", "longitude": "76.613889"},
    {"latitude": "14.1225", "user_id": 27, "name": "Enid", "longitude": "78.143333"},
    {"latitude": "13.1229599", "user_id": 6, "name": "Theresa", "longitude": "77.2701202"},
    {"latitude": "12.2559432", "user_id": 9, "name": "Jack", "longitude": "76.1048927"},
    {"latitude": "12.240382", "user_id": 10, "name": "Georgina", "longitude": "77.972413"},
    {"latitude": "13.2411022", "user_id": 4, "name": "Ian", "longitude": "77.238335"},
    {"latitude": "13.1302756", "user_id": 5, "name": "Nora", "longitude": "77.2397222"},
    {"latitude": "13.008769", "user_id": 11, "name": "Richard", "longitude": "77.1056711"},
    {"latitude": "13.1489345", "user_id": 31, "name": "Alan", "longitude": "77.8422408"},
    {"latitude": "13", "user_id": 13, "name": "Olive", "longitude": "76"},
    {"latitude": "11.999447", "user_id": 14, "name": "Helen", "longitude": "-9.742744"},
    {"latitude": "12.966", "user_id": 15, "name": "Michael", "longitude": "77.463"},
    {"latitude": "12.366037", "user_id": 16, "name": "Ian", "longitude": "78.179118"},
    {"latitude": "14.180238", "user_id": 17, "name": "Patricia", "longitude": "-5.920898"},
    {"latitude": "13.0033946", "user_id": 39, "name": "Lisa", "longitude": "77.3877505"},     {"latitude": "12.228056", "user_id": 18, "name": "Bob", "longitude": "76.915833"},
    {"latitude": "14.133333", "user_id": 24, "name": "Rose", "longitude": "77.433333"},
    {"latitude": "55.033", "user_id": 19, "name": "Enid", "longitude": "78.112"},
    {"latitude": "13.121111", "user_id": 20, "name": "Enid", "longitude": "-9.831111"},
    {"latitude": "11.802", "user_id": 21, "name": "David", "longitude": "-9.442"},
    {"latitude": "14.374208", "user_id": 22, "name": "Charlie", "longitude": "78.371639"},
    {"latitude": "13.74412", "user_id": 29, "name": "Oliver", "longitude": "76.11167"},
    {"latitude": "13.761389", "user_id": 30, "name": "Nick", "longitude": "76.2875"},
    {"latitude": "14.080556", "user_id": 23, "name": "Eoin", "longitude": "77.361944"},
    {"latitude": "12.833502", "user_id": 25, "name": "David", "longitude": "78.122366"}
    ]
    }
    '''
    data = json.loads(data_string)

    for a in data['people']:
        tt=user(userid=a['user_id'],username=a['name'],latitude=a['latitude'],longitude=a['longitude'])
        tt.save()
