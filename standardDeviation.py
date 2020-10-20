import math

def DataCollector(strData):
    originalData = []
        TempData = strData.split()
        for i in TempData:
            originalData.append(int(i))
        return originalData

def Mean(Arr):
    mean = 0
    for i in Arr:
        mean = mean + i
    mean = mean / len(Arr)
    return mean

def SD(Arr, mean):
    xi_m = []
    sd = 0
    for i in Arr:
        xi_m.append((i-mean)*(i-mean))
    sd = sum(xi_m)/len(Arr)
    sd = math.sqrt(sd) 
    return sd

x = int(input())
data = DataCollector(input())
mean = Mean(data)
print(SD(data, mean))