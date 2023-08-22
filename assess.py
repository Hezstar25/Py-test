class Students:
    def __init__(self, age, name, grade):
        self.age = age
        self.name = name
        self.grade = grade
class student_Record_System:
    def __init__(self):
        self.students = []

    def add_students(self, students):
        self.students.append(students)

    def display_all_students(self):
        for n in self.students:
            print(f'Name: {self.name} Age: {self.age} Grade: {self.grade}')
    
    def save_records(self, filename):
        with open('filename','a') as file:
            file.write(filename + '\n')
            print("Good job! Saved")

    def load_records(self, filename):
        with open('filename','r') as file:
            self.students = file.load(filename)
            print('Sucessfully Loaded')
def main():
    Record_system = student_Record_System()
    while True:
        print('STUDENTS RECORD SYSTEM')
        print('Menu\n')
        print('1.Enter student record')
        print('2. Display the record')
        print('3. Save the record')
        print('4. Load the recorded result')
        print('5. Exit')

        
        



        



    
        
        
    
    