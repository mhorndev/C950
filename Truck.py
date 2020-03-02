# Mark Horn / Student ID: 001069917

from datetime import datetime, timedelta

from DistanceTable import DistanceTable

# This is the truck object
# Contains the methods needed to track mileage/time, etc

class Truck(object):
    def __init__(self, number):
        self.number = number
        self.location = 0
        self.odometer = 0
        self.capacity = 16
        self.manifest = []
        self.history = []
        self.clock = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)

    # deliver the package, update the package, as well as the odometer, clock, etc
    # O(1)
    def deliver(self, package):
        distance = DistanceTable.get(self.location, package.destination)
        elapsed = timedelta(seconds=distance * 3600 / 18)
        self.odometer += distance
        self.clock += elapsed
        self.location = package.destination
        deadline_met = ""
        if self.clock > package.deadline:
            deadline_met = ", LATE"
        else:
            deadline_met = ", ON TIME"
        if package.destination not in self.history:
            self.history.append(package.destination)

        package.set_status(self.clock, "DELIVERED" + ", TRUCK " + str(self.number) + " @ " + str(self.clock) + deadline_met)
        package.status = (self.clock, "DELIVERED" + ", TRUCK " + str(self.number) + " @ " + str(self.clock) + deadline_met)

    # update the odometer, clock, etc
    # O(1)
    def return_to_hub(self):
        distance = DistanceTable.get(self.location, 0)
        elapsed = timedelta(seconds=distance * 3600 / 18)
        self.odometer += distance
        self.clock += elapsed
        self.location = 0
        self.history.append(0)
        #print("Truck #", self.number, "returned to hub", distance, "miles")

    # add the package object to the manifest and change its status
    # O(1)
    def load_package(self, package):
        package.set_status(self.clock, "EN-ROUTE" + ", TRUCK " + str(self.number))
        self.manifest.append(package)
