# Mark Horn / Student ID: 001069917

from TruckTable import TruckTable
from PackageTable import PackageTable
from LocationTable import LocationTable
from DistanceTable import DistanceTable

# Vertex class is the container for the Location object

class Vertex:

    # Vertex initialization method
    def __init__(self, location):
        # add the Location object to the vertex (LocationTable.py)
        self.location = location

# Graph class is the graph of all locations (for each truck manifest)

class Graph:

    # Graph initialization method
    def __init__(self):

        # the vertices (locations) table
        self.vertices = {}

        # the edges (distances) between the locations
        self.edges = {}

    # method to add a vertex (location) to the graph
    def add_vertex(self, location):
        self.vertices[location] = Vertex(location)

    # method to add an edge (distance) to the graph
    def add_edge(self, a, b, distance):
        self.edges[(a, b)] = distance

# This is the shortest path algorithm, based on Dijkstra and Hamiltonian path
# Input is the graph and start location, Output is a list
# Worst-case O(N^2)

def Dijkstra(graph, start):
    visited = []
    unvisited = []

    # loop through the graph vertices (locations) and put them in the unvisited
    for vertex in graph.vertices:
        unvisited.append(vertex)

    # loop through the unvisited vertices and assign the distance from the distance table
    for i in range(1, len(unvisited)):
        location = LocationTable.get(unvisited[i].location)
        unvisited[i].distance = DistanceTable.get(0, location)

    # iterate and repeat until all locations (unvisited) is []
    while len(unvisited) > 0:
        idx = 0
        for i in range(1, len(unvisited)):
            if unvisited[i].distance < unvisited[i].distance:
                idx = i
        vertex = unvisited.pop(idx)

        # Check all potential paths from the location to all neighboring locations
        for next_vertex in graph.vertices[vertex]:
            location = LocationTable.get(next_vertex.id)
            distance = graph.edges[(vertex, next_vertex)]
            calculated_distance = vertex.distance + distance

            # if better path, update it
            if calculated_distance < next_vertex.distance:
                next_vertex.distance = calculated_distance
                continue

    return visited

# Test load / simulation
def sort_manifest(truck):
    for package in truck.manifest:
        package.distance = DistanceTable.get(truck.location, package.destination)
    return sorted(truck.manifest, key=lambda x: x.distance)

# load truck 1, based on constraints given in the file
truck1 = TruckTable.get(1)
for id in [14, 15, 16, 34, 20, 21, 19, 1, 7, 29, 37, 30, 13, 39, 27, 35]:
    truck1.load_package(PackageTable.get(id))
while truck1.manifest:
    truck1.manifest = sort_manifest(truck1)
    truck1.deliver(truck1.manifest.pop(0))
truck1.return_to_hub()

# load truck 2, based on constraints given in the file
truck2 = TruckTable.get(2)
for id in [25, 26, 22, 24, 28, 4, 40, 31, 32, 17, 6, 36, 12, 18, 23, 11]:
    truck2.load_package(PackageTable.get(id))
while truck2.manifest:
    truck2.manifest = sort_manifest(truck2)
    truck2.deliver(truck2.manifest.pop(0))
truck2.return_to_hub()

# using truck 2 ro reload, due to package constraints
truck2 = TruckTable.get(2)
for id in [2, 33, 10, 5, 38, 8, 9, 3]:
    truck2.load_package(PackageTable.get(id))
while truck2.manifest:
    truck2.manifest = sort_manifest(truck2)
    truck2.deliver(truck2.manifest.pop(0))
truck2.return_to_hub()