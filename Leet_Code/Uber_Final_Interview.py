def car_count(list1):
    car_track = {}
    for a,b in list1:
        if a not in car_track:
            car_track[a] = []
        car_track[a].append(b)
        if b not in car_track:
            car_track[b] = []
        car_track[b].append(a)
        visited = set()
        cars = 0

    def dfs(i):
        visited.add(i)
        for car in car_track[i]:
            if car not in visited:
                dfs(car)

    for car in car_track:
        if car not in visited:
            cars += 1
            dfs(car)
    return cars

print(car_count([(0,1), (1,3),(2,4)]))
