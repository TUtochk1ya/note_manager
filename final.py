
first_name = input("Введите имя пользователя: ")
last_name = input("Введите фамилию пользователя: ")
title1 = input("Введите заголовок заметки: ")
title2 = input("Введите основной текст заметки: ")
title3 = input("Введите комментарий к заметке: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки ('Не активна','В процессе', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'дд-мм-гг': ")
issue_date = input("Введите дату истечения заметки в формате 'дд-мм-гг': ")

user_name = f"{first_name} {last_name[:1:]}"
title = [title1, title2, title3]
temp_created_date = created_date[:5:]
temp_issue_date = issue_date[:5:]

note = [user_name,
        title,
        content,
        status,
        temp_created_date,
        temp_issue_date
    ]

print("\nИмя: ",(note[0]),
      "\nЗаметка: ",(note[1]),
      "\nОсновной текст: ",(note[2]),
      "\nСтатус: ",(note[3]),
      "\nДата начала: ",(note[4])[:5:],
      "\nДата конца: ",(note[5])[:5:]
      )
















