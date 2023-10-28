# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=','):
    list_group1 = group1.split(str(separator))
    list_group2 = group2.split(str(separator))
    return sorted(set(list_group1).intersection(list_group2))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, ','))
