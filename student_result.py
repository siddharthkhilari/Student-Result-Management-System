def get_student_data():
    name= input("Enter student name:")
    rollnumber= int (input("Enter Roll number:"))

    maths= int(input( " Enter maths marks:"))
    physics= int ( input ("Enter physics marks:"))
    chemistry= int (input("Enter chemistry marks:"))

    return name,rollnumber,maths,physics,chemistry

def percentage_calculate(maths,physics,chemistry):
    total= maths+physics+chemistry

    percentage= total/ 3

    return total,percentage

def grade_calculate(percentage):
    if percentage >=80 :
        grade="A"
    elif percentage >=60:
        grade="B"
    elif percentage >=40:
        grade="C"
    else:
        grade="fail"
    return grade

def display_result(name,rollnumber,total,percentage,grade):
    print("\n---student result---")
    print("Student Name:",name)
    print("Roll Number:",rollnumber)
    print("Total Marks:",total,"/300")
    print("Percentage:", round(percentage, 2))
    print("Grade",grade)
    


name, rollnumber, maths, physics, chemistry = get_student_data()

total, percentage = percentage_calculate(maths, physics, chemistry)

grade = grade_calculate(percentage)

display_result(name, rollnumber, total, percentage, grade)