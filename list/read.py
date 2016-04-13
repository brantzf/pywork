# read
def readData(src):
    with open(src) as dest:
        data = dest.readline()
    
    return data.strip().split(',')