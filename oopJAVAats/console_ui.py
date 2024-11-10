def view_data(data, title):
    print(f'{title} = {data}')


def get_value():
    return input()


def input_data():
    print('С какими числами будем работать? Введите 1 для работы с комплексными числами, 2 - для работы с рациональными числами')
    data_type = get_value()
    if data_type == '1':
        print('Введите первое число (напишите число ввиде комплексного числа a + bj ):')
        left_value = get_value()
        print('Введите второе число (напишите число ввиде комплексного числа a + bj) :')
        right_value = get_value()
        print('Выберите операцию:')
        oper = get_value()
    elif data_type == '2':
        print('Введите первое число (напишите число ввиде дробного числа a/b):')
        left_value = get_value()
        print('Введите второе число (напишите число ввиде дробного числа a/b):')
        right_value = get_value()
        print('Выберите операцию:')
        oper = get_value()
    return (data_type, left_value, oper, right_value)