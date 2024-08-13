# Time table generator

from models import Course, Faculty, Room, TimeTable
from config import START_TIME, END_TIME, SLOT_DURATION
import datetime
import random
def generate_timetable(courses, faculties, rooms):
    timetable = []
    start_time = datetime.strptime(START_TIME, "%H:%M")
    end_time = datetime.strptime(END_TIME, "%H:%M")

    while start_time < end_time:
        for course in courses:
            faculty = random.choice(faculties)
            room = random.choice(rooms)
            if room.capacity >= course.credits:
                timetable.append(TimeTable(
                    course_id=course.id,
                    faculty_id=faculty.id,
                    room_id=room.id,
                    start_time=start_time,
                    end_time=start_time + timedelta(minutes=SLOT_DURATION)
                ))
        start_time += timedelta(minutes=SLOT_DURATION)

    return timetable

def save_timetable(timetable):
    session.add_all(timetable)
    session.commit()