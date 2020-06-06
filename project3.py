import codecs
import random


class Load:
    """Класс загрузки данных"""
    data = []
    classrooms = {}
    teachers = {}

    @classmethod
    def load_data(cls, file_name):
        """Метод для загрузки данных из файла"""
        with codecs.open(file_name, 'r', 'utf-8') as file:
            count = len(file.readlines())
        with codecs.open(file_name, 'r', 'utf-8') as file:
            for _ in range(count):
                line = file.readline()
                line = line.replace('\n', '')
                info = line.split(';')

                if info[1] not in Load.classrooms:
                    classroom = Classroom(info[1])
                    Load.classrooms[info[1]] = classroom

                if info[2] not in Load.teachers:
                    teacher = Teacher(info[2])
                    Load.teachers[info[2]] = teacher

                lesson = Lesson(name=info[0], type_of_lessons=info[3],
                                classroom=Load.classrooms[info[1]],
                                teacher=Load.teachers[info[2]],
                                count_per_week=float(info[4]))
                lesson.classroom.lessons.append(lesson)
                lesson.teacher.lessons.append(lesson)
                Load.data.append(lesson)


class Classroom:
    def __init__(self, number):
        self.number = number
        self.lessons = []

    def __str__(self):
        return self.number

    def __repr__(self):
        return self.__str__()


class Teacher:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Lesson:
    def __init__(self, name, type_of_lessons, classroom, teacher,
                 count_per_week):
        self.name = name
        self.classroom = classroom
        self.type_of_lessons = type_of_lessons
        self.teacher = teacher
        self.count_per_week = count_per_week

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name + ' ' + self.type_of_lessons


class TimeTable:
    time = ['9:00', '10:50', '12:40', '14:30', '16:20', '18:10']

    def __init__(self, classes, group_number):
        self.lst_classes = TimeTable.make_timetable(classes)
        self.group_number = group_number
        self.table = TimeTable.draw_table(self.lst_classes, self.group_number)

    def __str__(self):
        return self.table

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def make_timetable(lst_classes):
        timetable = [[' ' for _ in range(6)] for _ in range(6)]
        indexes = [(i, j) for i in range(6) for j in range(6)]
        classes = []
        for lesson in lst_classes:
            if int(lesson.count_per_week) == lesson.count_per_week and \
                    lesson.count_per_week > 1:
                for _ in range(int(lesson.count_per_week)):
                    classes.append(lesson)
            elif int(lesson.count_per_week) != lesson.count_per_week and \
                    lesson.count_per_week > 1:
                for _ in range(int(lesson.count_per_week)):
                    classes.append((lesson, 'чет'))
                classes.append((lesson, 'нечет'))
            else:
                classes.append(lesson)
        for lesson in classes:
            num = random.randint(0, len(indexes) - 1)
            timetable[indexes[num][0]][indexes[num][1]] = lesson
            indexes.remove(indexes[num])
        return timetable


    @staticmethod
    def draw_table(lst_classes, group_number):
        timetable = '+' + '-' * 107 + '+\n' + '|{:^107}|\n'.format(
            group_number) + '+' + '-' * 107 + '+\n' + \
                    '|{:^5}|{:^16}|{:^16}|{:^16}|{:^16}|{:^16}|{:^16}|\n'. \
                        format('TIME', 'MONDAY', 'TUESDAY', 'WEDNESDAY',
                               'THURSDAY', 'FRIDAY', 'SATURDAY') + '+' + \
                    '-' * 107 + '+\n'
        for i in range(6):
            line = lst_classes[i]
            for j in range(6):
                if j == 4:
                    timetable += '|{:^5}|{:<16}|{:<16}|{:<16}|{:<16}|{:<16}|{:' \
                                 '<16}|\n'.format('', TimeTable.check(line[0], ''),
                                                  TimeTable.check(line[1], ''),
                                                  TimeTable.check(line[2], ''),
                                                  TimeTable.check(line[3], ''),
                                                  TimeTable.check(line[4], ''),
                                                  TimeTable.check(line[5], ''))
                elif j == 2:
                    timetable += '|{:^5}|{:^16}|{:^16}|{:^16}|{:^16}|{:^16}|{:' \
                                 '^16}|\n'.format(
                        TimeTable.time[0],
                        TimeTable.check(line[0], 'classroom'),
                        TimeTable.check(line[1], 'classroom'),
                        TimeTable.check(line[2], 'classroom'),
                        TimeTable.check(line[3], 'classroom'),
                        TimeTable.check(line[4], 'classroom'),
                        TimeTable.check(line[5], 'classroom'))
                    TimeTable.time.remove(TimeTable.time[0])
                elif j == 5:
                    timetable += '+' + '-' * 107 + '+\n'
                elif j == 0:
                    timetable += '|{:^5}|{:>16}|{:>16}|{:>16}|{:>16}|{:>16}|{:' \
                                 '>16}|\n'.format(
                        '', TimeTable.check(line[0], 'type_of_lessons'),
                        TimeTable.check(line[1], 'type_of_lessons'),
                        TimeTable.check(line[2], 'type_of_lessons'),
                        TimeTable.check(line[3], 'type_of_lessons'),
                        TimeTable.check(line[4], 'type_of_lessons'),
                        TimeTable.check(line[5], 'type_of_lessons'))
                elif j == 1:
                    timetable += '|{:^5}|{:^16}|{:^16}|{:^16}|{:^16}|{:^16}|{:' \
                                 '^16}|\n'.format(
                        '', TimeTable.check(line[0], 'name'),
                        TimeTable.check(line[1], 'name'),
                        TimeTable.check(line[2], 'name'),
                        TimeTable.check(line[3], 'name'),
                        TimeTable.check(line[4], 'name'),
                        TimeTable.check(line[5], 'name'))
                elif j == 3:
                    timetable += '|{:^5}|{:^16}|{:^16}|{:^16}|{:^16}|{:^16}|{:' \
                                 '^16}|\n'.format(
                        '', TimeTable.check(line[0], 'teacher'),
                        TimeTable.check(line[1], 'teacher'),
                        TimeTable.check(line[2], 'teacher'),
                        TimeTable.check(line[3], 'teacher'),
                        TimeTable.check(line[4], 'teacher'),
                        TimeTable.check(line[5], 'teacher'))
        return timetable

    @staticmethod
    def check(param, attridute):
        if isinstance(param, tuple):
            if attridute == '':
                return param[1]
            param = param[0]
        try:
            if attridute == 'teacher':
                n = param.teacher
            elif attridute == 'name':
                n = param.name
            elif attridute == 'type_of_lessons':
                n = param.type_of_lessons
            elif attridute == 'classroom':
                n = param.classroom
            else:
                return ''
        except AttributeError:
            return ' '
        else:
            return str(n)


