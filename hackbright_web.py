"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template, redirect

import hackbright

app = Flask(__name__)

@app.rout('/')
def homepage():



@app.route("/student")
def get_student():
    """Show information about a student."""
    if request.args.get('github'):
        github = request.args.get('github')

        first, last, github = hackbright.get_student_by_github(github)
        project_grade_list = hackbright.get_grades_by_github(github)


        return render_template("student_info.html",
                            github=github, 
                            first=first, 
                            last=last,
                            project_grade_list=project_grade_list)
    else:
        return redirect('/student-search')

@app.route("/student-search")
def get_student_form():
    """Show form searching for a student."""

    return render_template("student_search.html")


@app.route("/student-add")
def student_add():
    """Add a student."""

    return render_template('new_student.html')

@app.route("/student-added", methods=['POST'])
def student_added():
    """Add a student."""

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)

    return render_template('student_added.html',
                            first_name = first_name,
                            last_name=last_name,
                            github=github)

@app.route("/project")
def list_project_details():
    """Listing title, description and max grade for a project"""
    title = request.args.get('title')
    project_list = hackbright.get_project_by_title(title)
    student_grades_list = hackbright.get_grades_by_title(title)

    print(student_grades_list)
    for student in student_grades_list:
        print('student', student[0], student[1])
    return render_template("project_page.html",
        project_list=project_list,
        student_grades_list=student_grades_list)
    

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
