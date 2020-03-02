# Mark Horn / Student ID: 001069917

# Location object, each stored by LocationTable

class Location(object):

    def __init__(self, data):
        self.id = int(data[0])
        self.name = data[1]
        self.address = data[2]