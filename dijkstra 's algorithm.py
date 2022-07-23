
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
        if all([link != x for x in self._links]):
            self._links.append(link)
            if link.v1 not in self._vertex:self._vertex.append(link.v1)
            if link.v2 not in self._vertex:self._vertex.append(link.v2)

    def find_path(self, start_v, stop_v):
        print(self._vertex[0].links)
        #print(start_v.__class__)
        print(stop_v.links)


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



map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))
