from flask import Flask
from flask_restful import Resource, Api
import psycopg2
import psycopg2.extras

app = Flask(__name__)
api = Api(app)

class Groups(Resource):
    groups_list = []

    def get(self):
        self.groups_list.clear()
        self.load_groups()
        return self.groups_list

    def load_groups(self):
        try:
            conn = psycopg2.connect(host='localhost', user='postgres', password='123', dbname='institut', port = '5432')
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.execute('SELECT * FROM groups')
            for row in cursor:
                id = row['id']
                id_faculty = row['ID_FACULTY']
                name = row['title']
                self.groups_list.append({'id': id, 'id_faculty': id_faculty, 'name': name})

            conn.close()
        except Exception as e:
            print(str(e))

class Faculties(Resource):
    faculty_list = []

    def get(self):
        self.faculty_list.clear()
        self.load_faculty()
        return self.faculty_list

    def load_faculty(self):
        try:
            conn = psycopg2.connect(host='localhost', user='postgres', password='123', dbname='institut', port = '5432')
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.execute('SELECT * FROM faculties')
            for row in cursor:
                id = row['id']
                name = row['title']
                self.faculty_list.append({'id': id, 'name': name})

            conn.close()
        except Exception as e:
            print(str(e))

class Disciplines(Resource):
    disciplines_list = []

    def get(self):
        self.disciplines_list.clear()
        self.load_disciplines()
        return self.disciplines_list

    def load_disciplines(self):
        try:
            conn = psycopg2.connect(host='localhost', user='postgres', password='123', dbname='institut', port = '5432')
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.execute('SELECT * FROM disciplines')
            for row in cursor:
                id = row['id']
                name = row['name']
                self.disciplines_list.append({'id': id, 'name': name})

            conn.close()
        except Exception as e:
            print(str(e))

class Days(Resource):
    days_list = []

    def get(self):
        self.days_list.clear()
        self.load_days()
        return self.days_list

    def load_days(self):
        try:
            conn = psycopg2.connect(host='localhost', user='postgres', password='123', dbname='institut', port = '5432')
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.execute('SELECT * FROM days')
            for row in cursor:
                id = row['id']
                name = row['name']
                self.days_list.append({'id': id, 'name': name})

            conn.close()
        except Exception as e:
            print(str(e))

class Rooms(Resource):
    rooms_list = []

    def get(self):
        self.rooms_list.clear()
        self.load_rooms()
        return self.rooms_list

    def load_rooms(self):
        try:
            conn = psycopg2.connect(host='localhost', user='postgres', password='123', dbname='institut', port = '5432')
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.execute('SELECT * FROM rooms')
            for row in cursor:
                id = row['id']
                name = row['num']
                id_corpus = row['id_corpus']
                self.rooms_list.append({'id': id, 'name': name, 'id_corpus': id_corpus})

            conn.close()
        except Exception as e:
            print(str(e))

class Teachers(Resource):
    teachers_list = []

    def get(self):
        self.teachers_list.clear()
        self.load_teachers()
        return self.teachers_list

    def load_teachers(self):
        try:
            conn = psycopg2.connect(host='localhost', user='postgres', password='123', dbname='institut', port = '5432')
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.execute('SELECT * FROM teachers')
            for row in cursor:
                id = row['id']
                name = row['fio']
                self.teachers_list.append({'id': id, 'name': name})

            conn.close()
        except Exception as e:
            print(str(e))

class Times(Resource):
    times_list = []

    def get(self):
        self.times_list.clear()
        self.load_times()
        return self.times_list

    def load_times(self):
        try:
            conn = psycopg2.connect(host='localhost', user='postgres', password='123', dbname='institut', port = '5432')
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.execute('SELECT * FROM times')
            for row in cursor:
                id = row['id']
                name = row['time']
                self.times_list.append({'id': id, 'name': name})

            conn.close()
        except Exception as e:
            print(str(e))

class Schedule(Resource):
    schedule_list = []

    def get(self):
        self.schedule_list.clear()
        self.load_schedule()
        return self.schedule_list

    def load_schedule(self):
        try:
            conn = psycopg2.connect(host='localhost', user='postgres', password='123', dbname='institut', port = '5432')
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.execute('SELECT days.name AS days_name, times.time AS times_time, disciplines.name AS disciplines_name, teachers.fio AS teachers_fio, rooms.num AS rooms_num, groups.title AS groups_title FROM schedule '
                            'JOIN days ON days.id = schedule.id_day '
                            'JOIN times ON times.id = schedule.id_time '
                            'JOIN disciplines ON disciplines.id = schedule.id_discipline '
                            'JOIN teachers ON teachers.id = schedule.id_teacher '
                            'JOIN rooms ON rooms.id = schedule.id_room '
                            'JOIN groups ON groups.id = schedule.id_group')
            for row in cursor:
                days_name = row['days_name']
                times_time = row['times_time']
                disciplines_name = row['disciplines_name']
                teachers_fio = row['teachers_fio']
                rooms_num = row['rooms_num']
                groups_title = row['groups_title']
                self.schedule_list.append({'days_name': days_name, 'times_time': times_time, 'disciplines_name': disciplines_name, 'teachers_fio': teachers_fio, 'rooms_num': rooms_num, 'groups_title': groups_title,})

            conn.close()
        except Exception as e:
            print(str(e))

api.add_resource(Groups, '/groups')
api.add_resource(Faculties, '/faculties')
api.add_resource(Disciplines, '/disciplines')
api.add_resource(Days, '/days')
api.add_resource(Rooms, '/rooms')
api.add_resource(Teachers, '/teachers')
api.add_resource(Times, '/times')
api.add_resource(Schedule, '/schedule')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
