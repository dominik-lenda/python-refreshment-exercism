class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string


    def row(self, index):
        split_list = self.matrix_string.split("\n") if "\n" in self.matrix_string else self.matrix_string
        split_nested_list = [i.split() for i in split_list]   
        rows_integers = [[int(char) for char in chars] for chars in split_nested_list]
        return rows_integers[index-1]


    def column(self, index):
        split_list = self.matrix_string.split("\n") if "\n" in self.matrix_string else self.matrix_string
        split_nested_list = [i.split() for i in split_list]   
        rows_integers = [[int(char) for char in chars] for chars in split_nested_list]
        columns = [row[index-1] for row in rows_integers]
        return columns