class Matrica():
    def __init__(self):
        pass
    
    def make_mat(self):
        pass
    
    def sum_mat(self):
        pass
    
    def mat_output(self):
        pass



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