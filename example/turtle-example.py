import turtle as t

# 화면 초기화
t.clearscreen()
t.setup(700, 700)

def draw():
    t.shape("turtle")
    t.color("skyblue")
    for j in range(100):
        t.left(j)
        t.forward(j)

for i in range(3):
    draw()