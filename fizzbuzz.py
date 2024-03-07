#this program prints numbers 1-100, 
#writing 'fizz' if the current index is 
#divisible by 3, 'buzz' if divisible by 5, 
#and 'fizzbuzz' if divisible by both

for i in range(101):
    print(i)
    if(i % 3 == 0):
        print("Fizz")
    if(i % 5 == 0):
        print("Buzz")
    if(i % 3 and i % 5 == 0):
        print("FizzBuzz")