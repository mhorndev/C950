# Mark Horn / Student ID: 001069917

import csv
from Location import Location

# The LocationTable object class
# O(N)

class Locations(object):

    def __init__(self):
        self.locations = []

        # load the csv into the Object
        with open('csv/locations.csv') as file:
            data = csv.reader(file)
            for row in data:
                self.locations.append(Location(row))

    # returns all locations
    def all(self):
        return self.locations

    # return the location requested
    # using param, lookup by either address(str) or id(int)
    def get(self, param):
        if type(param) == int:
            for location in self.locations:
                if location.id == param:
                    return location
        if type(param) == str:
            for location in self.locations:
                if location.address == param:
                    return location

# import this, to access this object in a global scope
LocationTable = Locations()
