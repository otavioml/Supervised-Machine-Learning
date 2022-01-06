import numpy as np

def dataPoints(filename):
    data = np.loadtxt(filename, delimiter=',', dtype=str)

    listofpoints = []

    for d in data:
        listofpoints.append(tuple(d))

    ans = []
    for tupl in listofpoints:
        temp = []
        for x in tupl:
            try:
                temp.append(float(x))
            except Exception:
                temp.append(x)
        ans.append(tuple(temp))

    return ans

def getDimensions(data):
    return len(data[0])

listofpoints = dataPoints('data/haberman.dat')

print(listofpoints)
print(type(listofpoints))
print(type(listofpoints[0]))
print(listofpoints[0])
print(listofpoints[-1])

print("Dimensions: " + str(getDimensions(listofpoints)))