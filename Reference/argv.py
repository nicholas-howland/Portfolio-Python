#!/usr/bin/python3
## for the times you cant use argparse

n = len(sys.argv)
# get the total number of arguments
print("Total number arguments passed:", n)
# the zeroth list element is the name of the script
print("\nName of the script:", sys.argv[0])
# dump all the arguments passed to the script
print("\nArguments passed to the script:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
    if(mode=="--option"):
        # an option that accepts a command line argument
        print(sys.argv[i]+" "+sys.argv[i+1], end = " ")
