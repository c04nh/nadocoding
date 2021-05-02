'''
# 숫자열 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5 + 3)
print(2 * 8)
print(3 * (3 + 1))

# 문자열 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ" * 9)

# boolean 자료형
# 참/거짓
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

# 변수
# 애완동물을 소개해주세요
animal1 = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3
print("우리집 " + animal1 + "의 이름은 " + name + "예요")
hobby = "공놀이"
# print(name + "는 ", str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name, "는 ", str(age), "살이며, ", hobby, "을 아주 좋아해요")
print(name, "는 어른일까요? ", is_adult)

# 주석
# 이렇게
# 하면
# 여려문장이
# 주석처리
# 됩니다

# 퀴즈1
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")

# 연산자
print(1 + 1)  # 2
print(3 - 1)  # 1
print(5 * 2)  # 10
print(6 / 3)  # 2

print(2 ** 3)  # 2^3 = 8
print(5 % 3)  # 나머지 구하기 2
print(10 % 3)  # 1
print(5 // 3)  # 1
print(10 // 3)  # 3

print(10 > 3)  # True
print(4 >= 7)  # False
print(10 < 3)  # False
print(5 <= 5)  # True

print(3 == 3)  # True
print(4 == 2)  # False
print(3 + 4 == 7)  # True

print(1 != 3)  # True
print(not (1 != 3))  # False

print((3 > 0) and (3 < 5))  # True
print((3 > 0) & (3 < 5))  # True

print((3 > 0) or (3 > 5))  # True
print((3 > 0) | (3 > 5))  # True

print(5 > 4 > 3)  # True
print(5 > 4 > 7)  # False

# 간단힌 수식
print(2 + 3 * 4)  # 14
print((2 + 3) * 4)  # 20
number = 2 + 3 * 4  # 14
print(number)
number = number + 2  # 16
print(number)
number += 2  # 18
print(number)
number *= 2  # 36
print(number)
number /= 2  # 18
print(number)
number -= 2  # 16
print(number)

number %= 5  # 1
print(number)

# 숫자 처리 함수
print(abs(-5))  # 5
print(pow(4, 2))  # 16
print(max(5, 12))  # 12
print(min(5, 12))  # 5
print(round(3.14))  # 3
print(round(4.99))  # 5

from math import *

print(floor(4.99))  # 내림 4
print(ceil(3.14))  # 올림 4
print(sqrt(16))  # 제곱근 4

# 랜덤 함수
from random import *

print(random())  # 0.0 ~ 1.0 임의의 값 생성
print(random() * 10)  # 0.0 ~ 10.0 임의의 값 생성
print(int(random() * 10))  # 0 ~ 10 임의의 값 생성
print(int(random() * 10))  # 0 ~ 10 임의의 값 생성
print(int(random() * 10))  # 0 ~ 10 임의의 값 생성
print(int(random() * 10) + 1)  # 1 ~ 10 임의의 값 생성
print(int(random() * 10) + 1)  # 1 ~ 10 임의의 값 생성
print(int(random() * 10) + 1)  # 1 ~ 10 임의의 값 생성
print(int(random() * 10) + 1)  # 1 ~ 10 임의의 값 생성
print(int(random() * 10) + 1)  # 1 ~ 10 임의의 값 생성
print(int(random() * 10) + 1)  # 1 ~ 10 임의의 값 생성

print(int(random() * 45) + 1)  # 1 ~ 45 임의의 값 생성
print(int(random() * 45) + 1)  # 1 ~ 45 임의의 값 생성
print(int(random() * 45) + 1)  # 1 ~ 45 임의의 값 생성
print(int(random() * 45) + 1)  # 1 ~ 45 임의의 값 생성
print(int(random() * 45) + 1)  # 1 ~ 45 임의의 값 생성
print(int(random() * 45) + 1)  # 1 ~ 45 임의의 값 생성

print(randrange(1, 46))  # 1~45 임의의 값 생성
print(randrange(1, 46))  # 1~45 임의의 값 생성
print(randrange(1, 46))  # 1~45 임의의 값 생성
print(randrange(1, 46))  # 1~45 임의의 값 생성
print(randrange(1, 46))  # 1~45 임의의 값 생성
print(randrange(1, 46))  # 1~45 임의의 값 생성

print(randint(1, 45))  # 1 ~ 45 임의의 값 생성
print(randint(1, 45))  # 1 ~ 45 임의의 값 생성
print(randint(1, 45))  # 1 ~ 45 임의의 값 생성
print(randint(1, 45))  # 1 ~ 45 임의의 값 생성
print(randint(1, 45))  # 1 ~ 45 임의의 값 생성
print(randint(1, 45))  # 1 ~ 45 임의의 값 생성

# 퀴즈2
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")

# 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

# 슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])  # 0 ~ 1
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])  # 처음부터 6직전까지
print("뒤 7자리 : " + jumin[7:])  # 7부터 끝까지
print("뒤 자리 (뒤에부터) : " + jumin[-7:])
# 맨 뒤에서 7번째부터 끝까지

# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java"))
# print(python.index("Java"))
print("hi")

print(python.count("n"))

# 문자열 포맷
# print("a" + "b")
# print("a", "b")

# 방법 1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple 은 %c로 시작해요." % "A")
# %s
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))

#  방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))

# 방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

#  탈출 문자
print("백문이 불여일견\n백견이 불여일타")
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")
print("D:\\nadocording")
print("Red Apple\rPine")
print("Redd\bApple")
print("Red\tApple")

#  퀴즈3
url = "http://naver.com"
my_str = url.replace("http://", "")  # 규칙1
my_str = my_str[:my_str.index(".")]  # 규칙2
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))

# 리스트
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

print(subway.index("조세호"))

subway.append("하하")
print(subway)

subway.insert(1, "정형돈")
print(subway)

print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)

# 사전
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(5))
print(cabinet.get(5, "사용 가능"))
print("hi")

print(3 in cabinet)  # True
print(5 in cabinet)  # False

cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목용탕 폐점
cabinet.clear()
print(cabinet)

# 튜플
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스")

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

# 세트 (집합)
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = {"유재석", "박명수"}

# 교집합(java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 잊었어요
java.remove("김태호")
print(java)

# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

# 퀴즈4
users = range(1, 21)  # 1부터 20까지 숫자 생성
users = list(users)

print(users)
shuffle(users)
print(users)

winners = sample(users, 4)

print(" --  당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" --  축하합니다 -- ")

# if
weather = input("오늘 날씨는 어때요? ")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요.")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp or temp < 30:
    print("괜찮은 날씨예요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")

# for
for waiting_no in range(1, 6):
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

# while
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")
# customer = "아이언맨"
# index = 1;
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1}회".format(customer, index))
customer = "토르"
person = "Unknown"
while person != customer:
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")

# continue와 break
absent = [2, 5]  # 결석
no_book = [7]  # 책을 깜빡했음
for student in range(1, 11):  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와.".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

# 한 줄 for
students = [1, 2, 3, 4, 5]
print(students)
students = [i + 100 for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

# 퀴즈3
cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[0] {0}번째 손님 (소요시간 : {1}분".format(i, time))
        cnt += 1
    else:
        print("[0] {0}번째 손님 (소요시간 : {1}분".format(i, time))
print("총 탑승 승객 : {0}분".format(cnt))


# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")


def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money


def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance


def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission


balance = 0
balance = deposit(balance, 1000)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))


# 기본값
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
          .format(name, age, main_lang))


profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")


def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
          .format(name, age, main_lang))


profile("유재석")
profile("김태호")


# 키워드값
def profile(name, age, main_lang):
    print(name, age, main_lang)


profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")


# 가변인자
def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")

# 지역변수와 전역변수
gun = 10


def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
checkpoint(2)
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))


# 퀴즈6
def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21


height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
'''


