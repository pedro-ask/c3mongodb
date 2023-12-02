import time

from src.cli.cli_options import ENTITY_MENU
from src.cli.cli_options import UPDATE_STUDENT_MENU
from src.cli.config import refresh_application
from src.services.classroom_service import ClassroomService
from src.services.student_service import StudentService
from src.entity.classroom import Classroom
from src.entity.student import Student

class EntityMenu:
    def __init__(self, main_menu):
        self.__back_to_main_menu = main_menu
        self.__classroom_service = ClassroomService()
        self.__student_service = StudentService()

    def start(self, operation):
        classroom_options = {
            "insert": self.__insert_classroom,
            "update": self.__update_classroom,
            "delete": self.__delete_classroom
        }
        student_options = {
            "insert": self.__insert_student,
            "update": self.__update_student,
            "delete": self.__delete_student,
        }
        print(ENTITY_MENU)
        user_input = input("Seleciona uma entidade: ")

        if user_input == "1":
            classroom_options[operation]()
        elif user_input == "2":
            student_options[operation]()
        elif user_input == "0":
            self.__back_to_main_menu()
        else:
            print("<< Opção inválida >>")
            self.start(operation)

    def __insert_classroom(self):
        classrom_name = input("Nome da turma: ")
        new_classroom = Classroom(classrom_name)
        self.__classroom_service.save(new_classroom)
        print("\n<< Turma salva com sucesso >>")
        refresh_application()
        self.__back_to_main_menu()

    def __insert_student(self):
        if self.__classroom_service.count_data() == 0:
            print("***Não há turmas para cadastrar alunos***")
            refresh_application()
            self.__back_to_main_menu()
        student_name = input("informe o nome do(a) aluno(a): ")
        self.__classroom_service.read()
        student_classroom = input("Informe o número da turma do aluno: ")
        student_points = input("Informe a quantidade de pontos: ")
        new_student = Student(student_classroom, student_name, student_points)
        self.__student_service.save(new_student)
        print("\n<< Aluno salvo com sucesso >>")
        refresh_application()
        self.__back_to_main_menu()

    def __update_classroom(self):
        self.__classroom_service.read()
        try:
            selected_id = input("Selecione o ID da turma que deseja atualizar: ")
            name = input("Novo nome da turma: ")
            self.__classroom_service.update(selected_id, name)
        except Exception as e:
            print("Selecione um ID válido" + str(e))
        refresh_application()
        self.__back_to_main_menu()

    def __update_student(self):
        self.__student_service.read()
        try:
            selected_id = input("Selecione o ID do aluno que deseja atualizar: ")
            student_to_update = self.__student_service.read_by_id(int(selected_id))
            if student_to_update is not None:
                name = student_to_update.get('name')
                classroom_id = student_to_update.get('classroom_id')
                points = student_to_update.get('points')
            print(UPDATE_STUDENT_MENU)
            try:
                selected_option = input("Selecione uma propriedade para alterar: ")
                if selected_option == "1":
                    name = input("Novo nome do aluno: ")
                if selected_option == "2":
                    classroom_id = input("Novo ID da turma: ")
                if selected_option == "3":
                    points = input("Nova pontuação: ")
            except Exception as e:
                print("<< Selecione uma ID válido >>")
                self.__update_student()
            self.__student_service.update(selected_id, name, int(classroom_id), points)
        except Exception as e:
            print("<< Erro ao atualizar aluno >>" + str(e))
        refresh_application()
        self.__back_to_main_menu()

    def __delete_classroom(self):
        print("Excluindo Turma")
        refresh_application()
        self.__back_to_main_menu()

    def __delete_student(self):
        print("Excluindo Aluno")
        refresh_application()
        self.__back_to_main_menu()