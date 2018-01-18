import moduleTasks


def loadMultiple(signalNames, folderName, maxCount):
    result = {}
    for signal in signalNames:
        try:
            list_float, count = moduleTasks.loadDataFrom(signal, folderName)
        except OSError:
            result[signal] = None
        else:
            if count <= maxCount:
                result[signal] = list_float
            else:
                result[signal] = []
    return result


def saveData(signalDictionary, targetFolder, bounds, threshold):
    for key, value in signalDictionary.items():
        try:
            check = moduleTasks.isBounded(value, bounds, threshold)
        except ValueError:
            pass
        else:
            if check:
                path_name = '{0}/{1}.txt'.format(targetFolder, key)
                with open(path_name, 'w') as myFile:
                    for v in value[:-1]:
                        myFile.write('{:.3f}\n'.format(v))
                    myFile.write('{:.3f}\n'.format(v))
            else:
                pass


def main():
    result = loadMultiple(['AFW-481', 'CIG-308'], 'Signals', 10)
    saveData(result, 'newSignals', (0, 100), 100)


if __name__ == '__main__':
    main()
