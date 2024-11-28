from random import randint
import numpy as np

class Matrica():
    def __init__(self):
        self.size = 0
        self.mat_1 = []
        self.mat_2 = []
        self.new_mat = []
        self.det = 0
        self.flag = 1
    
    def make_mat(self):
        self.size=int(input('введите размер матрицы\n'))
        self.mat_1 = self.mat_input()
        self.mat_2 = self.mat_input()
        self.new_mat = [ [0]*self.size for i in range(self.size)]
        self.flag = 2
    
    def sum_mat(self):
        if self.flag < 2:
            print ("ERROR")
            return 0
        self.new_mat = np.add(np.array(self.mat_1), np.array(self.mat_2))
        self.det = np.linalg.det(np.array(self.new_mat))
        self.flag = 3
    
    def mat_input(self):
        mat = [ [0]*self.size for i in range(self.size)]
        print('Вводите не числа, если хотите сгенерировать')
        for i in range(self.size):
            for j in range(self.size):
                s = input()
                if is_int(s):
                    mat[i][j] = int(s)
                else:
                    mat[i][j] = randint(-5,5) 
        return mat
    
    def mat_output(self):
        if self.flag < 3:
            print ("ERROR")
            return 0
        print(self.mat_1, self.mat_2, sep = '\n')
        print(self.new_mat, '\n', self.det)



def is_int(s):
    try:
        if type(s) is int:
            return True
        if s is None:
            return False
        if not s.isdecimal():
            return False
        int(s)
        return True
    except (Exception, ValueError, TypeError):
        return False


def valid_value(message_input: str, message_err: str, template: list):
    while True:
        ch = input(message_input, )
        if is_int(ch):
            ch = int(ch)
            if ch in template:
                return ch
        print(message_err)
        
def start_menu(message_input: str, message_err: str, template: dict):
    while True:
        ch = valid_value(message_input,
                         message_err,
                         list(template))
        f, is_break = template[ch]
        f()
        if is_break:
            break
    return False

def menu_main(mat):
    caption_start = "МЕНЮ\n1. Создать матрицы\n2. Выполнить алгоритм\n3. Вывести результат \n0. Выход\n"
    caption_err = "ERROR"
    menu_template = {
        0: (lambda: True, True),
        1: (mat.make_mat, False),
        2: (mat.sum_mat, False),
        3: (mat.mat_output, False)}
    start_menu(caption_start, caption_err, menu_template)
    
mat = Matrica()
if __name__ == "__main__":
    menu_main(mat)