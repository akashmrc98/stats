def DataCollector(strData):
    originalData = []
    TempData = strData.split()
    for i in TempData:
        originalData.append(int(i))
    return originalData

def ListMultiplier(data, weights):
    multiplierList = []
    for i in range(0, len(data)):
        multiplierList.append(data[i]*weights[i])
    listSum = sum(multiplierList)
    return listSum

x = int(input())
data = DataCollector(input())
weights = DataCollector(input())

mw = (ListMultiplier(data, weights))/sum(weights)
print(mw)
