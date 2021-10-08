import pickle
from save_object import Person

with open('object.bin', 'rb') as f:
    data = pickle.load(f)
print(data)

with open('objects.bin', 'rb') as f:
    data = pickle.load(f)
for d in data:
    print(d)