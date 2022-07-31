
class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links


class Link:
    def __init__(self, v1 , v2, dist = 1):
        self._v1 = v1
        self._v2 = v2
        self._dist = dist
        self._v1.links.append(self)

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        self._dist = value


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v):
        if v not in self._vertex:self._vertex.append(v)

    def add_link(self, link):
        if (link.v1,link.v2) not in [(x.v1, x.v2) for x in self._links] and (link.v1, link.v2) not in [(x.v2, x.v1) for x in self._links]:
            self._links.append(link)
            if link.v1 not in self._vertex:self._vertex.append(link.v1)
            if link.v2 not in self._vertex:self._vertex.append(link.v2)

    def find_path(self, start_v, stop_v):
        routes = dict()
        for x in self._links:
            if x.v1 not in routes:
                routes[x.v1] = [[x.v2, x.dist]]
            if x.v1 in routes and [x.v2, x.dist] not in routes[x.v1]:
                routes[x.v1].append([x.v2, x.dist])
            if x.v2 not in routes:
                routes[x.v2] = [[x.v1, x.dist]]
            if x.v2 in routes and [x.v1, x.dist] not in routes[x.v2]:
                routes[x.v2].append([x.v1, x.dist])
        vertexes = {x:[None, 0] if x == start_v else [None, 999] for x in routes.keys()}
        non_visit = [x for x in routes.keys()]
        while non_visit:
            min_elem = min([x for x in vertexes.keys() if x in non_visit], key=lambda x:vertexes[x][1])
            for x in routes[min_elem]:
                if vertexes[x[0]][1] > vertexes[min_elem][1] + x[1]:
                    vertexes[x[0]][1] = vertexes[min_elem][1] + x[1]
                    vertexes[x[0]][0] = min_elem
            del non_visit[non_visit.index(min_elem)]
        initial = vertexes[stop_v]
        best_route = [stop_v]
        links = [x for x in self._links if (x.v1 == stop_v and x.v2 == initial[0]) or (x.v1 == initial[0] and x.v2 == stop_v)]
        while initial[0]:
            best_route.append(initial[0])
            k = initial[0]
            initial = vertexes[initial[0]]
            links += [x for x in self._links if (x.v1 == k and x.v2 == initial[0]) or (x.v1 == initial[0] and x.v2 == k)]

        return list(reversed(best_route)),links




class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1,v2,dist)
