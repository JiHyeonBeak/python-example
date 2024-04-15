import random as r

buffer_num = r.randrange(3)
job = ["궁수","상인","마법사","격투가"]

print("당신의 이름은?")
name = input()

print("당신의 직업을 맞춰보겠습니다...")
print(name,"의 직업은",job[buffer_num],"입니다.")
