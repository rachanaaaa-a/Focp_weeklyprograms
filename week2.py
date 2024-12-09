#question1
name=input("Hello, what is your name?")
print(f"Hello, {name}.Good to meet you!")

#question2
celsius=float(input("enter a temperature in celsius"))
fahrenheit=(9/5*celsius)+32
print(f"{celsius}C is equvalent to {fahrenheit}F")

#question3
numberofstudents=int(input("How many students?"))
size=int(input("Required group size?"))
nofgroups=numberofstudents//size
leftovers=numberofstudents%size
group_singular="group" if nofgroups==1 else"groups"
student_singular="student" if leftovers==1 else "students"
print(f"There will be {nofgroups} {group_singular} with {leftovers} {student_singular} left over.")

#question4
sweets=int(input("How many sweets are there?"))
pupils=int(input("How many pupils are there?"))
sweets_each=sweets//pupils
leftovers=sweets%pupils
print(f"each will get {sweets_each} sweets and {leftovers} sweets left over.")
                 
                           