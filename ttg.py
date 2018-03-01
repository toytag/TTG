def not_(a):
    return not a

def and_(a, b):
    return a and b

def or_(a, b):
    return a or b

def imply(a, b):
    if a == True and b == False:
        return False
    else:
        return True

def back_imply(a, b):
    if a == True and b == False:
        return True
    else:
        return False

def iff(a, b):
    if a == b:
        return True
    else:
        return False

class WFF:
    precedence = {
        '¬': 1,
        '∧': 2,
        '∨': 3,
        '→': 4,
        '←': 4,
        '↔︎': 5,
    }

    operator = {
        '¬': not_,
        '∧': and_,
        '∨': or_,
        '→': imply,
        '←': back_imply,
        '↔︎': iff,
    }

    def __init__(self, wff):
        self.wff = wff.replace(' ', '')
        self.pVars = self.get_pVars()
        self.ptvDicts = self.possibleTruthValueDictList()
        self.truthTable = [self.logicEval(ptvDict) for ptvDict in self.ptvDicts]

    def get_pVars(self):
        pVarSet = set()
        for i in self.wff:
            if i.isalpha():
                pVarSet.add(i)
        pVars = list(pVarSet)
        pVars.sort()
        return pVars

    def possibleTruthValueDictList(self):
        def TorF(n=0, d={}):
            if n == len(self.pVars):
                ptvd = d.copy()
                ptvDicts.append(ptvd)
                return None
            for i in [True, False]:
                d[self.pVars[n]] = i
                TorF(n + 1, d)
        ptvDicts = []
        TorF()
        return ptvDicts

    def logicEval(self, truthValueDict):
        valueList = []
        opList = []
        for i in self.wff:
            if i.isalpha():
                valueList.append(truthValueDict[i])
            elif i == ')':
                op = WFF.operator[opList.pop()]
                opList.pop()
                if op == not_:
                    valueList.append(op(valueList.pop()))
                else:
                    valueList.append(op(valueList.pop(-2), valueList.pop(-1)))
            else:
                opList.append(i)
        return valueList[0]


if __name__ == '__main__':
    wff = WFF(input())
    print()
    print(wff.wff)
    print(wff.pVars)
    print(wff.ptvDicts)
    print(wff.truthTable)