# nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# nesting list in a dict

travel_log = {
    "France": ["Paris", "Lille", "Djon"],
    "India": ["Mumbai", "Gujarat", "Delhi"],
}

# nestig list in a list

lst1 = ["a", "b", ["c1", "c2", "c3"], "d"]

# Nesting dict in a dict
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Djon"],
    }
}


print(travel_log["France"]["cities_visited"])

# Nesting dic tina  list
travel_log = [
    {"country": "France", "cities_visited": ["Paris", "lille", "djon"]},
    {"country": "India", "cities_visited": ["mumbai", "pune", "delhi"]},
]
