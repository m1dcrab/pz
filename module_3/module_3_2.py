def send_email(messege, recipient, sender = "university.help@gmail.com"):
    error_id = 0
    if not(((sender.endswith(".ru") or sender.endswith(".com") or sender.endswith(".net")) and '@' in sender) and
((recipient.endswith(".ru") or recipient.endswith(".com") or recipient.endswith(".net")) and '@' in recipient)):
        error_id = 1

    elif sender == recipient:
        error_id = 2

    elif sender != "university.help@gmail.com":
        error_id = 3


    if error_id == 0:
        print('Письмо успешно отправлено с адреса',sender,'на адрес',recipient)
    elif error_id == 1:
        print("Невозможно отправить письмо с адреса", sender, 'на адрес', recipient)
    elif error_id == 2:
        print("Нельзя отправить письмо самому себе!")
    elif error_id == 3:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender = 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender = 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender = 'urban.teacher@mail.ru')
