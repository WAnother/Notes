from enum import Enum
import random


class Level(Enum):
    Freshman = 1
    Sophomore = 2
    Junior = 3
    Senior = 4


class Student:
    def __init__(self, ID, firstName, lastName, level):
        if not isinstance(level, Level):
            raise TypeError('The argument must be an instance of the ‘Level’ Enum.')
        self.ID = ID
        self.firstName = firstName
        self.lastName = lastName
        self.level = level

    def __str__(self):
        result = '{0}, {1} {2}, {3}'.format(self.ID, self.firstName, self.lastName, self.level.name)
        return result


class Circuit:
    def __init__(self, ID, resistors, capacitors, inductors, transistors):
        self.ID = ID
        for resistor in resistors:
            if resistor[0] != 'R':
                raise ValueError('The resistors’ list contain invalid components.')
        self.resistors = resistors
        for capacitor in capacitors:
            if capacitor[0] != 'C':
                raise ValueError('The resistors’ list contain invalid components.')
        self.capacitors = capacitors
        for inductor in inductors:
            if inductor[0] != 'L':
                raise ValueError('The resistors’ list contain invalid components.')
        self.inductors = inductors
        for transistor in transistors:
            if transistor[0] != 'T':
                raise ValueError('The resistors’ list contain invalid components.')
        self.transistors = transistors

    def __str__(self):
        if len(self.resistors) <= 9:
            num1 = '0' + str(len(self.resistors))
        else:
            num1 = len(self.resistors)
        if len(self.capacitors) <= 9:
            num2 = '0' + str(len(self.capacitors))
        else:
            num2 = len(self.capacitors)
        if len(self.inductors) <= 9:
            num3 = '0' + str(len(self.inductors))
        else:
            num3 = len(self.inductors)
        if len(self.transistors) <= 9:
            num4 = '0' + str(len(self.transistors))
        else:
            num4 = len(self.transistors)
        result = '{0}: (R = {1}, C = {2}, L = {3}, T = {4})'.format(self.ID, num1, num2, num3, num4)
        return result

    def getDetails(self):
        result = self.ID + ': '
        for resistor in self.resistors:
            result = result + resistor + ', '
        for capacitor in self.capacitors:
            result = result + capacitor + ', '
        for inductor in self.inductors:
            result = result + inductor + ', '
        for transistor in self.transistors:
            result = result + transistor + ', '
        return result[:-2]

    def __contains__(self, item):
        if type(item) != str:
            raise TypeError('Not String')
        if item[0] != 'R' and item[0] != 'C' and item[0] != 'L' and item[0] != 'T':
            raise ValueError('Value wrong')
        if item in self.resistors or item in self.capacitors or item in self.inductors or item in self.transistors:
            return True
        else:
            return False

    def __add__(self, item):
        if type(item) == Circuit:
            temp = list(range(10))
            new_ID = random.sample(temp, 5)
            converted_ID = ''.join(str(i) for i in new_ID)
            resistors_list = list(set(self.resistors).union(set(item.resistors)))
            capacitors_list = list(set(self.capacitors).union(set(item.capacitors)))
            inductors_list = list(set(self.inductors).union(set(item.inductors)))
            transistors_list = list(set(self.transistors).union(set(item.transistors)))
            return Circuit(converted_ID, resistors_list, capacitors_list, inductors_list, transistors_list)

        if type(item) != str:
            raise TypeError('Not String')
        if item[0] != 'R' and item[0] != 'C' and item[0] != 'L' and item[0] != 'T':
            raise ValueError('Value wrong')
        if item in self.resistors or item in self.capacitors or item in self.inductors or item in self.transistors:
            return self
        else:
            if item[0] == 'R':
                self.resistors.append(item)
            elif item[0] == 'C':
                self.capacitors.append(item)
            elif item[0] == 'L':
                self.inductors.append(item)
            else:
                self.transistors.append(item)
            return self

    def __radd__(self, item):
        return self.__add__(item)

    def __sub__(self, item):
        if type(item) != str:
            raise TypeError('Not String')
        if item[0] != 'R' and item[0] != 'C' and item[0] != 'L' and item[0] != 'T':
            raise ValueError('Value wrong')
        if item not in self.resistors and item not in self.capacitors and item not in self.inductors and item not in self.transistors:
            return self
        else:
            if item[0] == 'R':
                self.resistors.remove(item)
            elif item[0] == 'C':
                self.capacitors.remove(item)
            elif item[0] == 'L':
                self.inductors.remove(item)
            else:
                self.transistors.remove(item)
            return self


