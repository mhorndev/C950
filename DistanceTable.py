# Mark Horn / Student ID: 001069917

import csv

# This is a DistanceTable object
# O(N)

class Distances(object):

    def __init__(self):
        self._table = {}

        # load the csv data into the object
        with open('csv/distances.csv') as file:
            data = csv.reader(file)
            for i, row in enumerate(data):
                for j, distance in enumerate(row):
                    if distance != '':
                        # make it bi-directional
                        self._table[(i, j)] = float(distance)
                        self._table[(j, i)] = float(distance)

    # returns the distance between 2 locations, origin and destination
    def get(self, origin, destination):
        return self._table[(origin, destination)]

    # returns the entire table
    def all(self):
        return self._table

# import this object in other files, in a global scope
DistanceTable = Distances()