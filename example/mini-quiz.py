QUESTION = ["책상 위 시계의 색상은?",
            "시계 옆 책의 이름은?",
            "시계의 시침이 있는 숫자는?"]

ANSWER1 = ["파랑","셜록 홈즈의 귀환","3"]
ANSWER2 = ["blue","return of Sherlock Holmes","three"]

score = 0
UANSER = []

for i in range(3):
    print(QUESTION[i])
    ans = input()
    UANSER.append(ans)
    if ans == ANSWER1[i] or ans == ANSWER2[i]:
        score += 1
        print("정답")
    else:
        print("오답")

print("결과 :",score)
print("-- 당신의 답 --")
for j in range(len(UANSER)):
    print(UANSER[j])