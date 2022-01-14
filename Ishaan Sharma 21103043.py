#answer 1  
number_1=input("Give number 1:")
number_2=input("Give number 2:")
number_3=input("Give number 3:")

number_1=int(number_1)
number_2=int(number_2)
number_3=int(number_3)
#average
avg=(number_1+number_2+number_3)/3
print(avg)



#answer 2 
gross_income=input("Please enter gross income:")
gross_income=float(gross_income)

standard_deduction=10000
dependents=input("Enter the number of dependents:")
dependents=int(dependents)
#there is a $3000 deduction for each dependents
dependent_deduction=3000
#tax rate=20%
taxable_income=gross_income-standard_deduction-(dependent_deduction*dependents)
print("taxable income:")
print(taxable_income)
tax=(taxable_income*20)/100
print("tax:")
print(tax)


#answer 3
name=input("Enter name:")
sid=input("Enter student Id:")
gender=input("Enter gender:")
course_name=input("Enter your course name:")
cgpa=input("Enter cgpa:")
sid=int(sid)
cgpa=float(cgpa)
#our list now name as student_info
data=["Name", "SID","Gender","Cgpa"]
print(data)
student_info=[name,sid,gender,course_name,cgpa]
print(student_info)



#answer 4

student_1marks=int(input("Enter student 1 marks:"))
student_2marks=int(input("Enter student 2 marks:"))
student_3marks=int(input("Enter student 3 marks:"))
student_4marks=int(input("Enter student 4 marks:"))
student_5marks=int(input("Enter student 5 marks:"))

my_list=[student_1marks,student_2marks,student_3marks,student_4marks, student_5marks]
print("List")
print(my_list)
print("Sorted List (decreasing order):")
my_list.sort(reverse=True)
print(my_list)



#answer 5
my_list=["Red","Green","White","Black","Pink","Yellow"]
#(a) part
print('(a)')
print(my_list)
#remove 4th term thatbis black
my_list.remove('Black')
print(my_list)

my_list=["Red","Green","White","Black","Pink","Yellow"]
#(b)part
print('(b)')
print(my_list)
#replace black and pink with purple
#to replace nth term we write {my_list[n-1]='new value'}
my_list[3]='Purple'
my_list[4]='Purple'
print(my_list)
