superhero = {
    "name": "Wonder Woman",
    "alias": "Diana Prince",
    "gear": [
        "Lasso of Truth",
        "Bracelets of Submission"
    ],
    "vehicle": {
        "title": "Invisible Jet",
        "speed": "2000 mph",
        "miles_traveled": 50000
    }
}

def add_miles_traveled(vehicle, how_many):
    vehicle["miles_traveled"] += how_many

add_miles_traveled(superhero['vehicle'], 100)

print(superhero['vehicle']["miles_traveled"])