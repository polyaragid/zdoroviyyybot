import telebot
import webbrowser
import random

bot = telebot.TeleBot('7600957163:AAGPK2g6e4v8dAlPmecMDno8rrJDgl16hVU')

cats = ['https://w.forfun.com/fetch/2c/2c38ec7c72e3d0094f591d6f735a3b8e.jpeg',
        'https://webmg.ru/wp-content/uploads/2022/09/i-157-13.jpeg',
        'https://w-dog.ru/wallpapers/1/47/482986285242373/kot-rebenok-cvety.jpg',
        'https://yandex.ru/video/preview/664490842082205701',
        'https://krasivosti.pro/uploads/posts/2021-04/1617746538_14-p-koshka-oboi-nedovolnii-kot-15.jpg',
        'https://pic.rutubelist.ru/video/25/38/2538282190c105914d9f2fe7150f8844.jpg',
        'https://mykaleidoscope.ru/x/uploads/posts/2022-10/1666103650_24-mykaleidoscope-ru-p-kotiki-smeshnie-vkontakte-24.jpg',
        'https://koshka.top/uploads/posts/2021-11/1637783983_42-koshka-top-p-kotik-zhivotik-50.jpg',
        'https://sportishka.com/uploads/posts/2022-11/1667529368_34-sportishka-com-p-nakachennie-koti-vkontakte-35.jpg',
        'https://yt3.googleusercontent.com/ytc/AGIKgqNpev2H7i9eVxPCIPf2WPEe8A25g_z3SuXNXhzd=s900-c-k-c0x00ffffff-no-rj',
        'https://coolsen.ru/wp-content/uploads/2021/12/103-20211215_233921.jpg']


anecdote = ['''Идёт Колобок на всех ругается, а медведь говорит:
— Колобок-Колобок, ты чего ругаешься?
А колобок отвечает:
—Я не Колобок, я ёжик из парикмахерской''',
            '''— Доктор, к вам пришёл человек-невидимка.
— Скажите, что сейчас я не могу с ним увидеться''',
            '''Собака заходит на почту и просит отправить телеграмму. Сотрудник почты говорит: — Диктуйте!
Собака такая: — Гав, гав, гав, гав, гав, гав, гав, гав, гав.
Сотрудник почты записал, потом подсчитал и говорит: — У вас тут девять слов, а оплата за десять. Можете дописать ещё одно слово бесплатно.
Собака задумалась и отвечает: гав''',
            '''А у вас было такое, что вас просят не шуметь, а вы не можете, потому что вы камыш!''',
            '''Вышел  колобок из бани и говорит: "Блин, голову забыл помыть"''',
            '''Секрет похудения прост... Но секрет есть секрет!''',
            '''Римский легионер заходит в бар, показывает два пальца и говорит "пять кружек пива"''',
            '''Встретились две улитки. У одной из них нет на спине раковины.
– Ой, что с тобой случилось? — спрашивает улитка с раковиной.
Вторая отвечает ей шепотом:
– Я ушла из дома. Только не говори никому.''',
            '''Заходит Мистер Пропер в загс и спрашивает: "Ну и где у вас тут разводы?"''',
            '''А бармен говорит: "Мы путешественникам во времени не наливаем"
Путешественник во времени заходит в бар''']


@bot.message_handler(commands=['cat'])
def site(message):
    webbrowser.open(random.choice(cats))


@bot.message_handler(commands=['start'])
def main(message):
    if [message.from_user.last_name] == [None]:
        bot.send_message(message.chat.id, f'Привет, <u> {message.from_user.first_name} </u>! \nты попала в бот для тех,'
                                          f' кто любит осознанность, развитие, себя и котиков!! \n Welcome!  \n \n'
                                          f' Навигация: \n/cat - милый котик \n'
                                          f'/yoga - подборка занятий \n'
                                          f'/sport - подборка спортивных тренировок\n'
                                          f'/joke - самые угарные анекдоты', parse_mode='html')
    else:
        bot.send_message(message.chat.id, f'Привет, <u> {message.from_user.first_name} {message.from_user.last_name} '
                                          f'</u>! \nты попала в бот для тех,'
                                          f' кто любит осознанность, развитие, себя и котиков!! \n Welcome!  \n \n'
                                          f' Навигация: \n/cat - милый котик\n'
                                          f'/yoga - подборка занятий \n'
                                          f'/sport - подборка спортивных тренировок\n'
                                          f'/joke - самые угарные анекдоты', parse_mode='html')


@bot.message_handler(commands=['joke'])
def joke(message):
    bot.send_message(message.chat.id, f'<u>самый смешной в мире анекдот:</u> \n {random.choice(anecdote)}', parse_mode='html')


