class Matrix(object):
    def __init__(self, matrix_string):
        self.matriz = []
        lines = matrix_string.split('\n')
        for line in lines:
            intmatriz = []
            tempmatriz = line.split(' ')
            for a in tempmatriz:
                intmatriz.append(int(a))
            self.matriz.append(intmatriz)
            del intmatriz

    def row(self, index):
        return self.matriz[index-1][0:]

    def column(self, index):
        templist = []
        for a in self.matriz:
            templist.append(a[index-1])
        return templist
