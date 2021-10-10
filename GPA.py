import re
Grades = {'A+':4.30,'A':4.00,'A-':3.70,'B+':3.30,'B':3.00,'B-':2.70,'C+':2.30,
         'C':2.00,'C-':1.70,'D+':1.30,'D':1.00,'D-':0.70,'F':0.00, '-':0.00} 

class Schedule:
    courseList= []
    GPA = 0.0
    def __init__(self) -> None:
        courseList =[]
        GPA = 0.0

    def addCourse(self,course):
        inCourses = False
        for i in self.courseList:
            if course.courseName.strip() == i.courseName.strip():
                inCourses=True
                break
        if inCourses:
            print("Sorry, you already have a course under that name.")
        else:
            self.courseList.append(course)
            print("Course has been added!")
    
    def removeCourse(self):
        if(len(self.courseList)==0):
            print("Sorry, you have no courses in your schedule currently.")
        else:
            for count,i in enumerate(self.courseList):
                print(f"{count+1}. {i.courseName}")
            choice = input("Which course would you like to remove?\n")
            while(choice.isdigit==False or int(choice) not in range(1,len(self.courseList)+1)):
                choice = input("Please enter a valid number\n")
            del self.courseList[int(choice) - 1]
            print("Remove successful!")
    def wipeSchedule(self):
        self.courseList.clear()
        print("Schedule is now clear!")
    def displaySchedule(self):
        print('\n\nCourse\t Grade \tCredits\t Grade Points')
        points = [0.0,0.0]
        for i in self.courseList:
            gradePoint = Grades.get(i.gradeLetter)*i.credit
            points[1] += gradePoint
            points[0] += i.credit
            print(f"{i.courseName}    {i.gradeLetter} \t   {i.credit} \t    {gradePoint}")
        if(len(self.courseList)!=0):
            self.GPA = points[1]/points[0]
        print('Total', '{:>16.1f}{:>10.1f}'.format(points[0], points[1]))  
        print('\n\tSemester GPA =' , "{:.2f}".format(points[1]) , '/' , "{:.2f}".format(points[0]) , '=', round(self.GPA,3))


class Course:
    courseName = ""
    gradeLetter = ""
    credit = 0.0
    def __init__(self) -> None:
        course = input("Please enter in a course name(Ex. ENGL 101)\n")
        gradeLetter = input("Please enter in a grade letter for your course.(Ex. A+,B-,etc.)\n").upper()
        while(gradeLetter not in Grades):
            gradeLetter = input("You did not enter in a correct letter grade. Please try again\n").upper()
        cred = input("Please enter in a valid credit number(Ex. 4, 3, 2, etc.)\n")
        while(cred.isdigit==False):
            cred = input("Please enter in a valid credit number(Ex. 4, 3, 2, etc.)\n")

        self.courseName=course.replace(" ", "").upper()
        self.gradeLetter=gradeLetter
        self.credit=round(float(cred),2)
    def displayCourse(self):
        print(f"Course: {self.courseName} \nGrade: {self.gradeLetter} \nCredits: {self.credit}")


def main():
    print("Welcome to my schedule and GPA calculator! Here, you can add courses to your schedule, which I think is pretty cool!")
    run = True
    schedule = Schedule()
    while run:
        print("What would you like to do today?\n1. View Schedule\n2. Add Course\n3. Remove Course\n4. Clear Schedule\n5. Quit")
        choice = re.sub("\D", "", input())
        if(choice=="1"):
            schedule.displaySchedule()
        elif(choice=="2"):
            schedule.addCourse(Course())
        elif(choice=="3"):
            schedule.removeCourse()
        elif(choice=="4"):
            schedule.wipeSchedule()
        elif(choice=="5"):
            run = False
            print("Thank you for using this!")
        else:
            print("Sorry, you gotta enter a valid choice!\n")

main()