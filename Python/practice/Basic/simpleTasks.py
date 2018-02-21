def loadFile():
    with open("sequence.txt", "r") as myFile:
        content = myFile.read()
    return content


def find(pattern):
    sequence = loadFile()
    result = []
    for index, i in enumerate(sequence):
        check = True
        pattern_result = ""
        for index2, j in enumerate(pattern):
            if index > len(sequence) - len(pattern):
                break
            temp = sequence[index + index2]
            if temp == j or j == "X":
                pattern_result += temp
            else:
                check = False
                break
            if len(pattern_result) == len(pattern) and check:
                result.append(pattern_result)
    return result


def getStreakProduct(sequence, maxSize, product):
    result = []
    for index, i in enumerate(sequence):
        multiple = 1
        pattern = ""
        for j in range(maxSize):
            if index > len(sequence) - maxSize:
                break
            multiple *= int(sequence[index + j])
            pattern += sequence[index + j]
            if multiple == product:
                result.append(pattern)
                break
    return result


def writePyramids(filePath, baseSize, count, char):
    with open(filePath, "w") as myFile:
        num = int(baseSize / 2) + 1
        for i in range(num):
            space = int(baseSize / 2 - i)
            stuff = int(baseSize - 2 * space)
            contents = ""
            for j in range(count):
                contents += " " * space
                contents += str(char) * stuff
                contents += " " * space
                if j < count - 1:
                    contents += " "
                else:
                    contents += '\n'
            myFile.write(contents)


def getStreaks(sequence, letters):
    result = []
    for index, i in enumerate(sequence):
        if result:
            temp_pattern = list(result[-1])
            if i == temp_pattern[-1] and sequence[index - 1] == temp_pattern[-1]:
                continue
        for index2, j in enumerate(letters):
            if i == j:
                pattern = ""
                temp = sequence[index]
                while temp == j and index < len(sequence):
                    pattern += temp
                    if index >= len(sequence) - 1:
                        result.append(pattern)
                        break
                    index += 1
                    temp = sequence[index]
                    if temp != j:
                        result.append(pattern)
                        break

    return result


def findNames(nameList, part, name):
    name = name.upper()
    result = []
    for i in nameList:
        first, last = i.split()
        first = first.upper()
        last = last.upper()
        if part == 'L' and last == name:
            result.append(i)
        elif part == 'F' and first == name:
            result.append(i)
        elif part == 'FL' and (first == name or last == name):
            result.append(i)
    return result


def convertToBoolean(num, size):
    result = []
    if type(num) != int or type(size) != int:
        return result
    binary = bin(num)
    binary_result = binary[2:]
    while(len(binary_result) < size):
        binary_result = '0' + binary_result
    for c in binary_result:
        if c == '1':
            result.append("True")
        else:
            result.append("False")
    return result


def convertToInteger(boolList):
    if type(boolList) != list or not boolList:
        return None
    string = ''
    for i in boolList:
        if type(i) != bool:
            return None
        elif i:
            string += '1'
        else:
            string += '0'
    return int(string, 2)


def main():
    # Problem 1
    # pattern = "X38X"
    # result = find(pattern)
    # print(result)

    # Problem 2
    # sequence = "54789654321687984"
    # maxSize = 5
    # product = 288
    # result2 = getStreakProduct(sequence, maxSize, product)
    # print(result2)

    # Problem 3
    writePyramids("pyramid13.txt", 13, 6, 'X')
    writePyramids("pyramid15.txt", 15, 5, '*')

    # Problem 4
    # sequence = "AAASSSSSSAPPPSSPPBBCCCSSS"
    # result = getStreaks(sequence, "PAZ")
    # print(result)

    # Problem 5
    # names = ["George Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"]
    # result = findNames(names, "L", "Johnson")
    # print(result)
    # result = findNames(names, "F", "JOHNSON")
    # print(result)
    # result = findNames(names, "FL", "Johnson")
    # print(result)

    # Problem 6
    # result = convertToBoolean(9, 3)
    # print(result)

    # Problem 7
    bList = [False, False, True, False, False, True]
    result = convertToInteger(bList)
    print(result)


if __name__ == '__main__':
    main()
