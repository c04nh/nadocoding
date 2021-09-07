import datetime
import random
# 1. 핸드폰 요금이 62421원 나왔다. 100원 미만은 절사한다고 한다. 62400원 청구. 59827원일 경우, 실제 청구 금액은?
print("===1번===")
bill = 59827

def cell_phone_bill(bill):
    bill = int(bill / 100)
    return bill*100

answer = cell_phone_bill(bill)
print(answer)
print(bill//100*100)
print(bill - bill%100)

# 2. 평가계획은 100점 만점에 10점 단위로 점수를 줄 수 있다. 채점한 결과 93점이 나왔다. 90점 부여. 56점은 몇 점 부여?
print("===2번===")
score = 56

def ratind_plan(score):
    score = round(score, -1)
    return score

answer = ratind_plan(score)

print(answer)
print(round(score / 10) * 10)

# 3. 로또 복권 자동 생성기를 만든다면?
# (로또복권: 1~45 사이의 번호 중 랜덤으로 6개 뽑기)
print("===3번===")
def lotto():
    lotto = []
    while len(lotto) < 6:
        num = random.randint(1, 45)
        if num not in lotto:
            lotto.append(num)
    lotto.sort()
    return lotto

print(lotto())

print(random.sample(range(1, 46), 6))

# 4. 1~9 숫자로 중복되지 않은 숫자 세자리를 뽑는 방법은?(185:O, 212:X)
print("===4번===")
def three_digit_number():
    num = []
    str_num = ''
    while len(num) < 3:
        randnum = random.randint(1, 9)
        if randnum not in num:  # 새로운 수가 중복이 아니면,
            num.append(randnum)  # 리스트에 추가
    for i in num:
        str_num = str_num + str(i)
    return int(str_num)

print(three_digit_number())

list_r = random.sample(range(1, 9+1), 3)
print("".join(str(n)for n in list_r))
print("".join(map(str, list_r)))

# 5. 내가 태어난 날로부터 며칠이 지났는지?
print("===5번===")
birthday = datetime.datetime(2004, 9, 13, 16, 35)

def birth_over_days(birthday):
    now = datetime.datetime.now()
    days = now - birthday
    return days

answer = birth_over_days(birthday)
print(answer)

# 6. 올해 크리스마스까지 며칠이 남았는지?
print("===6번===")
def until_christmas():
    christmas = datetime.datetime(2021, 12, 25)
    now = datetime.datetime.now()
    days = christmas - now
    return days

print(until_christmas())

# 7. 내 생일이 며칠 남았는지?
birthday = datetime.datetime(2021, 9, 13)
now = datetime.datetime.now()
print("===7번===")

def until_birthday(birthday):
    now = datetime.datetime.now()
    if now < birthday:
        days = birthday - now
    else:
        birthday = datetime.datetime(birthday.year+1, birthday.month, birthday.day)
        days = birthday - now
    return days

answer = until_birthday(birthday)
print(answer)

if birthday < now:
    birthday = birthday.replace(year=birthday.year+1)

print(birthday - now)

# 8. 랜덤하게 번호로 자리를 배치하는 방법은?
# 제적(전출, 자퇴) 인원이 있다면?
print("===8번===")
# 마지막 번호가 몇 번인지 묻자
last_number = input("마지막 번호는 ? : ")
# 1부터 마지막 번호까지 리스트 만들자
list_class = list(range(1, int(last_number) + 1))
# 무한 반복
while True:
#   나간 친구 번호 묻자
    exclude_number = input("뺄 번호는?(그냥 enter치면 끝내자) : ")
#   그냥 enter면 반복 끝내자
    if exclude_number == "":
        break
#   리스트에서 빼자
    list_class.remove(int(exclude_number))
    print(list_class)

# 랜덤으로 섞자

# 출력하자





