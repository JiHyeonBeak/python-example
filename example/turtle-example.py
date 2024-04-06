import turtle as t
import random as r

# 화면 초기화
t.clearscreen()
t.setup(500, 500)

colors = ["green","skyblue","gray","pink"]

def settingTurtle():
    for i in range(1,5):
        globals()["t{}".format(i)] = t.Turtle()
        globals()["t{}".format(i)].shape("turtle")
        globals()["t{}".format(i)].turtlesize(1,1,1)
        globals()["t{}".format(i)].color(colors[-i])



def draw():
    count = 0
    flag = True
    setHead()
    while True:
        if (count%2) == 0:
          workingTurtles(flag,count)
          flag = False
        else:
            workingTurtles(flag,count)
            flag = True
        count += 1

def workingTurtles(flag,count):
    bufferNum = 0
    for i in range(1,5):
        bufferNum = i*2
        if flag == True:
            globals()["t{}".format(i)].right(20+bufferNum)
            globals()["t{}".format(i)].backward(15+count)
        else:
            globals()["t{}".format(i)].left(50+bufferNum)
            globals()["t{}".format(i)].forward(15+count)
           
def setHead():
    for j in range(1,5):
        if j > 2:
            globals()["t{}".format(j)].right(160)

# def draw():
#     flag = 0
#     count = 0
#     while True:
#         for k in range(4):
#             flag = r.randrange(5,15)
#             # 홀수번호 거북이는...
#             if k//2 == 1:
#                 if count//2 == 1:
#                     globals()["t{}".format(k)].right(flag)
#                 else:    
#                     globals()["t{}".format(k)].left(flag)
#                 globals()["t{}".format(k)].backward(15)
#             # 짝수번호 거북이는...
#             else:
#                 globals()["t{}".format(k)].right(180)
#                 if count//2 == 1:
#                     globals()["t{}".format(k)].left(flag)
#                 else:    
#                     globals()["t{}".format(k)].right(flag)
#                 globals()["t{}".format(k)].forward(15)
#             count+=1
    
settingTurtle()
draw()