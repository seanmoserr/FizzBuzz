#this program prints numbers 1-100, 
#writing 'fizz' if the current index is 
#divisible by 3, 'buzz' if divisible by 5, 
#and 'fizzbuzz' if divisible by both

##old program
##for i in range(101):
#    print(i)
#    if(i % 3 == 0):
#        print("Fizz")
#    if(i % 5 == 0):
#        print("Buzz")
#    if(i % 3 and i % 5 == 0):
#        print("FizzBuzz")


##best branch back on main

for i in range(101):
    if(i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif(i % 3 == 0):
       print("Fizz")
    elif(i % 5 == 0):
        print("Buzz")
    else:
        print(i)