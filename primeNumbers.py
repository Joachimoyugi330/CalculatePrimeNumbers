#!/usr/bin/python3

import os

# create a list 1,250
# num2 = ([x for x in range (1, 251)])

# Setting up path to the results.txt file
directory = os.getcwd()
filename = "results.txt"
filePath = os.path.join(directory, filename)

# Function to check if a number is prime

def checkPrime(num):
    count = 0
    if num<=1:
        return False
    else: 
        for i in range(1,num+1):
            if (num%i) == 0:
                count +=1
        if (count == 2):
            return True
        else:
            return False

# main function

def main():
    if os.path.exists(filePath):
        print (f"{filename} already exists")
    else:
        with open ("results.txt", "w") as file:
            for num in range(1,250):
                if checkPrime(num):
                    file.write(str(num) + "\n")

main()



