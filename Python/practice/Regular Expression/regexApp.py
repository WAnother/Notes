import re
from uuid import UUID


def getUrlParts(url):
    reg = re.search(r'http://([\w\.\-_]+)/([\w\.\-_]+)/([\w|\.|\-|_]+)\?', url)
    return (reg.group(1), reg.group(2), reg.group(3))


def getQueryParameters(url):
    reg = re.findall(r'([\w\.\-_]+)=([\w|\.\-_]+)&?', url)
    return reg


def getSpecial(sentence, letter):
    reg = re.findall(r'\b({0}\w*[^{0}\W]|[^\W{0}]\w*{0})\b'.format(letter), sentence, re.IGNORECASE)
    print(reg)


def getRealMac(sentence):
    reg = re.search(r'(\w{2}(:|-)){5}\w{2}', sentence, re.IGNORECASE)
    return reg.group()


def fixList():
    fixedList = []
    with open('Employees.txt', 'r') as myFile:
        contents = myFile.readlines()
    name_exp = '[A-Za-z]+[,\s]+[A-Za-z]+'
    ID_exp = '{?[\w\-]{32,36}}?'
    phone_exp = '\(?[\d]{3}\)?[\-\s]?[\d]{3}[\-\s]?[\d]{4}'
    state_exp = '[\w]+[,\s]?[\w]+'
    space_exp = '[,\s;]+'
    final_exp = r'(?P<Name>{0}){4}(?P<ID>{1})?{4}(?P<Phone>{2})?{4}(?P<State>{3})?'.format(name_exp, ID_exp, phone_exp, state_exp, space_exp)
    for each_line in contents:
        result = re.match(final_exp, each_line)
        if result.group('Name'):
            name = fixName(result.group('Name'))
        else:
            name = None
        if result.group('ID'):
            ID = fixID(result.group('ID'))
        else:
            ID = None
        if result.group('Phone'):
            phone = fixPhone(result.group('Phone'))
        else:
            phone = None
        if result.group('State'):
            state = result.group('State')
        else:
            state = None
        final_result = (name, ID, phone, state)
        fixedList.append(final_result)
    return fixedList


def fixPhone(phone):
    reg = re.findall(r'\d', phone)
    result = '({0}) {1}-{2}'.format(''.join(reg[0:3]), ''.join(reg[3:6]), ''.join(reg[6:10]))
    return result


def fixID(ID):
    reg = re.split(r'[\-]', ID)
    result = "".join(reg)
    if '{' not in result:
        result = '{' + result + '}'
    result = str(UUID(result))
    return result


def fixName(name):
    reg = re.sub(r'(\w+), (\w+)', r'\2 \1', name)
    return reg


def getRejectedEntries():
    fixedList = fixList()
    result = []
    for i in fixedList:
        if not i[1] and not i[2] and not i[3]:
            result.append(i[0])
    return result


def getDic(fixedList):
    dic = {each_one[0]: each_one[1] for each_one in fixedList if each_one[1]}
    return dic


def getEmployeeWithIDs():
    fixedList = fixList()
    fixedDic = getDic(fixedList)
    return fixedDic


def getNonIdList(fixedList):
    lis = [each_one[0] for each_one in fixedList if not each_one[1] and (each_one[2] or each_one[3])]
    return lis


def getEmployeeWithoutIDs():
    fixedList = fixList()
    fixedDic = getNonIdList(fixedList)
    return fixedDic


def getEmployeeWithPhones():
    fixedList = fixList()
    dic = {each_one[0]: each_one[2] for each_one in fixedList if each_one[2]}
    return dic


def getEmployeeWithStates():
    fixedList = fixList()
    dic = {each_one[0]: each_one[3] for each_one in fixedList if each_one[3]}
    return dic


def getCompleteEntries():
    fixedList = fixList()
    dic = {each_one[0]: (each_one[1], each_one[2], each_one[3]) for each_one in fixedList if each_one[1] and each_one[2] and each_one[3]}
    return dic


def main():

    # Problem 1
    # url = 'http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall'
    # result = getUrlParts(url)
    # print(result)

    # Problem 2
    # url = 'http://www.google.com/Math/Const?Pi=3.14&Max_Int=65536&What_Else=Not-Here'
    # result = getQueryParameters(url)
    # print(result)

    # Problem 3
    # s = 'The TART program runs on Tuesdays and Thursdays, but it does not start until next week'
    # result = getSpecial(s, 't')
    # print(result)

    # Problem 4
    # s = "hdgh_dfgd---fgdfg58:1c:0A:6e:39:4Ddfgdfg5.6_756756"
    # result = getRealMac(s)
    # print(result)

    # Problem 5
    # result = getRejectedEntries()
    # print(result)

    # Problem 6
    # result = getEmployeeWithIDs()
    # print(result)

    # Problem 7
    # result = getEmployeeWithoutIDs()
    # print(result)

    # Problem 8
    # result = getEmployeeWithPhones()
    # print(result)

    # Problem 9
    # result = getEmployeeWithStates()
    # print(result)

    # Problem 10
    # result = getCompleteEntries()
    # print(result)


if __name__ == '__main__':
    main()
