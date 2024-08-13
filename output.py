# Output generation logic

import pdfkit

def generate_pdf(timetable, day_wise_timetable):
    # Create a PDF file
    pdf_file = "timetable.pdf"

    # Generate faculty timetables
    faculty_pdf = ""
    for faculty, faculty_timetable in timetable.items():
        faculty_pdf += f"<h2>{faculty} Timetable</h2>"
        for i, day in enumerate(faculty_timetable):
            faculty_pdf += f"<h3>Day {i+1}</h3>"
            faculty_pdf += "<table>"
            for slot in day:
                faculty_pdf += f"<tr><td>{slot['time']}</td><td>{slot['subject']}</td><td>{slot['classroom']}</td></tr>"
            faculty_pdf += "</table>"

    # Generate class timetables
    class_pdf = ""
    for class_name, class_timetable in timetable.items():
        if class_name.startswith("Class"):
            class_pdf += f"<h2>{class_name} Timetable</h2>"
            for i, day in enumerate(class_timetable):
                class_pdf += f"<h3>Day {i+1}</h3>"
                class_pdf += "<table>"
                for slot in day:
                    class_pdf += f"<tr><td>{slot['time']}</td><td>{slot['subject']}</td><td>{slot['classroom']}</td></tr>"
            class_pdf += "</table>"

    # Generate lab timetables
    lab_pdf = ""
    for lab_name, lab_timetable in timetable.items():
        if lab_name.startswith("Lab"):
            lab_pdf += f"<h2>{lab_name} Timetable</h2>"
            for i, day in enumerate(lab_timetable):
                lab_pdf += f"<h3>Day {i+1}</h3>"
                lab_pdf += "<table>"
                for slot in day:
                    lab_pdf += f"<tr><td>{slot['time']}</td><td>{slot['lab']}</td><td>{slot['classroom']}</td></tr>"
                lab_pdf += "</table>"

    # Generate day-wise timetable
    day_wise_pdf = ""
    for day, slots in day_wise_timetable.items():
        day_wise_pdf += f"<h2>{day} Timetable</h2>"
        day_wise_pdf += "<table>"
        for slot in slots:
            day_wise_pdf += f"<tr><td>{slot['time']}</td><td>Faculties: {', '.join(slot['faculties'])}</td><td>Classes: {', '.join(slot['classes'])}</td><td>Labs: {', '.join(slot['labs'])}</td></tr>"
        day_wise_pdf += "</table>"

    # Combine all PDFs
    pdf_content = "<html><body>"
    pdf_content += faculty_pdf
    pdf_content += class_pdf
    pdf_content += lab_pdf
    pdf_content += day_wise_pdf
    pdf_content += "</body></html>"

    # Generate PDF file
    pdfkit.from_string(pdf_content, pdf_file)

    print(f"Timetable generated successfully! Check {pdf_file} for the output.")