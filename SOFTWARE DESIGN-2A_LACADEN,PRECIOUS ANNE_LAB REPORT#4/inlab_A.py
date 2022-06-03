def recursiveMin(data):
        if len(data) == 0:
                return None
        if len(data) == 1:
                return data[0]
        return min(data[0], recursiveMin(data[1:]))

def recursiveMax(data):
        if len(data) == 0:
                return None
        if len(data) == 1:
                return data[0]
        return max(data[0], recursiveMax(data[1:]))

def recursiveRev(data):
        if len(data) <= 1:
                return data
        return recursiveRev(data[1:]) + [data[0]]

print(recursiveMin([11, 12, 13, 14, 15, 16]))
print(recursiveMax([11, 12, 13, 14, 15, 16]))
print(recursiveRev([11, 12, 13, 14, 15, 16]))