import pickle
import requests

r = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
data = r.text
print(data)

# with open("Iris.txt", "a") as iris:
#     data2=[]
#     data2=data2.append(data)

with open("Iris.txt", "a") as iris:
    data2 = []
    ele = iris.read().split("\n")
    data2.append(ele)

with open("Iris.pkl", "wb") as obj_write:
    pickle.dump(data2, obj_write)

with open("Iris.pkl", "rb") as obj_read:
    iris = pickle.load(obj_read)
print(iris)
for i in iris:
    for j in i:
        print(j, end = "\n")
