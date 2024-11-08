#Question 1: Arithmetic and Assignment Operator
#TODO 1
x = +3
print(x)

#TODO 2
y= (x*2)
print(y)

#TODO 3
y = int(x/y)
print ("result")

#___________________________________________________________________________________
#Question 2: Comparison and Logical Operators
#TODO 4
print(7>4)

#TODO 5
print(7==4 %2)

#TODO 6
print(2<=7)

#TODO 7
print(7>=4)

#TODO 8
print(50!=60)   #(!=) not equal function
print(50>=60 or 40<=50)     #second method to get the answer

#TODO 9
print(40<=50)

#________________________________________________________________________________
#Question 3: Conditional Statement

#TODO 10
score=int(input("user to enter test score: "))

if 90 <= score <= 100:
    grade ="Bachelor"
elif 80<= score <=89:
    grade ="Distinction"
elif 70<= score <=79:
    grade ="Passed"
elif 60<= score <=69:
    grade ="Average"
elif 69>= score >=0:
    grade = "Failed"
else:
    grade = "Invalid score."

#TODO 11
print(f"The grade for the score {score} is {grade}")

#________________________________________________________________________________
#Question 4 :Combining Operators and Conditionals

#TODO 12
num1= int(input("user1 input two numbers: "))
num2= int(input("user2 input two numbers: "))

#TODO 13
operation= input("Please enter input operation like (+,-,*,/)")

#TODO 14
if operation == "+" :
    result = num1 + num2
elif operation == "-" :
    result = num1 - num2
elif operation == "*" :
    result = num1 * num2
elif operation == "/" :
   if num2 ==  0:        #Not divide by zero as the question illustrates 
        print(num1/num2)
        result = num1 / num2
else:
    result = "ERROR"

#TODO 15
print(f"The result is: {result}")