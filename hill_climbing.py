from random import choice

tsp = [
    [0, 400, 500, 300],
    [400, 0, 300, 500],
    [500, 300, 0, 400],
    [300, 500, 400, 0]
]

def createRandomRoute(tsp):
    noOfCities = len(tsp)
    cities = [i for i in range(noOfCities)]
    route = []
    while cities:
        newCity = choice(cities)
        route.append(newCity)
        cities.remove(newCity)
    return route


def findRouteLength(route):
    pass

route = createRandomRoute(tsp)
print(route)
route = [2,1,3,0]
findRouteLength(route)
