from exModule import runNetworkCode
import os
import sys
import re


def checkNetwork(**kwargs):
    try:
        runNetworkCode(**kwargs)
    except ConnectionError:
        raise
    except OSError as e:
        return 'An issue encountered during runtime. The name of the error is: {0}'.format(e)
    except:
        return False
    else:
        return True


def isOK(signalName):
    reg = re.match(r'[A-Z]{3}\-\d{3}$', signalName)
    if reg:
        return True
    else:
        return False


def loadDataFrom(signalName, folderName):
    if not isOK(signalName):
        raise ValueError('{0} is invalid'.format(signalName))
    else:
        path_name = '{0}/{1}.txt'.format(folderName, signalName)
        if not os.path.exists(path_name):
            raise OSError('File not exists')
        else:
            with open(path_name, 'r') as myFile:
                contents = myFile.readlines()
            list_float = []
            count = 0
            for each_line in contents:
                reg = re.match(r'[\-]?\d+\.\d+', each_line)
                if reg:
                    list_float.append(float(each_line))
                else:
                    count += 1
            result = (list_float, count)
            return result


def isBounded(signalValues, bounds, threshold):
    if not signalValues:
        raise ValueError('Signal contains no data')
    min_value, max_value = bounds
    count = 0
    for signal in signalValues:
        if signal < min_value or signal > max_value:
            count += 1
    if count <= threshold:
        return True
    else:
        return False


def main():
    result = isBounded([], (0, 3.5), 2)
    print(result)


if __name__ == '__main__':
    main()
