import sys
print("\033[1m" + "         Program to check system status" + "\033[0m")
a= input("please input the value in binary\n>>>")#take user input as string
print("The total length of the digit is",len(a))
coun = str(a).count('1')# count 1s in user input
print("There are",coun, "1s  in provided value")
if (coun % 2) == 0: # even checker
    print("system functioning normally")
else:
    print("System Error Detected")


a = 1
ag = input("Type 1 to continue or any key to end: ")

if int(ag) == a:  # Continue if 1 is pressed
    print(" This is the Message filterer")
else:
    sys.exit()  # exit the program

msg = input("Write your message here:\n>>> ")

# List of words to check for
vulgar_words = ["hate", "shit"]# arrays of string

# Check if any vulgar word is in the message
if any(word in msg.lower() for word in vulgar_words):
    print("failed to send, don't use vulgar words")
else:
    print("message send sucessfully")

