import os


def loadPfile():
    with open('projects.txt', 'r') as myFile:
        content = myFile.readlines()[2:]
    return content


def loadSfile():
    with open('students.txt', 'r') as myFile:
        content = myFile.readlines()[2:]
    return content


def getComponentCountByProject(projectID):
    content = loadPfile()
    result = [0, 0, 0, 0]
    flag = False
    for each_line in content:
        if str(each_line).split()[1] == projectID:
            flag = True
            with open('Circuits/circuit_{0}.txt'.format(str(each_line).split()[0]), 'r') as myFile:
                circuit_content = myFile.readlines()[4]
            for i in circuit_content:
                if i == 'R':
                    result[0] += 1
                elif i == 'L':
                    result[1] += 1
                elif i == 'C':
                    result[2] += 1
                elif i == 'T':
                    result[3] += 1

    if flag:
        return tuple(result)
    else:
        return None


def getStudentDic(content):
    dic = {str(each_line.split('|')[0]).strip(): str(each_line.split('|')[1]).strip() for each_line in content}
    return dic


def reverseStudentIdc(student_dic):
    new_dic = {value: key for key, value in student_dic.items()}
    return new_dic


def getComponentCountByStudent(studentName):
    content = loadSfile()
    new_content = getStudentDic(content)
    if studentName not in new_content:
        return None
    studentID = new_content[studentName]
    result = [0, 0, 0, 0]
    flag = False
    for filename in os.listdir('./Circuits'):
        with open('./Circuits/{0}'.format(filename)) as myFile:
            circuit_content = myFile.readlines()
        students = circuit_content[1].split(', ')
        students[-1] = str(students[-1]).strip()
        for i in students:
            if i == studentID:
                flag = True
                materials = circuit_content[4]
                for j in materials:
                    if j == 'R':
                        result[0] += 1
                    elif j == 'L':
                        result[1] += 1
                    elif j == 'C':
                        result[2] += 1
                    elif j == 'T':
                        result[3] += 1
    if flag:
        return tuple(result)
    else:
        return tuple()


def getProjectDic(content):
    dic = {}
    for each_line in content:
        key, value = each_line.split()
        key = key.strip()
        value = value.strip()
        dic.setdefault(key, []).append(value)
    return dic


def getParticipationByStudent(studentName):
    content = loadPfile()
    project_dic = getProjectDic(content)
    student_content = loadSfile()
    student_dic = getStudentDic(student_content)
    if studentName not in student_dic.keys():
        return None
    result = set()
    studentId = student_dic[studentName]
    for filename in os.listdir('./Circuits'):
        with open('./Circuits/{0}'.format(filename)) as myFile:
            circuit_content = myFile.readlines()
        students = circuit_content[1].split(', ')
        students[-1] = str(students[-1]).strip()
        for i in students:
            if i == studentId:
                real_name = os.path.splitext(filename)
                circuit_id = real_name[0].split('_')[1]
                for z in project_dic[circuit_id]:
                    result.add(z)

    return result


def getParticipationByProject(projectID):
    project_content = loadPfile()
    student_content = loadSfile()
    student_dic = getStudentDic(student_content)
    student_dic = reverseStudentIdc(student_dic)
    flag = False
    result = set()
    for each_line in project_content:
        if str(each_line).split()[1] == projectID:
            flag = True
            with open('./Circuits/circuit_{0}.txt'.format(str(each_line).split()[0]), 'r') as myFile:
                contents = myFile.readlines()
            student_id = contents[1].split(', ')
            student_id[-1] = str(student_id[-1]).strip()
            for i in student_id:
                result.add(student_dic[i])
    if flag:
        return result
    else:
        return None


def getProjectByComponent(components):
    project_content = loadPfile()
    project_dic = getProjectDic(project_content)
    result = {}
    for i in components:
        value = set()
        for filename in os.listdir('./Circuits'):
            with open('./Circuits/{0}'.format(filename)) as myFile:
                contents = myFile.readlines()
            component = contents[4].split(', ')
            if i in component:
                for z in project_dic[filename[8:13]]:
                    # print(filename)
                    value.add(z)
        result[i] = value
    return result


def getStudentByComponent(components):
    student_content = loadSfile()
    student_dic = getStudentDic(student_content)
    student_dic = reverseStudentIdc(student_dic)
    result = {}
    for i in components:
        value = set()
        for filename in os.listdir('./Circuits'):
            with open('./Circuits/{0}'.format(filename)) as myFile:
                contents = myFile.readlines()
                component = list(contents[4].split(', '))
                if i in component:
                    students = contents[1].split(', ')
                    students[-1] = students[-1].strip()
                    for j in students:
                        value.add(student_dic[j])
        result[i] = value
    return result


