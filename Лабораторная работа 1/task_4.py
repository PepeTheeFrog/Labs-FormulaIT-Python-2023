users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статистикой посещений
visits = {
    'Общее количество': 0,
    'Уникальные посещения': 0
}
visits['Общее количество'] = len(users)
visits['Уникальные посещения'] = len(set(users))
print(visits)
