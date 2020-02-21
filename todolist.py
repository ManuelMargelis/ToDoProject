# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 02:02:19 2020

@author: User
"""

import pickle
import os
os.system("clr")

#creating the class "variable type" "task" which is a struct more or less that has the type of task, name of task, date and shit like that
class TaskClass:
  def __init__(self, Type, Task, DateAdd, Deadline, MainGoal, NumberLeft, NumPerDay):
    self.Type = Type
    self.Task = Task
    self.DateAdd = DateAdd
    self.Deadline = Deadline
    self.MainGoal = MainGoal
    self.NumberLeft = NumberLeft
    self.NumPerDay = NumPerDay


listOfTasks = []
TaskDict = dict()
f=open("TaskTextFile.txt", "r")
contents = f.readlines()
try:
    for x in contents:
        line = x.split(" -- ")
        TaskType = line[0]
        TaskName = line[1]
        TaskDateAdd = line[2]
        TaskDeadline = line[3]
        TaskMainGoal = line[4]
        TaskNumberLeft = line[5]
        TaskNumPerDay = line[6]
        listOfTasks.append(line[1])
        TaskDict[TaskName] = TaskClass(TaskType,TaskName,TaskDateAdd,TaskDeadline,TaskMainGoal,TaskNumberLeft,TaskNumPerDay)
except:
    print("somthings askew in the text file probobly an empty line")
#Function to save the data so your gonna get all the data that ur passing thru and somehow save it to the fucken text file
#def SaveTask(Type, Task, DateAdd, Deadline, MainGoal, NumberLeft, NumPerDay):



#creating a lists of "task class type structs" that will allow us to continously add this new variable type to a ever changing list
def ReadSaveFile():
  global listOfTasks
  global TaskDict
  listOfTasks.clear()
  f=open("TaskTextFile.txt", "r")
  contents = f.readlines()
  try:
      for x in contents:
          line = x.split(" -- ")
          TaskType = line[0]
          TaskName = line[1]
          TaskDateAdd = line[2]
          TaskDeadline = line[3]
          TaskMainGoal = line[4]
          TaskNumberLeft = line[5]
          TaskNumPerDay = line[6]
          listOfTasks.append(line[1])
          TaskDict[TaskName] = TaskClass(TaskType,TaskName,TaskDateAdd,TaskDeadline,TaskMainGoal,TaskNumberLeft,TaskNumPerDay)
  except:
    print("your data is messed up some1 enterd some janky stuff as a task")

  f.close()



def AddTask(TaskType,TaskName,TaskDateAdd,TaskDeadline,TaskMainGoal,TaskNumberLeft,TaskNumPerDay):
    gap = " -- "
    save = str(TaskType) + gap + str(TaskName)+ gap +str(TaskDateAdd)+ gap +str(TaskDeadline)+ gap +str(TaskMainGoal)+ gap +str(TaskNumberLeft)+ gap + str(TaskNumPerDay) + "\n"

    CheckIfThere = []
    ItsDoubled = 0
    f=open("TaskTextFile.txt", "r")
    contents = f.readlines()

    try:
     for x in contents:
      line = x.split(" -- ")
      names = line[1]
      CheckIfThere.append(line[1])
    except:
        print("your data is messed up some1 enterd some janky stuff as a task")


    print(ItsDoubled)
    print("read the shit and put all the names in a list heres the list \n")
    print(CheckIfThere)


    if TaskName in CheckIfThere:
        ItsDoubled = 1

    print(ItsDoubled)

    if ItsDoubled == 0:
        f = open("TaskTextFile.txt", "a")
        f.write(save)
        f.close()


def _print_layout(object):
  print(object.Type)
  print(" ")
  print(object.Task)
  print(" ")
  print(object.DateAdd)
  print(" ")
  print(object.Deadline)
  print(" ")
  print(object.MainGoal)
  print(" ")
  print(object.NumberLeft)
  print(" ")
  print(object.NumPerDay)


def print_customer(nameoftask):
    try:
        _print_layout(TaskDict[nameoftask])
    except:
        print("that object doesnt exists lol")


print_customer("write script for mtg deck")
ReadSaveFile()
print_customer("learn 500 Greek words")
AddTask("complete task","Do mtrn lab 2 prework","2020, 2, 22","2020, 2, 27","Uni 2020 T1","0","0")
ReadSaveFile()
print_customer("learn 500 Greek words")
print_customer("nerd")
print_customer("Do mtrn lab 2 prework")
