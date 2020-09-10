#!/usr/bin/env python3
import yaml


#Convert people list of dictionaries into YAML file
people = [
    {
        "name": "Sabrina Green",
        "username": "sgreen",
        "phone": {
            "office": "802-867-5309",
            "cell": "802-867-5310"
        },
        "department": "IT Infrastructure",
        "role": "Systems Administrator"
    },
    {
        "name": "Eli Jones",
        "username": "ejones",
        "phone": {
            "office": "684-348-1127"
        },
        "department": "IT Infrastructure",
        "role": "IT Specialist"
    },
]


with open('people.yaml', 'w') as people_yaml:
    yaml.safe_dump(people, people_yaml)
