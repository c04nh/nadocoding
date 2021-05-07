class Icecream:
    def __init__(self, name, flavor):
        self.name = name
        self.flavor = flavor

    # 이름: name 맛: flavor 설명: description
    def set_description(self, description):
        self.description = description

    def __str__(self):
        return f'이름: {self.name}\t맛: {self.flavor}'


# 베리베리스트로베리 = Icecream('베리베리스트로베리', '딸기')
# 베리베리스트로베리.set_description('새콤상큼 딸기 과육이 듬뿍!')
# print(베리베리스트로베리)
# print(베리베리스트로베리.description)
# 뉴욕치즈케이크 = Icecream('뉴욕치즈케이크', '치즈케이크')
# print(뉴욕치즈케이크)
# 초콜릿무스 = Icecream('초콜릿 무스', '초콜릿')
# print(초콜릿무스)


class Cup:
    _CUP_CATEGORIES = ['싱글컵', '더블컵', '파인트']
    _PRICES = [4000, 6200, 8200]

    def __init__(self, name, count_flavor):
        self.name = name
        self.price = Cup._PRICES[count_flavor - 1]
        self.count_flavor = count_flavor
        self.menu = []
        self.add_menu()
        self.order_menu = []

    def add_menu(self):
        베리베리스트로베리 = Icecream('베리베리스트로베리', '딸기')
        베리베리스트로베리.set_description('새콤상큼 딸기 과육이 듬뿍!')
        뉴욕치즈케이크 = Icecream('뉴욕치즈케이크', '치즈케이크')
        초콜릿무스 = Icecream('초콜릿 무스', '초콜릿')

        self.menu.append(베리베리스트로베리)
        self.menu.append(뉴욕치즈케이크)
        self.menu.append(초콜릿무스)

    def show_menu(self):
        for index, icecream in enumerate(self.menu):
            print(index+1, icecream)

    def order(self):
        for n in range(self.count_flavor):
            self.show_menu()                     # 메뉴 보여주기
            flavor = input('맛을 고르세요: ')     # 사용자 선택
            flavor = int(flavor)                # 인텍스를 위해 문자 => 숫자
            icecream = self.menu[flavor-1]      # 메뉴에서 인덱스로 가져오자
            self.order_menu.append(icecream)    # 주문한 메뉴에 추가하자
        print('주문한 아이스크립입니다.')
        for icecream in self.order_menu:    # 주문내역 보여주자
            print(icecream)

    def __str__(self):
        return f'이름: {self.name}\t가격: {self.price}원\t종류: {Cup._CUP_CATEGORIES[self.count_flavor - 1]}'


나현이거 = Cup('더블컵', 2)
print(나현이거)
나현이거.order()
