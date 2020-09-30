def numBusesToDestination( routes, S, T):
    """
    :type routes: List[List[int]]
    :type S: int
    :type T: int
    :rtype: int
    """
    station2route = dict()

    for i,route in enumerate(routes):
        for station in route:
            if station in station2route:
                station2route[station].append(i)
            else:
                station2route[station]=[i]

    cur_routes = station2route[S]
    target_routes =set(station2route[T])
    used_routes= dict()

    change_bus = 1
    for route_id in cur_routes:
        if route_id in target_routes:
            return change_bus
        used_routes[route_id]=1
    used_station = dict()
    while cur_routes:
        change_bus+=1
        next_routes =[]
        for route_id in cur_routes:
            for station_id in routes[route_id]:
                if station_id not in used_station:
                    for next_route_id in station2route[station_id]:
                        if next_route_id not in used_routes:
                            if next_route_id in target_routes:
                                return change_bus
                            next_routes.append(next_route_id)
                            used_routes[next_route_id]=1
                    used_station[station_id]=1
        cur_routes = next_routes

    return -1

routes = [[1, 2, 7], [3, 6, 7]]
S=1
T=6

print(numBusesToDestination(routes,S,T))

