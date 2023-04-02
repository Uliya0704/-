
random_number = input('Введите целые числа через пробел: ')
user_number = int(input('Введите любое число: '))

def is_int(str):
        str = str.replace(' ', '')
        try:
             int(str)
             return True
        except ValueError:
             return False


if " " not in random_number:
         print("\nОШИБКА!!!!ОТСУТСТВУЮТ ПРОБЕЛЫ.")
         random_number = input('Введите целые числа через пробел: ')
if not is_int(random_number):
        print('\n ОШИБКА ВВОДА ДАННЫХ!!!!! Только целые ЧИСЛА!!!!!)\n')

else:
        random_number = random_number.split()


list_random_number = [int(item) for item in random_number]

def merge_sort(L):
        if len(L) < 2:
            return L[:]
        else:
            middle = len(L) // 2
            left = merge_sort(L[:middle])
            right = merge_sort(L[middle:])
            return merge(left, right)

def merge(left, right):
        result = []
        t, y = 0, 0

        while t < len(left) and y < len(right):
            if left[t] < right[y]:
                result.append(left[t])
                t += 1
            else:
                result.append(right[y])
                y += 1

        while t < len(left):
            result.append(left[t])
            t += 1

        while y < len(right):
            result.append(right[y])
            y += 1
        return result

list_random_number = merge_sort(list_random_number)

def binary_search(array, element, left, right):
        try:
            if left > right:
                return False
            middle = (right + left) // 2
            if array[middle] == element:
                return middle
            elif element < array[middle]:
                return binary_search(array, element, left, middle - 1)
            else:
                return binary_search(array, element, middle + 1, right)
        except IndexError:
            return 'Число выходит за диапазон списка, введите меньшее число.'

print(f'Упорядоченный по возрастанию список: {list_random_number}')

if not binary_search(list_random_number, user_number, 0, len(list_random_number)):
        rI = min(list_random_number, key=lambda x: (abs(x - user_number), x))
        ind = list_random_number.index(rI)
        max_ind = ind + 1
        min_ind = ind - 1
        if rI < user_number:
            print(f'''Элемент отсутствует в списке
    Ближайший меньший элемент: {rI}, его индекс: {ind}
    Ближайший больший элемент: {list_random_number[max_ind]} его индекс: {max_ind}''')
        elif min_ind < 0:
            print(f'''Элемент отсутствует в списке
    Ближайший больший элемент: {rI}, его индекс: {list_random_number.index(rI)}
    В списке нет меньшего элемента''')
        elif rI > user_number:
            print(f'''Элемент отсутствует в списке
    Ближайший больший элемент: {rI}, его индекс: {list_random_number.index(rI)}
    Ближайший меньший элемент: {list_random_number[min_ind]} его индекс: {min_ind}''')
        elif list_random_number.index(rI) == 0:
            print(f'Индекс введенного элемента: {list_random_number.index(rI)}')
else:
        print(
            f'Индекс введенного элемента: {binary_search(list_random_number, user_number, 0, len(list_random_number))}')

