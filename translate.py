from sys import argv
from time import localtime, strftime
from pymongo import Connection

connection = Connection()
db = connection.actions

#pass help for action names
#pass an action for times

def showActions():
        actions = db["action"].find({"action":{"$ne":None}},{"action":1})
        for item in actions:
                print item['action']

def showTimes(action_name):
        entries = returnEntries(action_name)
        for item in entries['time']:
                print strftime('%Y-%m-%d %H:%M:%S', localtime(item))

def returnEntries(action_name):
        entries = db["action"].find_one({"action":action_name})
        return entries


if __name__ == "__main__":
        if argv[1] == "help":
                showActions()
        else:
                showTimes(argv[1])
