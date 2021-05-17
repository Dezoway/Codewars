def tour(friends, friends_town, home_to_town_distances):
    sum = 0
    tables = {x[0]: x[1] for x in friends_town}
    equals = [home_to_town_distances[tables[x]] for x in friends1 if x in tables.keys()]
    sum += equals[0] + equals[-1]
    for x in range(len(equals)):
        if x != 0 :
            sum += ((equals[x]**2) - (equals[x-1]**2))**(1/2)
    return int(sum)







friends1 = ["A1", "A2", "A3", "A4", "A5"]
ftowns1 = [["A1", "X1"], ["A2", "X2"], ["A3", "X3"], ["A4", "X4"]]
dist_tables = {"X1": 100.0, "X2": 200.0, "X3": 250.0, "X4": 300.0}
print(tour(friends1,ftowns1,dist_tables))