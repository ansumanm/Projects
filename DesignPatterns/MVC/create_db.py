import json

data = [
        { 'first_name': 'Arnold',
            'last_name': 'Schwarzeneggar'},
        { 'first_name': 'Sylvestor',
            'last_name': 'Stallone'},
        { 'first_name': 'Dwyane',
            'last_name': 'Jhonson'},
        { 'first_name': 'Vidit',
            'last_name': 'Jammal'}
        ]

with open("db.txt", "w") as write_file:
        json.dump(data, write_file)
