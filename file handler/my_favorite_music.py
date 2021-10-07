# 파일 저장
with open('my_favorite_music.txt', 'w', encoding='utf-8') as f:
    f.write('이선우: 너를 생각해\n')
    f.write('주서영: 낙하\n')

# 파일 불러오기
with open('my_favorite_music.txt', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if line == '':
            break
        line_list = line.split(':')
        name = line_list[0]
        music = line_list[1].rstrip()
        print(f'이름: {name}    좋아하는 노래: {music}')
        # print(line.rstrip())