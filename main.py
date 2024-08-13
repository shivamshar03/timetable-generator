# Main program

import input
import timetable
import output

def main():
    faculties, num_working_days, classes, labs, classrooms = input.get_input()
    timetable, day_wise_timetable = timetable.generate_timetable(faculties, num_working_days, classes, labs, classrooms)
    output.generate_pdf(timetable, day_wise_timetable)

if __name__ == "__main__":
    main()