import sys

def greet_users(usernames):
        for i in range(0,len(usernames)):
            print("Hello, %s" %usernames[i].capitalize())

args = sys.argv[1:]
greet_users(args)