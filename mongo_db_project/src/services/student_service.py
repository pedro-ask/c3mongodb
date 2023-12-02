from tabulate import tabulate
from src.database.mongo_db_connection import MongoDBConnection
from src.entity.student import Student

class StudentService:
    __id_cout = None

    def __init__(self):
        try:
            collection_name = "students_collection"
            connection = MongoDBConnection()
            self.__collection = connection.get_collection(collection_name)
        except Exception as e:
            print("\n<< Erro ao conectar na coleção de estudantes >>")

    def save(self, student: Student):
        if self.__id_cout is None:
            self.__id_cout = self.count_data()
        student.set_id(self.__id_cout)
        try:
            document = {
                "_id": self.__id_cout,
                "name": student.get_name(),
                "classroom_id": int(student.get_classroom_id()),
                "points": student.get_points()
            }
            self.__collection.insert_one(document)
        except Exception as e:
            print("\n<< Erro ao salvar aluno >>")

    def read(self):
        if self.count_data() == 0:
            print("\n*** Não há alunos cadastrados ***")
            return
        try:
            search = self.__collection.find()
            ## Apresenta os dados no console em forma de tabela
            table_data = []
            for document in search:
                row = [document.get('_id'), document.get('name'), document.get('points')]
                table_data.append(row)
            table_title = ["ID", "Nome", "Pontos"]
            table = tabulate(table_data, table_title, tablefmt="pretty")
            print(table)
        except Exception as e:
            print("\n<< Erro ao obter alunos >>")

    def read_by_id(self, id):
        return self.__collection.find_one({"_id": id})

    def read_by_classroom_id(self, classroom_id):
        try:
            classroom_students = self.__collection.find({"classroom_id": int(classroom_id)})
            table_data = []
            for student in classroom_students:
                row = [student.get('_id'), student.get('name'), student.get('points')]
                table_data.append(row)
            table_title = ["ID", "Nome", "Pontos"]
            table = tabulate(table_data, table_title, tablefmt="pretty")
            print(table)
        except Exception as e:
            print("<< Erro ao obter alunos por turma >>")
            return None

    def update(self, id, name, classroom_id, points):
        try:
            result = self.__collection.update_one(
                {"_id": int(id)},
                {"$set": {
                    "classroom_id": int(classroom_id),
                    "name": name,
                    "points": points
                }}
            )
            if result.matched_count > 0:
                print("<< Atualizado com sucesso >>")
            else:
                print("Nenhum documento correspondente encontrado.")
        except Exception as e:
            print("\n<< Erro ao atualizar aluno >>")

    def delete(self, id):
        self.__collection.delete_one({"_id": id})
        print("<< Deletado com sucesso >>")

    def get_total_points(self, classroom_id=None) -> int:
        students = self.__collection.find()
        if classroom_id is not None:
            students = self.__collection.find({"classroom_id": classroom_id})
        total_points = 0
        for student in students:
            total_points += int(student['points'])
        return total_points

    def get_all_data(self):
        return self.__collection

    def count_data(self) -> int:
        try:
            return self.__collection.count_documents({})
        except Exception as e:
            print("<< Documentos não encontrados >>")
            return 0