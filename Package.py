# Mark Horn / Student ID: 001069917

from datetime import datetime
from LocationTable import LocationTable
from enum import Enum

# This is more or less an enum to improve readability

class Status(Enum):
    NONE = -1
    AT_HUB = 0
    ON_TRUCK = 1
    DELIVERED = 2

# The package object, that will be stored in the PackageTable (HashTable)
# O(1), 1 object in, 1 out

class Package(object):

    def __init__(self, data):
        self.id = int(data[0])
        self.address = data[1]
        self.city = data[2]
        self.state = data[3]
        self.zipcode = data[4]
        self.deadline = data[5]
        self.weight = data[6]
        self.notes = data[7]
        self.times = []
        self.ontime = None
        self.status = None
        self.pickup = None
        self.linked = None
        self.delayed = None
        self.priority = None
        self.standard = None
        self.location = None
        self.destination = None
        self.bound_to_truck = None
        self.bound_to_package = None

        # Status
        if self.status is None:
            self.status = Status.NONE

        # Location
        if self.location is None:
            self.location = LocationTable.get(0).id

        # Destination
        if self.destination is None:
            self.destination = LocationTable.get(self.address).id

        # Delayed on flight
        if "Delayed on flight" in self.notes:
            self.delayed = True

        # Can only be on truck x
        if "Can only be on truck" in self.notes:
            self.bound_to_truck = 2

        # Must be delivered with
        if "Must be delivered with" in self.notes:
            self.bound_to_package = True

        # Linked packages
        if self.id in [13, 14, 15, 16, 19, 20]:
            self.linked = True

        # Wrong address listed
        if "Wrong address listed" in self.notes:
            self.destination = 19
            self.set_status(datetime.now(), "INCORRECT ADDRESS")

        # Deadline
        if "EOD" in self.deadline:
            dt = datetime.now()
            dt = dt.replace(hour=23)
            dt = dt.replace(minute=59)
            dt = dt.replace(second=59)
            dt = dt.replace(microsecond=0)
        else:
            dt = datetime.strptime(self.deadline, '%H:%M:%S')
            dt = dt.replace(day=datetime.now().day)
            dt = dt.replace(month=datetime.now().month)
            dt = dt.replace(year=datetime.now().year)
        self.deadline = dt

        # Priority
        if not self.priority:
            dt = datetime.now()
            dt = dt.replace(hour=12)
            dt = dt.replace(minute=0)
            dt = dt.replace(second=0)
            dt = dt.replace(microsecond=0)
        self.priority = self.deadline < dt

        # Standard
        if not self.priority:
            self.standard = True

        # Pickup
        if self.delayed:
            dt = datetime.now()
            dt = dt.replace(hour=9)
            dt = dt.replace(minute=5)
            dt = dt.replace(second=0)
            dt = dt.replace(microsecond=0)
            self.pickup = dt
            self.set_status(datetime.now(), "DELAYED")
        else:
            dt = datetime.now()
            dt = dt.replace(hour=0)
            dt = dt.replace(minute=0)
            dt = dt.replace(second=0)
            dt = dt.replace(microsecond=0)
            self.pickup = dt
            self.set_status(datetime.now(), "AT HUB")

        # Wrong address listed
        if "Wrong address listed" in self.notes:
            self.destination = 19
            self.set_status(datetime.now(), "INCORRECT ADDRESS")

    # adds an entry to the the collection of timestamps
    def set_status(self, time, status):
        self.times.append([time, status])

    # get the entry at a particular time
    def get_status(self, time):
        s = self.times[0][1]
        for t in self.times:
            if time > t[0]:
                s = t[1]
        return s

    # returns the final status of the package
    def get_final_status(self):
        return self.times[len(self.times)-1][1]


