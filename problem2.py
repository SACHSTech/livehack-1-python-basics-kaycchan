'''
-------------------------------------------------------------------------------
Name:		problem2.py
Purpose:	determine the number of chicken pieces per student, and number of chicken pieces for Mr. Fabroa

Author:	Chan.K

Created:	07/12/2020
------------------------------------------------------------------------------
'''

# input number of chicken pieces
number_of_chicken = float(input("Enter number of total chicken pieces: "))

# input number of students
number_of_students = float(input("Enter number of students: "))

# number of mr. fabroas
mr_fabroa = 1

# determine the amount of chicken pieces per student
chicken_per_student = number_of_chicken//number_of_students

# determine the amount of chicken for mr.fabroa
fabroa_chicken = number_of_chicken%number_of_students

# final statement of chicken per student and mr.fabroa
print ("If there are " + str(number_of_students) + " students in the class, and " + str(number_of_chicken) + " piece(s) of chicken, each student will get " + str(chicken_per_student) + " piece(s) of chicken, and Mr.Fabroa will get " + str(fabroa_chicken) + " piece(s) of chicken.")