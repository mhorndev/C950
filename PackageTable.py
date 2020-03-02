# Mark Horn / Student ID: 001069917

import csv

from DistanceTable import DistanceTable
from Package import Package

# This is the main hash table for the program
# It should be accessed in a global scope via PackageTable = Packages()

class Packages(object):

    def __init__(self, capacity=10):
        self._table = []
        self.keys = []
        self._struct(capacity)

        # import the data
        with open('csv/packages.csv') as file:
            data = csv.reader(file)
            for row in data:
                package = Package(row)
                self.insert(package.id, package)

    # create the buckets
    # O(1)
    def _struct(self, capacity):
        for i in range(capacity):
            self._table.append([])

    # creates the hash of the identifier for each package object
    # O(1)
    def _hash(self, key):
        return hash(str(key)) % len(self._table)

    # insert a package object by its key
    # O(1)
    def insert(self, key, value):
        self.keys.append(key)
        bucket = self._table[self._hash(key)]
        bucket.append(value)

    # get a package object by its key
    # O(1)
    def get(self, key):
        bucket = self._table[self._hash(key)]
        for obj in bucket:
            if obj.id == key or str(obj.id) == key:
                return obj
        return None

    # get all packages
    # O(N)
    def all(self):
        packages = []
        for bucket in self._table:
            for package in bucket:
                packages.append(package)
        return packages

    # get all available packages
    # only return packages at the hub
    # O(N)
    def available(self):
        result = []
        for bucket in self._table:
            for obj in bucket:
                if obj.location == 0:
                    obj.distance = DistanceTable.get(0, obj.destination)
                    result.append(obj)
        return sorted(result, key=lambda package: package.distance)

    # get all undelivered packages
    # same as available packages, but will include delays, on truck, etc
    # O(N)
    def undelivered(self):
        result = []
        for bucket in self._table:
            for obj in bucket:
                if "Delivered" not in obj.status:
                    result.append(obj)
        return result

    # will return packages in the current time frames
    # .priority is set in the package object
    # O(N)
    def priority(self):
        result = []
        for bucket in self._table:
            for obj in bucket:
                if obj.priority and obj.location == 0:
                    obj.distance = DistanceTable.get(0, obj.destination)
                    result.append(obj)
        return sorted(result, key=lambda package: package.distance)

    # returns all non-priority packages
    # O(N)
    def standard(self):
        result = []
        for bucket in self._table:
            for obj in bucket:
                if obj.standard and obj.location == 0:
                    obj.distance = DistanceTable.get(0, obj.destination)
                    result.append(obj)
        return sorted(result, key=lambda package: package.distance)

    # returns all packages that are bound to each other via constraints
    # O(N)
    def linked(self):
        packages = []
        for bucket in self._table:
            for package in bucket:
                if package.bound_to_package and package.location == 0:
                    packages.append(package)
        return packages


# import this object in other files in a global scope
PackageTable = Packages()
