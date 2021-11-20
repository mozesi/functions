try:
    fileHandle = open('mbox.txt')
except:
    print("file can not be opened")
    quit()

for line in fileHandle:
        if line.startswith('From'):
            continue
        print(line.strip())
        print("hello word")


def addNumbers():
    firstNumber = input("fist number")
    ssecondNumber = input("second number")

    print(firstNumber + ssecondNumber)