def get_user_input():
    marks_str = input("Enter marks: ")

    return int(marks_str)

def calculate_grade(marks):
    grade = ""
    if marks>=90:
        grade = "A"
    elif marks>=75 and marks<80:
        grade = "B+"
    elif marks>=70 and marks<75:
        grade = "B"
    elif marks>=50 and marks<70:
        grade = "passed"
    elif marks>=0 and marks<50:
        grade = "failed"
    else:
        print("invalid input")
    return grade

def main():
    marks = get_user_input()
    grade = calculate_grade(marks)

    print("Grade = " + grade)

if __name__=="__main__":
    main()