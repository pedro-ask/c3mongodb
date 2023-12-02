from tabulate import tabulate
from src.database.mongo_db_connection import MongoDBConnection
from src.entity.classroom import Classroom
from src.services.student_service import StudentService

from bson import ObjectId

class ClassroomService:
    __id_cout = None

    def __init__(self):
        self.__student_service = StudentService()
        try:
            collection_name = "classrooms_collection"
            self.__connection = MongoDBConnection()
            self.__collection = self.__connection.get_collection(collection_name)
        except Exception as e:
            print("<< Erro ao se conectar na coleção de turmas >>")

    def save(self, classroom: Classroom):
        if self.__id_cout is None:
            self.__id_cout = self.count_data()
        classroom.set_id(self.__id_cout)
        try:
            document = {
                "_id": self.__id_cout,
                "name": classroom.get_name()
            }
            self.__collection.insert_one(document)
        except Exception as e:
            print("<< Erro ao inserir turma >>")

    def read(self):
        if self.count_data() == 0:
            print("*** Não há alunos cadastrados ***>>")
            return
        try:
            search = self.__collection.find()
            ## Apresenta os dados no console em forma de tabela
            table_data = []
            for document in search:
                id = document.get('_id')
                row = [id, document.get('name'), self.__student_service.get_total_points(id)]
                table_data.append(row)
            table_title = ["ID", "Nome da turma", "Pontuação total"]
            table = tabulate(table_data, table_title, tablefmt="pretty")
            print(table)
        except Exception as e:
            print("<< Erro ao obter turmas >>" + str(e))

    def read_by_id(self, id):
        return self.__collection.find_one({"_id": str(id)})

    def update(self, id, name):
        try:
            result = self.__collection.update_one(
                {"_id": int(id)},
                {"$set": {"name": name}}
            )
            if result.matched_count > 0:
                print("<< Atualizado com sucesso >>")
            else:
                print("Nenhum documento correspondente encontrado.")
        except Exception as e:
            print("<< Erro ao atualizar turma >>" + str(e))

    def delete(self, id):
        try:
            self.__collection.delete_one({"_id": str(id)})
        except Exception as e:
            print("<< Erro ao deletar turma >>")

    def get_most_points_classroom(self, return_type=None):
        try:
            highest_score = 0
            most_points_classroom = None
            for classroom in self.__collection.find({}):
                points = self.__student_service.get_total_points(classroom.get('_id'))
                if points > highest_score:
                    most_points_classroom = classroom
                    highest_score = points
            if return_type == "formated":
                return f"{most_points_classroom.get('name')} ({highest_score} pts)"
            return most_points_classroom
        except Exception as e:
            return 0

    def get_all_data(self):
        return self.__collection

    def count_data(self):
        try:
            return self.__collection.count_documents({})
        except Exception as e:
            print("<< Documentos não encontrados >>")
            return 0;

