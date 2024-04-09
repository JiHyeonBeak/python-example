import turtle as t

# 화면 초기화
t.clearscreen()
t.setup(500, 500)

colors = ["green","skyblue","gray","pink"]

# 거북이 객체 생성
def settingTurtle():
    for i in range(1,5):
        globals()["t{}".format(i)] = t.Turtle()
        globals()["t{}".format(i)].shape("turtle")
        globals()["t{}".format(i)].turtlesize(1,1,1)
        globals()["t{}".format(i)].color(colors[-i])

# draw 상위 함수
def draw():
    count = 0
    flag = True
    setHead()
    while True:
        # 짝수번 실행시에는 flag변수를 넘겨 거북이들이 오른쪽으로 가게한다.
        if (count%2) == 0:
          workingTurtles(flag,count)
          flag = False
        else:
            workingTurtles(flag,count)
            flag = True
        count += 1

# 실제 거북이들이 무늬를 그리는 함수
def workingTurtles(flag,count):
    bufferNum = 0
    for i in range(1,5):
        # bufferNum 각 거북이들과 거리를 두기 위한 변수
        bufferNum = i*2
        if flag == True:
            globals()["t{}".format(i)].right(20+bufferNum)
            globals()["t{}".format(i)].backward(15+count)
        else:
            globals()["t{}".format(i)].left(50+bufferNum)
            globals()["t{}".format(i)].forward(15+count)


# 거북이 머리 방향 조정 함수
# 1번, 2번 거북이는 반대방향에서 시작합니다.         
def setHead():
    for j in range(1,5):
        if j > 2:
            globals()["t{}".format(j)].right(160)

# 실행부    
settingTurtle()
draw()