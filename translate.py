from sys import argv
from time import localtime, strftime

times = [1399402955.584515]

def printTimes(times):
    for item in times:
        print strftime('%Y-%m-%d %H:%M:%S', localtime(item))

if __name__ == "__main__":
    printTimes(times)