# 클래스
# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# name = "마린"  # 유닛의 이름
# hp = 40  # 유닛의 체력
# damage = 5  # 유닛의 공격력
#
# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))
#
# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
#
# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))
#
# # 탱크2 새로 추가
# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35
#
# print("{} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))
#
#
# # 공격 함수
# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))
#
#
# attack(name, "1시", damage)  # 마린 공격 명령
# attack(tank_name, "1시", tank_damage)  # 탱크 공격 명령
# attack(tank2_name, "1시", tank2_damage)  # 탱크2 공격 명령


# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name  # 멤버변수 name 에 전달값 name 저장
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
#
#
# marine1 = Unit("마린", 40, 5)  # 마린1 생성. 전달값으로 name, hp, damage 를 전달
# marine2 = Unit("마린", 40, 5)  # 마린2 생성
# tank = Unit("탱크", 150, 35)  # 탱크 생성

# __init__
# class Unit:
#     def __init__(self, name, hp, damage): # 3개의 전달값
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
#
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)
#
# marine3 = Unit("마린", 40) # 전달값 3개 중 2개만 넘김

# 멤버변수
# class Unit:
#     def __init__(self, name, hp, damage): # 3개의 전달값
#         self.name = name # 멤버변수 name
#         self.hp = hp # 멤버변수 hp
#         self.damage = damage # 멤버변수 damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


