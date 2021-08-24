#  퀴즈1-1
id_number = "040913"
# noinspection PyTypeChecker
print(id_number[0:2] + "\n" + id_number[2:6] + "\n" + str(int(id_number[:2]) * int(id_number[2:6])))

#  퀴즈1-2
phone_number = "02-887-0589"
print(phone_number[0:] + "\n" + phone_number[:phone_number.index("-")] + "\n" + phone_number[-4:])

#  학교 실습
phone_number = "02-1234-5678"
phone_number2 = "032-9876-4321"
x = phone_number2.index("-")  # index()함수는 없으면 valueError, find()함수는 없으면 -1
print(phone_number2[0:x])
print(phone_number2[-4:])

#  전화번호 입력시 -가 있든 없는 찰떡같이 알아먹기
phone_number1 = "010-1234-5678"
phone_number2 = "01098765432"
phone_number3 = "010 1111 2222"

phone_number = phone_number3
result = phone_number.replace("-", "").replace(" ", "")
print(result)

# 퀴즈 2-1
student_number = "2313"
if student_number[1] == "1" or student_number[1] == "2":
    print(student_number[1] + "반 뉴미디어소프트웨어과")
elif student_number[1] == "3" or student_number[1] == "4":
    print(student_number[1] + "반 뉴미디어웹솔루션과")
elif student_number[1] == "5" or student_number[1] == "6":
    print(student_number[1] + "반 뉴미디어디자인과")
else:
    print("잘못 입력했습니다")

# 학교 실습
student_number = "2313"
number = student_number[1]
number = int(number)
majors = ["뉴미디어소프트웨어과", "뉴미디어웹솔루션과", "뉴미디어디자인과"]
if 1 <= number <= 6:
    print(f"{number}반 {majors[(number - 1) // 2]}")
else:
    print("잘못입력했습니다.")


# 퀴즈 2-2
def get_major(student_number):
    major = "잘못입력했습니다"
    grade = student_number[0]
    if student_number[1] == "1" or student_number[1] == "2":
        major = "뉴미디어소프트웨어과"
    elif student_number[1] == "3" or student_number[1] == "4":
        major = "뉴미디어웹솔루션과"
    elif student_number[1] == "5" or student_number[1] == "6":
        major = "뉴미디어디자인과"
    return grade, major


grade, major = (get_major("2313"))
print(major, grade)


# 퀴즈 2-3
def average(*number):
    sum_number = 0
    for num in number:
        sum_number += num
    return sum_number / len(number)


print(average(10, 20, 30))


# 학교실습
def average(*numbers):
    sum_value = 0
    count = 0
    for number in numbers:
        sum_value += number
        count += 1
    return sum_value / count


print(average(4, 23))


# 퀴즈 2-4
def get_bmi(height, weight):
    bmi = round(weight / ((height / 100) * (height / 100)), 1)
    if bmi < 18.5:
        result = "저체중"
    elif 18.5 <= bmi < 23:
        result = "보통"
    elif 23 <= bmi < 25:
        result = "과체중"
    else:
        result = "비만"
    return result


bmi = get_bmi(176, 69)
print(bmi)


# 학교 실습
def get_bmi(height, weight):
    height /= 100
    return round(weight / height ** 2, 1)


bmi = get_bmi(176, 69)

if bmi < 18.5:
    print("저체중")
elif bmi < 23:
    print("정상")
elif bmi < 25:
    print("과체중")
elif 25 <= bmi:
    print("비만")

# 구구단 7단 출력하기
for i in range(1, 9 + 1):
    print(f"7 X {i} = {7 * i}")

# 구구단 2단 ~ 9단 출력하기
for dan in range(2, 9 + 1):
    for i in range(1, 9 + 1):
        print(f"{dan} X {i} = {dan * i}")
    print("-" * 10)

# 구구단 2단 ~ 7단 출력하기
for dan in range(2, 9 + 1):
    for i in range(1, 9 + 1):
        print(f"{dan} X {i} = {dan * i}")
    print("-" * 10)
    if dan == 7:
        break

# 구구단 2단 ~ 7단 출력하되, x홀수인 것만 출력하기
for dan in range(2, 9 + 1):
    for i in range(1, 9 + 1, 2):
        print(f"{dan} X {i} = {dan * i}")
    print("-" * 10)
    if dan == 7:
        break

for dan in range(2, 9 + 1):
    for i in range(1, 9 + 1):
        # if i == 2 or i == 4 or i == 6 or i == 8:
        #     continue
        if i % 2 == 0:
            continue
        print(f"{dan} X {i} = {dan * i}")
    print("-" * 10)
    if dan == 7:
        break


