class Entertainer:  # 키, 얼굴, 인성, 이름
    def __init__(self, name):
        self.name = name

    def set_height(self, height):
        self.height = height

    def set_face(self, face):
        self.face = face

    def set_kind(self, kind):  # 인성
        self.kind = kind

    def set_name(self, name):
        self.name = name

    # def info(self):
    #     print(f'이름: {self.name}\t키: {self.height}\t얼굴: {self.face}\t인성: {self.kind}')

    def __str__(self):
        return f'이름: {self.name}\t키: {self.height}\t얼굴: {self.face}\t인성: {self.kind}'

아이유 = Entertainer('아이유')
# 아이유.set_name('이지은')
아이유.set_height('161cm')
아이유.set_face('형섭썜이상형')
아이유.set_kind('That\'s very good.')
print(아이유)
# 아이유.info()

홍서영 = Entertainer('홍서영')
홍서영.set_height('172cm')
홍서영.set_face('예쁨..')
홍서영.set_kind('나보다 괜찮겠지 뭐..')
print(홍서영)


class Singer(Entertainer):
    def __init__(self, name, song):
        super().__init__(name)
        self.song = song

    def __str__(self):
        return super().__str__() + f'\t대표곡: {self.song}'


miley = Singer('Miley Cyrus', 'Wrecking Ball')
miley.set_height('165cm')
miley.set_face('괜찮은듯해요')
miley.set_kind('좋은노래로보답부탁')
print(miley)


class Talent(Entertainer):
    def __init__(self, name, filmography):
        super().__init__(name)
        self.filmography = filmography

    def __str__(self):
        return super().__str__() + f'\t작품: {self.filmography}'


cate = Talent('Cate Blanchett', '<토르: 라그나로크>, <벤자민 버튼의 시간은 거꾸로 간다>, <오션스 8>')
cate.set_height('174cm')
cate.set_face('Sooooo gorgeous!!')
cate.set_kind('최고')
print(cate)

bridget = Talent('Bridget Regan', '<제인 더 버진>, <에이전트 카터>, <레전드 오브 시커>')
bridget.set_height('175cm')
bridget.set_face('너무너무너무너무너무너무너무너무너무 예뻐요')
bridget.set_kind('잘 모르지만.. 좋겠지 뭐..~')
print(bridget)

favorite = []
favorite.append(cate)
favorite.append(bridget)
# print(favorite)
for 멤버 in favorite:
    print(멤버)