"""
Напишите функцию, которая применит к списку чисел произвольную
пользовательскую функцию и вернет суммы элементов полученного списка.
"""


def calculate_sum(my_list):

    result = 0
    for i in range(len(my_list)):
        result += my_list[i]
    return result


print(calculate_sum([2, 5, 4, 2]))
