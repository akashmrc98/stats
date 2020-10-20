x = int(input())
y = input()
strData = y.split()

data = []
for i in strData:
    data.append(int(i))
data.sort()

mean = 0
for j in data:
    mean = mean+j
mean = mean / len(data)

mid = int(x/2)
median = (data[mid]+data[mid-1])/2

modeList = {}
for p in data:
    modeList[p] = 0;

for q in data:
    for r in modeList.keys():
        if(r==q):
            modeList[r] = modeList[r]+1

    
print(mean)
print(median)
print(max(modeList, key=modeList.get))