def getComponentByStudent(studentNames):
    student_content = loadSfile()
    student_dic = getStudentDic(student_content)
    result = {}
    for i in studentNames:
        student_id = student_dic[i]
        value = set()
        for filename in os.listdir('./Circuits'):
            with open('./Circuits/{0}'.format(filename)) as myFile:
                contents = myFile.readlines()
                students = contents[1].split(', ')
                students[-1] = students[-1].strip()
                if student_id in students:
                    components = contents[4].split(', ')
                    for z in components:
                        value.add(z)
        result[i] = value
    return result


def getCommonByProject(projectID1, projectID2):
    flag1 = False
    flag2 = False
    project_content = loadPfile()
    result1 = []
    result2 = []
    for each_line in project_content:
        if each_line.split()[1] == projectID1:
            with open('./Circuits/circuit_{0}.txt'.format(each_line.split()[0])) as myFile:
                contents = myFile.readlines()
            components = contents[4].split(', ')
            flag1 = True
            for i in components:
                result1.append(i)
        if each_line.split()[1] == projectID2:
            with open('./Circuits/circuit_{0}.txt'.format(each_line.split()[0])) as myFile2:
                contents2 = myFile2.readlines()
            components2 = contents2[4].split(', ')
            flag2 = True
            for j in components2:
                result2.append(j)
    result3 = list(set(result1) & set(result2))
    result3.sort()
    if flag1 and flag2:
        return result3
    else:
        return None


def getCommonByStudent(studentName1, studentName2):
    studentNames = {studentName1, studentName2}
    temp_result = getComponentByStudent(studentNames)
    result = list(temp_result[studentName1] & temp_result[studentName2])
    result.sort()
    return result


def getProjectByCircuit():
    project_content = loadPfile()
    project_dic = getProjectDic(project_content)
    return project_dic


def getCircuitByStudent():
    student_content = loadSfile()
    student_dic = getStudentDic(student_content)
    student_dic = reverseStudentIdc(student_dic)
    result = {}
    for filename in os.listdir('./Circuits'):
        with open('./Circuits/{0}'.format(filename), 'r') as myFile:
            contents = myFile.readlines()
        students = contents[1].split(', ')
        students[-1] = students[-1].strip()
        for i in students:
            result.setdefault(student_dic[i], []).append(filename[8:13])
    return result


def getCircuitByStudentPartial(studentName):
    student_content = loadSfile()
    student_dic = getStudentDic(student_content)
    names = list(student_dic.keys())
    temp_result = getCircuitByStudent()
    result = {}
    for i in names:
        first, last = i.split(', ')
        last = last.strip()
        if first == studentName or last == studentName:
            result[i] = temp_result[i]
    return result


def main():
    # Problem 1
    # projectID = '082D6241-40EE-432E-A635-65EA8AA374B6'
    # result = getComponentCountByProject(projectID)
    # print(result)

    # Problem 2
    # studentName = 'Adams, Keith'
    # result = getComponentCountByStudent(studentName)
    # print(result)

    # Problem 3
    # studentName = 'Adams, Keith'
    # result = getParticipationByStudent(studentName)
    # print(result)

    # Problem 4
    # projectID = '082D6241-40EE-432E-A635-65EA8AA374B6'
    # result = getParticipationByProject(projectID)
    # print(result)

    # Problem 5
    # components = {'T71.386', 'L341.064'}
    # result = getProjectByComponent(components)
    # print(result)

    # Problem 6
    # components = {'T71.386', 'L341.064'}
    # result = getStudentByComponent(components)
    # print(result)

    # Problem 7
    # studentNames = {'Sanders, Emily', 'Alexander, Carlos'}
    # result = getComponentByStudent(studentNames)
    # print(result)

    # Problem 8
    # projectID1 = '17A946D3-A1B0-4335-8808-8594D9FBD62C'
    # projectID2 = '83383848-1D69-40D4-A360-817FB22769ED'
    # result = getCommonByProject(projectID1, projectID2)
    # print(result)

    # Problem 9
    # studentName1 = 'Sanders, Emily'
    # studentName2 = 'Campbell, Eugene'
    # result = getCommonByStudent(studentName1, studentName2)
    # print(result)

    # Problem 10
    # result = getProjectByCircuit()
    # print(result)

    # Problem 11
    # result = getCircuitByStudent()
    # print(result)

    # Problem 12
    # studentName = 'Adams'
    # result = getCircuitByStudentPartial(studentName)
    # print(result)


if __name__ == '__main__':
    main()
