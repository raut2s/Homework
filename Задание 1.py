class Matrix:

    type_of_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __init__(self, matrix_list_1, matrix_list_2):
        self.matrix_list_1 = matrix_list_1
        self.matrix_list_2 = matrix_list_2

    def __str__(self):
        return str('\n'.join([str('\t'.join([str(self.type_of_matrix[a][b]) for b in range(len(self.type_of_matrix[a]))])) for a in range(len(self.type_of_matrix))]))

    def __add__(self):
        for a in range(len(self.matrix_list_1)):
            for b in range(len(self.matrix_list_2[a])):
                self.type_of_matrix[a][b] = self.matrix_list_1[a][b] + \
                    self.matrix_list_2[a][b]
        return self.__str__()


print(Matrix([[9, 11, 13], [4, 1, 15], [33, 35, 44]], [[60, 102, 5], [1, 4, 32], [55, 12, 7]]).__add__())