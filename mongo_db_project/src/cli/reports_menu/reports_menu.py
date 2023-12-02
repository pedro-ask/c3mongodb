from src.cli.cli_options import REPORTS_MENU
from src.services.classroom_service import ClassroomService
from src.services.student_service import StudentService

class ReportsMenu:
    def __init__(self, main_menu):
        self.__main_menu = main_menu
        self.__classroom_service = ClassroomService()
        self.__student_service = StudentService()

    def start(self):
        print(REPORTS_MENU)
        user_input = input("Selecione uma opção: ")
        options = {
            1: self.__classroom_service.read,
            2: self.__student_service.read,
            3: self.__read_students_by_classroom,
            4: self.__read_most_points_class,
            0: self.__main_menu
        }
        selected = options.get(int(user_input))
        if selected:
            selected()
            self.start()
        else:
            print("<< Selecione uma opção válida >>")
            self.start()

    def __read_students_by_classroom(self):
        print("\nTurmas disponíveis:")
        self.__classroom_service.read()
        classroom_id = input("Selecione o ID de uma turma: ")
        print("\n Alunos da turma " + str(classroom_id))
        self.__student_service.read_by_classroom_id(classroom_id)
        self.start()

    def __read_most_points_class(self):
        most_points_classroom = self.__classroom_service.get_most_points_classroom()
        score = self.__student_service.get_total_points(most_points_classroom.get('_id'))
        print(f"### Maior pontuação: {most_points_classroom.get('name')} ({score} pts) ###")
        self.start()