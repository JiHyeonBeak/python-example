import random as r

buffer_num = r.randrange(3)
#answers = ["1","2","3"]
check = True
job = [{
    'name':'궁수',
    'hp':30,
    'mp':5,
    'luck':10,
    'int':3,
    'str':8
    },{
    'name':'마법사',
    'hp':15,
    'mp':30,
    'luck':13,
    'int':10,
    'str':2
    },
    {
    'name':'격투가',
    'hp':40,
    'mp':0,
    'luck':8,
    'int':3,
    'str':15
    },
    {
    'name':'상인',
    'hp':20,
    'mp':10,
    'luck':15,
    'int':8,
    'str':5
    }
    ]

print("당신의 이름은?")
name = input()

#print("당신의 직업을 맞춰보겠습니다...")
print(name,"의 직업은",job[buffer_num].get('name'),"입니다.\n")
input("진행하려면 Enter\n")

job = job[buffer_num]
user = {'name':name,'job':job}
pocket = []

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
check = True

monster_list1 = [{'name':"히드라",'hp':20,'mp':0,'item':{'1':'히드라의 눈알','2':'비늘'}},
                 {'name':"파란문어",'hp':30,'mp':15,'item':{'1':'문어 다리','2':'혈액'}},
                 {'name':"수액박쥐",'hp':20,'mp':5,'item':{'1':'혈액','2':'박쥐 이빨'}}]
buffer_num = r.randrange(2)

monster = monster_list1[buffer_num]

print(name,"은(는)",monster.get('name'),"을(를) 만났습니다.\n 1.싸운다. 2.도망친다.")
answer = input()

def roll_the_dice():
    return r.randrange(1,6)

# def getItem(m):
#     chance = roll_the_dice()
#     if user.get('job').get('luck') > 10:
#         chance += 1
#     if chance > 3:
#         m.get('item')
#     else:
#     return 

def calc_damage(userJob,dice):
    job = userJob.get('name')
    damage = 0
    if job == '마법사':
        damage = round(userJob.get('int')/3)
    else:
        damage = round(userJob.get('str')/3)
    damage = damage + round(dice*0.3)
    return damage;

def into_shop():
    print("어서오세요. 무엇을 구매하시겠습니까?")
    input("1. 체력포션\n2. 마나포션\n")

def into_town():
    print("마을에 도착했습니다. 무엇을 하시겠습니까?\n")
    answer = input("1.상점\n2.마을 사람과 대화\n3.떠난다.\n")
    check = True
    while(check):
        if answer not in ["1","2","3"]:
            answer = input("지정된 번호로 입력해주세요.\n1.상점 2.마을 사람과 대화\n3.떠난다\n")
        else:
            check = False
    if answer == "1":
        into_shop()
    elif answer == "2":
        print("이 마을 사람들은 모두가 바빠보입니다.")
    else:
        return

def battle(m,u,a):
    while u.get('job').get('hp') > 0 and m.get('hp') > 0:
        marked = roll_the_dice()
        damage = calc_damage(u.get('job'),marked)
        if a == "1":
            if marked > 3:
                print("공격에 성공합니다. \n데미지",damage)
                m['hp'] = m.get('hp') - damage
                print('나의 남은 체력 :',u.get('job').get('hp'))
                print('몬스터의 남은 체력 :',m.get('hp'),"\n")
                input("진행하려면 Enter")
            else:
                print(m.get('name'),"가(이) 공격합니다. \n데미지 2")
                u['job']['hp'] = u.get('job').get('hp') - 2
                print('나의 남은 체력 :',u.get('job').get('hp'))
                print('몬스터의 남은 체력 :',m.get('hp'),"\n")
                input("진행하려면 Enter")
        else:
            if marked > 3:
                return print("무사히 도망쳤습니다.")
            else:
                print("도망에 실패했습니다.")
                a = "1"
    if(u.get('job').get('hp') <= 0):
        print("당신은 쓰러졌습니다.\n 게임 오버")
        exit()
    elif(m.get('hp') <= 0):
        print("당신은",m.get('name'),"을(를) 처치했습니다.")
        return

while(check):
    if answer not in ["1","2"]:
        print("지정된 번호로 입력해주세요.\n1.싸운다. 2.도망친다.")
        answer = input()
    else:
        check = False
        battle(monster,user,answer)

print("다음 스테이지를 진행합니다...")
input("진행하려면 Enter\n")

print("마을이 보입니다. \n들어갑니다.")
into_town()

