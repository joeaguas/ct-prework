#Question 1
#Write a function to print "hello_USERNAME!"
#USERNAME is the input of the function
def hello_name(user_name):
    print(f"hello_{user_name.upper()}!")


#Question 2
#Write a function that prints the odd numbers from 1-100
#return nothing
def first_odds():
    x = 1
    while x<100:
        print(x)
        x+=2


#Question 3
#Write a function to return the max number of a given list
def max_min_in_list(a_list):
    max_num = a_list[0]
    for number in a_list:
        if number > max_num:
            max_num = number
    return max_num


#Question 4
#Write a function to return if the given year is a leap year
#Leap year %4==0, %100!=0 (unless also %400==0)
#Should return boolean type
def is_leap_year(a_year):
    if a_year%4 == 0:
        if a_year%100 != 0:
            return True
        elif a_year%400 == 0:
            return True
        else:
            return False
    else:
        return False


#Question 5
#Write a function to check if all numbers in a list are consecutive
#The return type should be boolean
def is_consecutive(a_list):
    consecutive = True
    index = 1
    prev_num = a_list[0]
    while consecutive:
        if index >= len(a_list):
            break
        elif prev_num == (a_list[index] - 1):
            prev_num = a_list[index]
            index += 1
        else:
            consecutive = False
    return consecutive
           
