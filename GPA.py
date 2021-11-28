import re
#Required to determine the weight of a course for GPA
Grades = {'A+':4.30,'A':4.00,'A-':3.70,'B+':3.30,'B':3.00,'B-':2.70,'C+':2.30,
         'C':2.00,'C-':1.70,'D+':1.30,'D':1.00,'D-':0.70,'F':0.00, '-':0.00} 

#Class Schedule is intended to be used to store the course list and GPA
class Schedule:
    courseList= []
    GPA = 0.0
    def __init__(self) -> None: #Default constructor
        courseList =[]
        GPA = 0.0

    def addCourse(self,course):#Being able to add a course that does not have the same name as another course
        inCourses = False
        for i in self.courseList:#iterate through to ensure the course does not exist
            if course.courseName.strip() == i.courseName.strip():
                inCourses=True
                break
        if inCourses:#if the course does already exist, we tell them they cannot add that course
            print("Sorry, you already have a course under that name.")
        else:#update course list otherwise
            self.courseList.append(course)
            print("Course has been added!")
    
    def removeCourse(self):#Being able to remove a course that exists within the course list
        if(len(self.courseList)==0):
            print("Sorry, you have no courses in your schedule currently.")
        else:
            for count,i in enumerate(self.courseList):#Prints out the course list 
                print(f"{count+1}. {i.courseName}")
            choice = input("Which course would you like to remove?\n")
            while(choice.isdigit==False or int(choice) not in range(1,len(self.courseList)+1)):#prompt until user selects a valid number
                choice = input("Please enter a valid number\n")
            del self.courseList[int(choice) - 1]
            print("Remove successful!")

    def wipeSchedule(self):#Clears out the course list 
        self.courseList.clear()
        print("Schedule is now clear!")

    def displaySchedule(self):#Displays the courses, along with all the other information and GPA information
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

#Class Course is intended to be created and stored into Schedule
class Course:
    courseName = ""
    gradeLetter = ""
    credit = 0.0
    def __init__(self) -> None:#Constructor to populate an instance of a course
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

    def displayCourse(self):#Simply displays the course information
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