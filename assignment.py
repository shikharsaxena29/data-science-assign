#1.  Explain with an example each when to use a for loop and a while loop.
#  ans For loop is used when the number of iterations is already known. While loop is used when the number
# of iterations is Unknown
# for loop example;
l1=[1,2,3,4,5]
for i in l1:
    print(i)
    i=i+1
    
# while loop example;
i=10
while i>0:
    print("pwskills")
    i=i-1


# Q2. Write a python program to print the sum and product of the first 10 natural numbers using for and while loop.
# for loop
summ=0
product=1
for i in range(1,11): # o is included and 11 is not included 
    summ=summ+i
    product=product*i
    i=i+1
print("sum of first 10 natural numbers using for loop is",summ)  
print("product of first 10 natural numbers using for loop is",product)


# while loop
num=10
sum2=0
prod=1
while num>0:
    sum2=sum2+num
    prod=prod*num
    num=num-1
print("sum of first 10 natural numbers using while loop is ",sum2)  
print("product of first 10 natural numbers using while loop is",prod)


# Q3. Create a python program to compute the electricity bill for a household.
units = int(input("Enter the total units consumed: "))

bill = 0

if units <= 100:
    bill = units * 4.5


elif units <= 200:
    bill = 100 * 4.5  
    bill += (units - 100) * 6  


elif units <= 300:
    bill = 100 * 4.5  
    bill += 100 * 6 
    bill += (units - 200) * 10  


else:
    bill = 100 * 4.5 
    bill += 100 * 6 
    bill += 100 * 10  
    bill += (units - 300) * 20  

print("Your electricity bill is: Rs.", bill)


#Q4. Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each
# number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print
# that list.

l1=[]
l2=[]
for i in range(1,101):
    q=i*i*i
    l1.append(q)
    if q%4==0 or q%5==0:
       l2.append(q)
    print(l2)    


#Q5 Write a program to filter count vowels in the below-given string. string = "I want to become a data scientist"

vowels=0
string="I want to become a data scientist"
for i in string:
    if i=="a":
       vowel=vowel+1
    elif i=="e":
        vowel=vowel+1 
    elif i=="i": 
        vowel=vowel+1  
    elif i=="o":
        vowel=vowel+1
    elif i=="u":  
        vowel=vowel+1    


