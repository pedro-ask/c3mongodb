import time
from src.services.classroom_service import ClassroomService
from src.services.student_service import StudentService
from src.cli.reports_menu.reports_menu import ReportsMenu
from src.cli.entity_menu.entity_menu import EntityMenu
from src.cli.cli_options import MAIN_MENU

class MainMenu:
    def __init__(self):
        self.student_service = StudentService()
        self.classroom_service = ClassroomService()
        self.total_classrooms = self.classroom_service.count_data()
        self.total_students = self.student_service.count_data()
        self.highest_score = self.classroom_service.get_most_points_classroom("formated")
        self.total_points = self.student_service.get_total_points()

        self.created_by = "Ari Guimarães da Silva Pinto, Gabriel Fischer Braga, João Victor Trarbach dos Santos e Pedro Arthur de Souza Kuster"
        self.teacher = "Prof. M.Sc. Howard Roatti"
        self.subject = "Banco de Dados"
        self.semester = "2023/2"

    def display_splash_screen(self):
        splash_screen = f"""
        ########################################################
        #                   SISTEMA DE PONTUAÇÃO                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - TURMAS: {self.total_classrooms}
        #      2 - ALUNOS: {self.total_students}
        #      3 - TURMA COM MAIOR PONTUAÇÃO: {self.highest_score}
        #      4 - PONTUAÇÃO GERAL: {self.total_points}
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.teacher}
        #
        #  DISCIPLINA: {self.subject}
        #              {self.semester}
        ########################################################
        """
        print(f"{splash_screen}")

    def start(self):
        self.display_splash_screen()
        print(MAIN_MENU)
        user_input = input("Selecione uma opção: ")
        self.process_input(user_input)

    def process_input(self, user_input):
        entity_menu = EntityMenu(self.start)
        reports_menu = ReportsMenu(self.start)

        options = {
            "1": reports_menu.start,
            "2": entity_menu.start,
            "3": entity_menu.start,
            "4": entity_menu.start,
            "5": exit
        }

        selected_option = options.get(user_input)

        if selected_option:
            if user_input == "2" or user_input == "3" or user_input == "4":
                selected_option("insert" if user_input == "2" else "update" if user_input == "3" else "delete")
            else:
                selected_option()
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(1)
            self.start()
