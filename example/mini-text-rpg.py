import random as r

buffer_num = r.randrange(3)
#answers = ["1","2","3"]
check = True
job = [{
    'name':'궁수',
    'hp':30,
    'mp':5
    },{
    'name':'마법사',
    'hp':15,
    'mp':30
    },
    {
    'name':'격투가',
    'hp':40,
    'mp':0
    },
    {
    'name':'상인',
    'hp':20,
    'mp':10
    }
    ]

print("당신의 이름은?")
name = input()

print("당신의 직업을 맞춰보겠습니다...")
print(name,"의 직업은",job[buffer_num].get('name'),"입니다.")

job = job[buffer_num]
user = {'name':name,'job':job}

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
            place = "동굴"
            print("당신은 동굴로 향합니다.")
        elif place == "2":
            place = "바다"
            print("당신은 바다로 향합니다.")
        else:
            place = "숲"
            print("당신은 숲으로 향합니다.")

print(user.get('name'),"은(는)",place,"(으)로 갑니다.")

monster1 = {'name':"히드라",'hp':20,'mp':0}
monster2 = {'name':"파란문어",'hp':30,'mp':15}
monster3 = {'name':"수액박쥐",'hp':20,'mp':5}

print(name,"은(는)",monster1.get('name'),"을(를) 만났습니다.\n 1.싸운다. 2.도망친다.")

        