# 퀴즈 3-1
def n_sum(argument):
    number = str(argument)
    sum_num = 0
    if len(number) < 10:
        # for a in range(0, len(number)):     #range(3)   0, 1, 2
        #     sum_num += int(number[a])
        for a in number:
            sum_num += int(a)
        return sum_num
    elif len(number) >= 10:
        return -1


result = n_sum(10)
print(result)
result = n_sum(331)
print(result)
result = n_sum(408)
print(result)
result = n_sum(1000000000)
print(result)


# 퀴즈 3-2
def get_subway_fare(km):
    count_km = 0
    if km <= 10:
        return 720
    else:
        if km <= 50:
            for a in range(11, km + 1, 5):
                count_km += 1
        else:
            for a in range(11, 51, 5):
                count_km += 1
            for a in range(51, km + 1, 8):
                count_km += 1
        return 720 + count_km * 100


fare = get_subway_fare(26)
print(fare)  # 1120
fare = get_subway_fare(61)
print(fare)  # 1720
fare = get_subway_fare(56)
print(fare) # 10: 720 50:1520 56: 1620
fare = get_subway_fare(50)
print(fare)  # 1520


# 퀴즈 3-3
def get_three_six_nine(number):
    number = str(number)
    count = number.count("3") + number.count("6") + number.count("9")
    if count >= 1:
        return "짝" * count
    else:
        return number


result = get_three_six_nine(1)
print(result)
result = get_three_six_nine(3)
print(result)
result = get_three_six_nine(16)
print(result)
result = get_three_six_nine(36)
print(result)

# 퀴즈 3-4
'''
rollercoster() 함수를 만든다. 이 함수에 나이, 키, 몸무게를 
입력하면 탑승 가능인지 탑승 불가능인지 리턴한다.
* 나이 65세 이하, 키 120cm 이상 ~ 190cm 이하, 몸무게 100kg 이하여야지 
탑승 가능, 하나라도 충족 안 되면 탑승 불가능
'''


def rollercoster(age, height, weight):
    if age <= 65 and 120 <= height <= 190 and weight <= 100:
        return "탑승 가능"
    else:
        return "탑승 불가능"


result = rollercoster(33, 165, 48)
print(result)  # 탑승 가능
result = rollercoster(67, 180, 72)
print(result)  # 탑승 불가능
result = rollercoster(21, 193, 95)
print(result)  # 탑승 불가능
result = rollercoster(45, 179, 103)
print(result)  # 탑승 불가능


# 퀴즈 4-1
def is_prime(number):
    count_num = 0
    for a in range(1, number + 1):
        if number % a == 0:
            count_num += 1
    if count_num <= 2:
        return "소수"
    else:
        return "소수 아님"


result = is_prime(2)
print(result)  # 소수
result = is_prime(13)
print(result)  # 소수
result = is_prime(36)
print(result)  # 소수 아님


# 퀴즈 4-2
def get_compliment(sentence):
    if sentence.count("고구마") >= 1:
        return "왓쇼이!"
    elif sentence.count("맛있는") >= 1:
        return "우마이!"
    elif sentence.count("놀랄 만한") >= 1 or sentence.count("황당한") >= 1 or sentence.count("굉장한") >= 1:
        return "요모야..!"
    else:
        return "으무!"


result = get_compliment('고구마 된장국')
print(result)  # 왓쇼이!
result = get_compliment('맛있는 크레이프')
print(result)  # 우마이!
result = get_compliment('놀랄 만한 상황')
print(result)  # 요모야..!
result = get_compliment('좋은 마음가짐이다!')
print(result)  # 으무!

'''
Quiz5-1. 모듈이란?
자동차 부품처럼 필요한 것들끼리 모아둔 파일

Quiz5-2. 패키지란?
모듈들을 모아놓은 집합

Quiz5-3. theater_module.py 모듈(파일)의 price 함수를 p학번 라는 이름으로 호출 하도록 import문을 작성하세요
from theater_module import price as p2313

Quiz5-4. __all__의 역할은?
import 되길 원하는 걸 공개로 설정

Quiz5-5. 지금 파이썬 파일을 직접실행할 때만 실행되고, 다른 모듈에서 import할 때는 실행되지 않도록 하는 제어문은?
if __name__ == "__main__"

Quiz5-6. travel 패키지(폴더) 안에 vietnam.py 모듈(파일) 안의 VietnamPackage 클래스를 생성하고 detail 함수를 호출하는 < 가 >, < 나 >, < 다 > 에 들어갈 각 방법은?
import travel.vietnam
travel.vietnam.VietnamPackage()


from travel import vietnam
vietnam.VietnamPackage()


from travel.vietnam import VietnamPackage
VietnamPackage()
'''