# 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)  # 체력 80, 공격력 5
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))  # 멤버변수 접근
# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.cloaking = True  # 빼앗은 레이스만을 위한 특별한 멤버변수 정의
#
# if wraith2.cloaking == True:  # 클로킹 상태라면?
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))


# 에러
# if wraith1.cloaking == True: # 우리가 만든 레이스 클로킹 여부
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith1.name))

# 메소드
# class AttackUnit:  # 공격 유닛
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#
#     def attack(self, location):  # 공격 방향
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
#               .format(self.name, location, self.damage))  # 공간이 좁아서 2줄에 걸쳐 출력
#
#     def damaged(self, damage):  # damage 만큼 유닛 피해
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))  # 데미지 정보 출력
#         self.hp -= damage  # 유닛의 체력에서 전달받은 damage 만큼 감소
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))  # 남은 체력 출력
#         if self.hp <= 0:  # 남은 체력이 0 이하이면?
#             print("{0} : 파괴되었습니다.".format(self.name))  # 유닛 파괴 처리
#
#
# # 파이어뱃 : 공격 유닛, 화염방사기.
# firebat1 = AttackUnit("파이어뱃", 50, 16)  # 체력 50, 공격력 16
# firebat1.attack("5시")  # 5시 방향으로 공격 명령
#
# # 공격 2번 받는다고 가정
# firebat1.damaged(25)  # 남은 체력 25
# firebat1.damaged(25)  # 남은 채력 0


# 상속
# 일반 유닛
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#
#
# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage
#
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
#               .format(self.name, location, self.damage))
#
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))
#
#
# # 파이어뱃 : 공격 유닛, 화염방사기.
# firebat1 = AttackUnit("파이어뱃", 50, 16)  # 체력 50, 공격력 16
# firebat1.attack("5시")  # 5시 방향으로 공격 명령
#
# # 공격 2번 받는다고 가정
# firebat1.damaged(25)  # 남은 체력 25
# firebat1.damaged(25)  # 남은 채력 0

# 다중상속
# 일반 유닛
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#
#
# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage
#
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
#               .format(self.name, location, self.damage))
#
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))
#
#
# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):  # 공중 이동 속도
#         self.flying_speed = flying_speed
#
#     def fly(self, name, location):  # 유닛 이름, 이동 방향
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
#               .format(name, location, self.flying_speed))
#
#
# # 공중 공격 유닛
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):  # 이름, 체력, 공격력, 공중 이동 속도
#         AttackUnit.__init__(self, name, hp, damage)  # 이름, 체력, 공격력
#         Flyable.__init__(self, flying_speed)  # 공중 이동 속도
#
#
# # 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)  # 이름, 체력, 공격력, 공중 이동 속도
# valkyrie.fly(valkyrie.name, "3시")  # 3시 방향으로 발키리를 이동


# 메소드 오버라이딩
# 일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" \
#               .format(self.name, location, self.speed))
#
#
# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage
#
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
#               .format(self.name, location, self.damage))
#
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))
#
#
# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
#               .format(name, location, self.flying_speed))
#
#
# # 공중 공격 유닛
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)
#         Flyable.__init__(self, flying_speed)
#
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)
#
#
# # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)  # 지상 speed 10
#
# # 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
#
# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")  # 오버라이딩된 move() 호출

#
# # pass
# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" \
#               .format(self.name, location, self.speed))
#
#
# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage
#
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
#               .format(self.name, location, self.damage))
#
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))
#
#
# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
#               .format(name, location, self.flying_speed))
#
#
# # 공중 공격 유닛
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)
#         Flyable.__init__(self, flying_speed)
#
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)
#
#
# # 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass
#
#
# # 서플라이 디폿 : 건물, 1개 건물 = 8 유닛
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")  # 체력 500, 생성 위치 7시
#
#
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")
#
#
# def game_over():
#     pass
#
#
# game_start()
# game_over()


# super
class Unit:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flyable 생성자")


# class FlyableUnit(Unit, Flyable):
class FlyableUnit(Flyable, Unit):  # 순서 변경
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)  # Unit 클래스 생성자 호출
        Flyable.__init__(self)  # Flyable 클래스 생성자 호출


# 드랍쉽
dropship = FlyableUnit()