class Matrix(object):
    def __init__(self, matrix_string):
        temp_rows = matrix_string.split('\n')
        self.rows = []
        for row in temp_rows:
            self.rows.append(row.split(' '))

    def row(self, index):
        return [ int(i) for i in self.rows[index-1] ]

    def column(self, index):
        return [ int(self.rows[i][index-1]) for i in range(len(self.rows)) ]

