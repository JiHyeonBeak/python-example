import random as r

buffer_num = r.randrange(3)
#answers = ["1","2","3"]
check = True
job = ["궁수","상인","마법사","격투가"]

print("당신의 이름은?")
name = input()

print("당신의 직업을 맞춰보겠습니다...")
print(name,"의 직업은",job[buffer_num],"입니다.")

print("당신을 집을 떠나 모험을 합니다. 어디로 갈까요?\n번호를 입력하세요.")
print("1.동굴 2.바다 3.숲 ")
place = input()

while(check):
    if place not in ["1","2","3"]:
        print("지정된 번호로 입력해주세요.\n1.동굴 2.바다 3.숲")
        place = input()
    else:
        check = False    
        if place == "1":
            print("당신은 동굴로 향합니다.")
        elif place == "2":
            print("당신은 바다로 향합니다.")
        else:
            print("당신은 숲으로 향합니다.")