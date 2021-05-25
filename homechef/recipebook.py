from recipe import Recipe


class Recipebook:
    def __init__(self):
        self.recipe_list = []

    def add_recipe(self):
        # 추가할 레시피 이름을 입력 받좌~
        recipe_name = input('>> 레시피 이름을 입력하세요 : ')
        # 중복 체크
        for recipe in self.recipe_list:
            # 중복되는 레시피가 있으면
            if recipe_name == recipe.name:
                # 이미 있다고 알려주자
                print('이미 존재하는 레시피입니다!😛😛😛😛')
                return
        # 중복되는 레시피가 없으면
        # 새 레시피 생성하자
        new_recipe = Recipe(recipe_name)
        new_recipe.set_recipe()
        # 레시피 리스트에 추가하작
        self.recipe_list.append(new_recipe)

    def show_all_recipe(self):
        for index, recipe in enumerate(self.recipe_list):
            print(f'{index + 1}번')
            print(recipe)

    def search_Recipe(self):
        # 검색할 레시피 이름을 입력 받자
        recipe_name = input('>> 찾는 레시피를 검색하세요: ')
        searche_recipe =[]
        # 검색.. 체크 반복문 시~~~~~~~~~~~작
        for recipe in self.recipe_list:
            # 있으면
            if recipe_name in recipe.name:
                # 보~여주세요
                print(recipe)
                searche_recipe.append(recipe)
        # 반복문종료
        # 찾아진 레시피가 없다면
        if len(searche_recipe) == 0:
            # 추가할래?
            choice = input('>> 찾는 레시피가 없습니다. 추가하시겠습니까? (1: 예, 0: 아니오): ')
            # 넹 추가 할래요잉~
            if choice == '1':
                # 레시피 추가하기
                self.add_recipe()
            # 추가 안 해
            else:
                # 끝.
                return

    def __str__(self):
        pass

