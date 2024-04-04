import turtle as t

# 화면 초기화
t.clearscreen()
t.setup(700, 700)

colors = ["red","green","skyblue","gray"]

def settingTurtle():
    for i in range(4):
        globals()["t{}".format(i)] = t.Turtle()
        globals()["t{}".format(i)].shape("turtle")
        globals()["t{}".format(i)].turtlesize(1,1,1)
        globals()["t{}".format(i)].color(colors[i])

def draw():
    for j in range(117):
        for k in range(4):
            if k//2 == 1:
                globals()["t{}".format(k)].left(3)
                globals()["t{}".format(k)].forward(10)
            else:
                globals()["t{}".format(k)].right(3)
                globals()["t{}".format(k)].forward(10)
        

settingTurtle()
draw()