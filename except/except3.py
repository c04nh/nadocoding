list1 = [1, 5, 7]

try:
    print(list1[0])
    print(list1[1])
    print(list1[2])
    print(list1[3])
except IndexError as e:
    print(e)
except:
    pass
finally:
    print('성공!!!✨✨✨✨')