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
        '!': 5,
        '&': 4,
        '|': 3,
        '>': 2,
        '<': 2,
        '=': 1,
    }

    operator = {
        '!': not_,
        '&': and_,
        '|': or_,
        '>': imply,
        '<': back_imply,
        '=': iff,
    }

    def __init__(self, wff):
        self.wff = wff.replace(' ', '').replace('<->', '=').replace('->', '>').replace('<-', '<')
        self.postForm = self.postFormTransfer()
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

    # an alternative is itertools.product
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

    def postFormTransfer(self):
        postForm = []
        tmpList = []
        for i in self.wff:
            if i.isalpha():
                postForm.append(i)
            elif i == ')':
                while True:
                    op = tmpList.pop()
                    if op == '(':
                        break
                    else:
                        postForm.append(op)
            else:
                try:
                    while WFF.precedence[tmpList[-1]] >= WFF.precedence[i]:
                        postForm.append(tmpList.pop())
                    tmpList.append(i)
                except:
                    tmpList.append(i)
        while len(tmpList) > 0:
            postForm.append(tmpList.pop())
        return postForm
        
    def logicEval(self, truthValueDict):
        container = []
        for i in self.postForm:
            if i.isalpha():
                container.append(truthValueDict[i])
            else:
                op = WFF.operator[i]
                if i == '!':
                    container.append(op(container.pop()))
                else:
                    container.append(op(container.pop(-2), container.pop()))
        return container[0]


if __name__ == '__main__':
    wff = WFF(input())
    print()
    # print(wff.wff)
    # print(wff.postForm)
    # print(wff.pVars)
    # print(wff.ptvDicts)
    print(wff.truthTable)
