class Drink:
    _CUPS = ('레귤러', '점보')
    _ICES = ('0%', '50%', '100%', '150%')
    _SUGARS = ('0%', '50%', '100%', '150%')
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cup = 0
        self.ice = 2
        self.sugar = 2

    def set_cup(self):
        for index, cup in enumerate(Drink._CUPS):
            print(f'{index+1}: {cup}')
        cup = input('컵사이즈를 선택하세요: ')
        if cup == '':
            self.cup = 0
        else:
            cup = int(cup) - 1
            self.cup = cup
        if self.cup == 1:
            self.price += 500

    def set_ice(self):
        for index, ice in enumerate(Drink._ICES):
            print(f'{index+1}: {ice}')
        ice = input('얼음량을 선택하세요: ')
        self.ice  = 2 if ice == '' else int(ice) -1

    def set_sugar(self):
        for index, sugar in enumerate(Drink._SUGARS):
            print(f'{index+1}: {sugar}')
        sugar = input('당도를 선택하세요: ')
        self.sugar  = 2 if sugar == '' else int(sugar) -1

    def order(self):
        self.set_cup()
        self.set_ice()
        self.set_sugar()

    def __str__(self):
        return f'이름: {self.name}\t가격: {self.price}원\t컵사이즈: {Drink._CUPS[self.cup]}\t얼음량: {Drink._ICES[self.ice]}\t당도: {Drink._SUGARS[self.sugar]}'


수민이꺼 = Drink('초코버블티', 3300)
수민이꺼.order()
print(수민이꺼)


class Coffee(Drink):
    pass


class Bubbletea:
    def __init__(self):
        pass
    def __str__(self):
        pass


class Order:
    def __init__(self):
        pass
    def __str__(self):
        pass

