import math


def closestStraightCity(cities, x_cor, y_cor, query_city):
    min_dist_city = "None"
    min_distance = math.inf

    index = cities.index(query_city)
    x = x_cor[index]
    y = y_cor[index]

    for i in range(len(cities)):
        if i != index and (x_cor[i] == x or y_cor[i] == y):
            city_distance = abs(x - x_cor[i]) + abs(y - y_cor[i])

            if city_distance < min_distance or (city_distance == min_distance and cities[i] < query_city):
                min_distance = city_distance
                min_dist_city = cities[i]

    return min_dist_city


def nearestCity(cities, x_cor, y_cor, queries):
    output = []
    for query_city in queries:
        output.append(closestStraightCity(cities, x_cor, y_cor, query_city))

    return output
