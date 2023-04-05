capitals = {
    "France":"Paris",
    "Germany":"Berlin"
}

travel_log = {
    "France": ["Paris","Lille","Dijon"],
    "Germany": ["Berlin","Hamburg","Stuttgart"]
}
#what if now I want to list how many times I visited each city

#nesting a dictionary in a dictionary
new_travel_log = {
    "France": {"cities_visited":["Paris","Lille","Dijon"], "total_visits": 12},
    "Germany": {"cities_visited":["Berlin","Hamburg","Stuttgart"],"total_visits": 5}
}

#nesting a dictionary in a list

new_travel_log2 = [
    {
    "Country":"France", 
    "cities_visited":["Paris","Lille","Dijon"], 
    "total_visits": 12
    },
    {
    "Country":"Germany", 
    "cities_visited":["Berlin","Hamburg","Stuttgart"],
    "total_visits": 5
    }
]