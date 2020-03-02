# Mark Horn / Student ID: 001069917

from datetime import datetime
from TruckTable import TruckTable
from PackageTable import PackageTable
from Dijkstra import truck1, truck2

print('********************************************** WGUPS Simulation ***********************************************')
print("Truck 1 completed route in", round(truck1.odometer, 2), "miles")
print("Truck 2 completed route in", round(truck2.odometer, 2), "miles")
print("Full Package Route completed in", round(truck1.odometer + truck2.odometer, 2), "miles")

print('********************************************* WGUPS Command Line **********************************************')
print('0: exit the program')
print('1: lookup truck route(s)')
print('2: lookup package by id')
print('3: lookup packages by time')
print('***************************************************************************************************************')

# This code block is the input for the user interface in the terminal, as seen in the WGUPS Command Line above.
# Continue until user breaks the loop

while 1:
    user_input = input("Enter command [0-3]:")

    # exit application
    # O(1)
    if user_input == "0":
        print("Goodbye")
        break

    # display the route for each truck and all packages
    # O(N)
    elif user_input == "1":
        for truck in TruckTable.all():
            line = "[Truck " + str(truck.number) + "] "
            for stop in truck.history:
                line = line + "->" + str(stop)
            print(line + " (" + str(round(truck.odometer, 2)) + " miles)")

    # display the status of one individual package, by ID
    # O(1)
    elif user_input == "2":
        while 1:
            id_input = input("Enter Package ID:")
            try:
                id = int(id_input)
                if id in PackageTable.keys:
                    package = PackageTable.get(id)
                    print("[ID]", package.id,
                          "[ADDRESS]", package.address, package.city, package.state, package.zipcode,
                          "[DUE]", package.deadline,
                          "[STATUS]", package.get_final_status())
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid")

    # display the status of all packages at a given time
    # O(N)
    elif user_input == "3":
        while 1:
            time_input = input("Enter Time (hh:mm):")
            try:
                time_input = datetime.strptime(time_input, '%H:%M').time()
                time = datetime.now().replace(hour=time_input.hour, minute=time_input.minute, second=0, microsecond=0)
                packages = PackageTable.all()
                packages = sorted(packages, key=lambda x: x.id)
                for package in packages:
                    status_at_time = package.get_status(time)
                    print("[ID]", package.id,
                          "[ADDRESS]", package.address, package.city, package.state, package.zipcode,
                          "[DUE]", package.deadline,
                          "[STATUS]", status_at_time)
                break
            except ValueError:
                print("Invalid")
    else:
        print("Invalid command")

