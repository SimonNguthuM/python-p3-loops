#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count > 0:
        print(count)
        count -=1
    print("Happy New Year!")    

def square_integers(int_list):
    int_list = [num ** 2 for num in int_list]
    return int_list

def fizzbuzz():
    count = 1
    while count <= 100:
        if count % 3 == 0 and count % 5 == 0:
            print("FizzBuzz")
        elif count % 3 == 0:
            print("Fizz")
        elif count % 5 == 0:
            print("Buzz")
        else:
            print(count)        
        count +=1
    