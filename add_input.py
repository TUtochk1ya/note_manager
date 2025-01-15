

first_name = input("Введите имя пользователя: ")
last_name = input("Введите фамилию пользователя: ")
title1 = input("Введите заголовок заметки: ")
title2 = input("Введите основной текст заметки: ")
title3 = input("Введите комментарий к заметке: ")
#content = input("Введите описание заметки: ")
#status = input("Введите статус заметки ('Не активна','В процессе', 'Выполнена'): ")
#created_date = input("Введите дату создания заметки в формате 'дд-мм-гг': ")
#issue_date = input("Введите дату истечения заметки в формате 'дд-мм-гг': ")

user_name = f"{first_name} {last_name[:1:]}"
title = f"{title1}. {title2} ({title3})"
#temp_created_date = created_date[:5:]
#temp_issue_date = issue_date[:5:]

#print("\nЗаметка создана:")
print("Имя пользователя:", user_name)
print("Заголовок заметки:", title)
#print("Описание заметки:", content)
#print("Статус заметки:", status)
#print("Дата создания заметки:", temp_created_date)
#print("Дата истечения заметки:", temp_issue_date)





