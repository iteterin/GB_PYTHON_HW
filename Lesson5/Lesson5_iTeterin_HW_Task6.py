# 6. Сформировать (не программно) текстовый файл. В нём
# каждая строка должна описывать учебный предмет и наличие
# лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно,
# чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
# Так как разрешения использовать какие-либо сторонние библиотеки нет, не будем использовать re.split и прочие


def create_dic_from_file(filename):
    data_dict = dict()
    file_data = open(filename, "r", encoding='utf-8')
    content = file_data.readlines()
    # Пробегаем по каждой строчке
    for i in range(0, len(content)):
        # Создаем список для хранения значения нагрузки занятий
        lessons = list()
        # Переменная для хранения значения занятия в int
        dig_int = 0
        # Переменная для сбора числа перед пр, лаб и пр
        dig_str = ''
        # Перебираем строчку из файла по символьно и ищем цифру
        for j in list(content[i]):
            if j.isdigit():
                # Склеиваем цифру
                dig_str += str(j)
            # Если уже не цифра, а пробел, тогда переводим цифру
            # из str в int и добалвяем ее в список
            elif j.isspace():
                #try-except, потому что может быть несколько пробелов
                try:
                    dig_int = int(dig_str)
                    lessons.append(dig_int)
                except:
                    pass
                dig_str = ''
        # Добовляем в словарь предмет и сумму нагрузки
        data_dict[(content[i].split(':')[0])] = sum(lessons)
    print(data_dict)


def main():
    filename = './Lesson5/lesson5_Task6.txt'
    create_dic_from_file(filename)


if __name__ == '__main__':
    print("Задание №6")
    main()