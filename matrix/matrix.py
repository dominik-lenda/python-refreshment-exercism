class Matrix:
    def __init__(self, matrix_string: str):
        split_lines = matrix_string.splitlines()
        rows = [[int(j) for j in i.split()] for i in split_lines]
        self.rows_converted = rows

    def row(self, index):
        return self.rows_converted[index-1]

    def column(self, index):
        return [row[index-1] for row in self.rows_converted]