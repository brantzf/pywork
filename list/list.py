import read
import sanitize

# clear
def clearData(data):
    clear_data = []
    for item in data:
        clear_data.append(sanitize.st(item))      
    return  clear_data;

# clear2
def clearData2(data):       
    return  [sanitize.st(item) for item in data]

# get
def getData(data):
    return sorted(data)[0 : 3]

# get@set
def getData2(data):
    return sorted(set(data))[0 : 3]

james = getData(clearData(read.readData('data/james.txt')))
sarah = getData(clearData2(read.readData('data/sarah.txt')))
julie = getData2(clearData2(read.readData('data/julie.txt')))

print(james)
print(sarah)
print(julie)