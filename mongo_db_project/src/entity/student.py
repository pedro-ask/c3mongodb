from bson import ObjectId

class Student:
    def __init__(self, classroom_id, name, points):
        self.__id = None
        self.__classroom_id = classroom_id
        self.__name = name
        self.__points = points

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.id = id

    def get_classroom_id(self):
        return self.__classroom_id

    def set_classroom_id(self, classroom_id):
        self.__classroom_id = classroom_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_points(self):
        return self.__points

    def set_points(self, points):
        self.__points = points

    def __str__(self):
        return f"----------\nid: {self.__id}\n classroom id: {self.__classroom_id}\n name: {self.__name}\n points: {self.__points}----------"