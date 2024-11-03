# TODO Напишите функцию find_common_participants

def list_separating(participants, separator = ","):
    tuple_participants = []
    place = 0
    for i in range(len(participants)):
        if participants[i] == separator:
            tuple_participants.append(participants[place:i])
            place = i + 1
    tuple_participants.append(participants[place:(i + 2)])
    return tuple_participants

def find_common_participants(list1, list2, separator = ","):
    common_participants = []
    list1 = list_separating(list1, separator)
    list2 = list_separating(list2, separator)
    for i in range(len(list1)):
        for k in range(len(list1)):
            if list1[i] == list2[k]:
                common_participants.append(list1[i])
    common_participants.sort()
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print('Общие участники для обеих групп: ', find_common_participants(participants_first_group, participants_second_group, "|"))