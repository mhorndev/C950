# Mark Horn / Student ID: 001069917

from Truck import Truck
from datetime import datetime

# TruckTable object
# stores all of the Truck objects in a table

class Trucks(object):

    def __init__(self):
        self._trucks = []

        truck = Truck(1)
        self._trucks.append(truck)

        # holding this truck at the hub until delayed packages arrive
        truck = Truck(2)
        truck.clock = datetime.now().replace(hour=9, minute=5, second=0, microsecond=0)
        self._trucks.append(truck)

    # returns all trucks
    # O(1)
    def all(self):
        return self._trucks

    # return one truck, by it's number
    # O(1)
    def get(self, number):
        for truck in self._trucks:
            if truck.number == number:
                return truck

# Access the TruckTable in a global scope
TruckTable = Trucks()
