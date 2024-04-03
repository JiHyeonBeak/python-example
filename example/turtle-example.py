import turtle as t

# 화면 초기화
t.clearscreen()
t.setup(700, 700)

colors = ["red","green","skyblue","gray"]

def settingTurtle():
    for i in range(1,4):
        globals()["t{}".format(i)] = t.Turtle()
        globals()["t{}".format(i)].shape("turtle")
        globals()["t{}".format(i)].turtlesize(2,2,2)
        globals()["t{}".format(i)].color(colors[i])

def draw():
    for j in range(150):
        t1.left(3)
        t1.forward(10)

settingTurtle()
draw()