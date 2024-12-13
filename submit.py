import csv
import os

def submit(self):
    """
    This is used to calculate the GPA, checks for name entered, checks
    if invalid grades are entered, and inputs information into data.csv
    entered into the GUI
    :param self:
    :return:
    """

    # Dictionary to store the value of each letter grade into GPA format
    grade_points = {
        'A+': 4.0,
        'A': 4.0,
        'A-': 3.7,
        'B+': 3.3,
        'B': 3.0,
        'B-': 2.7,
        'C+': 2.3,
        'C': 2.0,
        'C-': 1.7,
        'D+': 1.3,
        'D': 1.0,
        'F': 0.0,
        'NA': None
    }

    # Stores name, math, science, history, and english into variables
    name = self.input_name.get().strip()
    math = self.input_math.get().strip() or 'NA'
    science = self.input_science.get().strip() or 'NA'
    history = self.input_history.get().strip() or 'NA'
    english = self.input_english.get().strip() or 'NA'

    # List to store grades
    grades = [math, science, history, english]

    # Checks if name was entered
    if not name:
        self.mes_label.config(text='Enter in a name')
        return

    # Checks if any grade input is within grade_points
    invalid_grades = [grade for grade in grades if grade not in grade_points]
    if invalid_grades:
        self.mes_label.config(text='Invalid grade entered')
        return

    # Makes sure that the input of grades is being added to total_points
    # Quantity adds how many classes were entered
    total_points = 0
    quantity = 0
    for grade in grades:
        if grade in grade_points and grade_points[grade] is not None:
            total_points += grade_points[grade]
            quantity += 1

    # gpa holds the total of gpa points divided by the quantity of classes
    # Then updates the GUI of new GPA
    if quantity > 0:
        gpa = total_points / quantity
        gpa = f'GPA: {gpa:.2f}'
        self.gpa_label.config(text=gpa)
        self.mes_label.config(text='')
    # if there isn't anything entered into any classes, GPA will show up as NA on GUI
    else:
        gpa = 'GPA: NA'
        self.gpa_label.config(text=gpa)
        self.mes_label.config(text='')

    # Checks to see if data.csv is in OS path
    file_name = 'data.csv'
    file_exists = os.path.isfile(file_name)

    # data.csv is opened if existing
    # Then appends information entered into the GUI to data.csv
    # If data.csv does not exist, then data.csv is created to write new rows in
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Name', 'Math', 'Science', 'History', 'English', 'Overall GPA'])
        writer.writerow([name, math, science, history, english, gpa])