class Project:
    def __init__(self, ID, participants, circuits):
        # Ignore all necessary checks, assume every parameter is right
        self.ID = ID
        self.participants = participants
        self.circuits = circuits

    def __str__(self):
        if len(self.circuits) <= 9:
            num1 = '0' + str(len(self.circuits))
        else:
            num1 = len(self.circuits)
        if len(self.participants) <= 9:
            num2 = '0' + str(len(self.participants))
        else:
            num2 = len(self.participants)
        result = '{0}: {1} Circuit, {2} Participants'.format(self.ID, num1, num2)
        return result

    def getDetails(self):
        result = '{0}\n\nParticipants\n'.format(self.ID)
        for student in self.participants:
            result = result + '{0}\n'.format(student)
        result = result + '\nCircuits\n'
        for circuit in self.circuits:
            result = result + '{0}\n'.format(circuit.getDetails())
        return result

    def __contains__(self, item):
        if type(item) == Circuit:
            for i in self.circuits:
                if item.ID == i.ID:
                    return True
            return False
        elif type(item) == Student:
            for i in self.participants:
                if item.ID == i.ID:
                    return True
            return False
        else:
            raise TypeError('Type Wrong')

    def __add__(self, item):
        if isinstance(item, Circuit):
            if item in self.circuits:
                return self
            else:
                self.circuits.append(item)
                return self
        elif isinstance(item, Student):
            if item in self.participants:
                return self
            else:
                self.participants.append(item)
                return self
        else:
            raise TypeError('Wrong Type')

    def __sub__(self, item):
        if isinstance(item, Circuit):
            if item not in self.circuits:
                return self
            else:
                self.circuits.remove(item)
                return self
        elif isinstance(item, Student):
            if item not in self.participants:
                return self
            else:
                self.participants.remove(item)
                return self


class CapStone(Project):
    def __init__(self, ID, participants, circuits):
        for student in participants:
            if student.level != Level.Senior:
                raise ValueError('Wrong')
        super().__init__(ID, participants, circuits)

    def __add__(self, item):
        if item.level != Level.Senior:
            raise ValueError('Wrong')
        super().__add__(item)
        return self


def main():
    result3 = Student('15487-79431', 'John', 'Smith', Level.Senior)
    result4 = Student('55152-55132', 'Adam', 'Keith', Level.Senior)
    result = Circuit("11023", ["R1.1", "R1.5", "R2.3", "R1.3"], ["C4.8", "C4.6", "C2.42", "C5.62", "C1.79", "C10.8", "C10.1"], ["L1.1", "L12.5", "L66.2"], ["T1.24", "T90.1"])
    result2 = Circuit("10101", ["R5.7", 'R1.1', 'R1.1'], ["C6.23"], ["L11.51"], ["T8.2"])
    project1 = Project('38753067-e3a8-4c9e-bbde-cd13165fa21e', [result3, result4], [result, result2])
    result5 = Student('66234-55512', 'Jordan', 'Michale', Level.Senior)
    result6 = Circuit("66344", ["R5.8", 'R1.2', 'R1.1'], ["C6.23"], ["L11.51"], ["T8.2"])
    project1 = project1 + result5
    project1 = project1 + result6
    project1 = project1 - result2
    project1 = project1 - result5
    final_result = CapStone('38753067-e3a8-4c9e-bbde-cd13165fa21e', [result3, result4], [result, result2])
    final_result = final_result + result5
    print(final_result.getDetails())


if __name__ == '__main__':
    main()
