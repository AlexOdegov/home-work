def send_email(message, recipient, sender = 'university.help@gmail.com'):
        correct_domen = ('.com', '.ru', '.net')
        valid = recipient.endswith(correct_domen) == sender.endswith(correct_domen)
        if recipient.count('@') == 1 and sender.count('@') == 1:
            if valid is not True:
                print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        if sender == recipient:
            print('Нельзя отправить письмо самому себе')
        if sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

