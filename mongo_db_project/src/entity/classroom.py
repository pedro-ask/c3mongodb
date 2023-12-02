from bson import ObjectId

class Classroom:
    def __init__(self, name):
        self.__id = None
        self.__name = name

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        return self.__name

    def __str__(self):
        return f"\n----------\nid: {self.__id}\nname: {self.__name}\n----------"