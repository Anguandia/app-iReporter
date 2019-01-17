import datetime


class RedFlag:
    count = 0
    def __init__(self, id, location, createdBy, title):
        RedFlag.count += 1
        self.id = id
        self.location = location
        self.createdBy = createdBy
        self.title = title
