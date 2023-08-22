import pickle

class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

class Student_Record_System:
    def __init__(self):
        self.student = []

    def add_student(self, student):
        self.student.append(student)
        print('Added Successfully!')

    def display_all_students(self):
       if not self.student:
           print('Unknown')
       else:
           print('Student Records:')
           for i, student in enumerate(self.student, start=1):
               print(f"Student {i}:")
               print(f"Name: {student.name}")
               print(f"Age: {student.age}")
               print(f"Grade: {student.grade}")
               print()

    def save_records(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.student, file)
            print("Saved")
        
    def load_records(self):
        try:
            with open('filename', 'rb'):
                self.student = pickle.load(file=1)
                print("Loading")
        except FileNotFoundError:
            print("File Not Found")
        except pickle.UnpicklingError:
            print("Error")

def main():
    Record_System = Student_Record_System()

    while True:
        print('STUDENTS\'  RECORDS')
        print('Menu\n')
        print('1. Enter student\'s name')
        print('2. Display Studentd Record')
        print('3. Save the Record')
        print('4. Load the Recorded info')
        print('5. Exit')


        filly = input('Enter your details')

        if filly == '1':
            name = input('Enter your name')
            age = int(input('Enter your age'))
            grade = float(input('What is your grade'))
            student = Students(name, age, grade)
            Record_System.add_student(student)

        elif filly == '2':
            Record_System.display_all_students()

        elif filly == '3':
            Record_System.save_records
            filename = input('Enter file name to save')
        elif filly == '4':
            filename = input('Load Records')
            Record_System.load_records(filename)
        
        elif filly == '5':
            print('Done Deal')
            break

        else:

            print('Strange Input')

if __name__ == '__main__':
    main()