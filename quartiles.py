def DataCollector(strData):
    originalData = []
    TempData = strData.split()
    for i in TempData:
        originalData.append(int(i))
    return originalData


def Median(Arr, total):
    mid = int(total/2)
    if(total%2==0):
        median = (Arr[mid-1] + Arr[mid])/2 
        return int(median), mid
    else:
        return Arr[mid], mid

def Quartile(Arr, median):
    Q1 = Arr[:median].sort()
    Q3 = Arr[median+1:].sort()
    q1 = Median(Q1, len(Q1))
    q3 = Median(Q3, len(Q3))
    return [q1[0], Arr[median], q3[0]]

data = [4, 17 ,7, 14, 18, 12, 3, 16, 10, 4, 4, 12]
median, mid = Median(data, len(data))
quartileResult = Quartile(data, mid)
for i in quartileResult:
    print(i)