

user_name = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки ('Не активна','В процессе', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'дд-мм-гг': ")
issue_date = input("Введите дату истечения заметки в формате 'дд-мм-гг': ")

temp_created_date = created_date[:5:]
temp_issue_date = issue_date[:5:]

print("\nЗаместка создана:")
print("Имя пользователя:", user_name)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", temp_created_date)
print("Дата истечения заметки:", temp_issue_date)









