import turtle as t

# 화면 초기화
t.clearscreen()
t.setup(700, 700)

def draw():
    t.shape("turtle")
    t.color("skyblue")
    for i in range(100):
        t.left(3)
        t.forward(5)
        tPos = t.pos()
        t.write(tPos)
#        if tPos == "196.22,151.33":
#            for j in range(5):
#                t.forward(j)
#        else:
#            continue

draw()