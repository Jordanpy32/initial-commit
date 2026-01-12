"""
This program manages grades for a classe

1. Ask a user how many students there are in the class.
2. For each students, Ask:
  - Name of student
  - his note (betwen 0 and 20)
3. Stores names and notes in two separate lists.
4. Displays the list of students with their notes, in the form:
    Alice : 15
    Bob : 12
    ...etc
5. Calculate and display
  - Average note of the classe
  - Student with the best note and his note
  - Student with the worst note and his note
6. Display how many students have a note above Average
7. Display how many students have failed (note < 10)
8. Ask a user if he wants add a new student in the end and update the lists.

"""
#declaration of my two lists. students and notes
my_list_students = []
my_list_note = []

number_students = 0 #declaration of a variable number of students.

number_students = int(input("How many students there are in the class: ")) #store the value in the variable

#loop for to recover the name of each students and his note
for n in range(number_students):
    student_name = input("Enter the name of student, name: ") #store the name of each student in a variable
    student_note = int(input("Enter his note, note: ")) #store the note of student in a variable
    
    my_list_students.append(student_name)
    my_list_note.append(student_note)

#display my two lists
print("my_list_students: ", my_list_students)
print("my_list_note: ", my_list_note)





