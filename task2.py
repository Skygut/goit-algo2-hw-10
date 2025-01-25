# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()  # Предмети, які викладач буде викладати


def create_schedule(subjects, teachers):
    # Копія множини предметів, які потрібно покрити
    remaining_subjects = set(subjects)
    schedule = []

    while remaining_subjects:
        # Знайти викладача, який може викладати найбільше предметів із залишку
        best_teacher = None
        best_coverage = set()

        for teacher in teachers:
            # Визначити, які предмети з залишку може викладати викладач
            can_cover = teacher.can_teach_subjects & remaining_subjects
            if len(can_cover) > len(best_coverage) or (
                len(can_cover) == len(best_coverage)
                and teacher.age < (best_teacher.age if best_teacher else float("inf"))
            ):
                best_teacher = teacher
                best_coverage = can_cover

        if not best_teacher or not best_coverage:
            # Якщо немає викладача, який може покрити залишкові предмети
            return None

        # Призначити предмети викладачу
        best_teacher.assigned_subjects.update(best_coverage)
        schedule.append(best_teacher)
        # Оновити залишкові предмети
        remaining_subjects -= best_coverage

    return schedule


if __name__ == "__main__":
    # Множина предметів
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}

    # Створення списку викладачів
    teachers = [
        Teacher(
            "Олександр",
            "Іваненко",
            45,
            "o.ivanenko@example.com",
            {"Математика", "Фізика"},
        ),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher(
            "Сергій",
            "Коваленко",
            50,
            "s.kovalenko@example.com",
            {"Інформатика", "Математика"},
        ),
        Teacher(
            "Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}
        ),
        Teacher(
            "Дмитро",
            "Бондаренко",
            35,
            "d.bondarenko@example.com",
            {"Фізика", "Інформатика"},
        ),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"}),
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}"
            )
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