@bot.message_handler(commands=['yoga'])
def yoga(message):
    if [message.from_user.last_name] == [None]:
        bot.send_message(message.chat.id, f'{message.from_user.first_name}, держи подборку практик от редакции!\n '
                                          f'<u>Йога </u>- отличный способ улучшить выносливость, гибкость и'
                                          f' качество своего тела, почувствовать ясность ума.\n'
                                          f'  \n<em>утренняя йога </em> \nhttps://www.youtube.com/watch?v=NCSKTE6BPvk '
                                          f'\nhttps://www.youtube.com/watch?v=w9yo5dlAr30&list=PLsTxFmng5F0IE3CFSv5sNloFfbgm1xejp&index=1'
                                          f'\n \n<em>вечерняяя йога </em> \n'
                                          f'https://www.youtube.com/watch?v=AnNElgqBOdQ&list=PLsTxFmng5F0IZNMqQUDU4nKfY_hO7GltB&index=25 '
                                          f'https://www.youtube.com/watch?v=m62MFlPacpE&list=PLkyAHeBaWbgBUMK4fCOo9yYAYWNZsSpW2&index=4 '
                                          f'https://www.youtube.com/watch?v=E1JT1CKEOuA&list=PLkyAHeBaWbgBUMK4fCOo9yYAYWNZsSpW2&index=3 \n'
                                          f'\n<em>приятные практики </em> \n'
                                          f'\nhttps://www.youtube.com/watch?v=TJ8MVaZDJQ4'
                                          f'\nhttps://www.youtube.com/watch?app=desktop&v=3t_sGOPlHNs'
                                          f' (йога для спины) \n ', parse_mode='html')

    else:
        bot.send_message(message.chat.id, f'{message.from_user.first_name} {message.from_user.last_name}, держи подборку практик от редакции!\n '
                                          f'<u>Йога </u>- отличный способ улучшить выносливость, гибкость и'
                                          f' качество своего тела, почувствовать ясность ума.\n'
                                          f'  \n<em>утренняя йога </em> \nhttps://www.youtube.com/watch?v=NCSKTE6BPvk '
                                          f'\nhttps://www.youtube.com/watch?v=w9yo5dlAr30&list=PLsTxFmng5F0IE3CFSv5sNloFfbgm1xejp&index=1'
                                          f'\n \n<em>вечерняяя йога </em> \n'
                                          f'https://www.youtube.com/watch?v=AnNElgqBOdQ&list=PLsTxFmng5F0IZNMqQUDU4nKfY_hO7GltB&index=25 '
                                          f'https://www.youtube.com/watch?v=m62MFlPacpE&list=PLkyAHeBaWbgBUMK4fCOo9yYAYWNZsSpW2&index=4 '
                                          f'https://www.youtube.com/watch?v=E1JT1CKEOuA&list=PLkyAHeBaWbgBUMK4fCOo9yYAYWNZsSpW2&index=3 \n'
                                          f'\n<em>приятные практики </em> \n'
                                          f'\nhttps://www.youtube.com/watch?v=TJ8MVaZDJQ4'
                                          f'\nhttps://www.youtube.com/watch?app=desktop&v=3t_sGOPlHNs'
                                          f' (йога для спины) \n ', parse_mode='html')

@bot.message_handler(commands=['sport'])
def sport(message):
    if [message.from_user.last_name] == [None]:
        bot.send_message(message.chat.id, f'{message.from_user.first_name}, держи подборку спортивных тренировок от редакции! \n'
                                          f'\n https://www.youtube.com/watch?v=h8ctkfSx6R0&feature=youtu.be \n'
                                          f'\n https://www.youtube.com/watch?v=5yDqg5sAMlI&list=PLkyAHeBaWbgBUMK4fCOo9yYAYWNZsSpW2&index=19')
    else:
        bot.send_message(message.chat.id, f'{message.from_user.first_name}  {message.from_user.last_name}, держи подборку спортивных тренировок от редакции! \n'
                                          f'\n https://www.youtube.com/watch?v=h8ctkfSx6R0&feature=youtu.be'
                                          f'\n https://www.youtube.com/watch?v=5yDqg5sAMlI&list=PLkyAHeBaWbgBUMK4fCOo9yYAYWNZsSpW2&index=19')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'id':
        bot.send_message(message.chat.id, f' <u>Ваш id</u>: <b>{message.id}</b>', parse_mode='html')
    if ''.join(message.text.lower().split()) == 'username':
        bot.send_message(message.chat.id, f'<u>Ваш username</u>: <b>{message.from_user.username}</b>',
                         parse_mode='html')


bot.polling(none_stop=True)
