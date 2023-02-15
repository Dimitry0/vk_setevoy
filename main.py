# -*- coding: utf-8 -*-
# https://severecloud.github.io/vk-keyboard/
# https://github.com/gennadis/quiz-bot

import asyncio, json
from netschoolapi import NetSchoolAPI
import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from random import randint, choice
from db import UsersInfo as user
import time
import image_tests

days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение']


async def main():
    global mes_text
    vk_session = vk_api.VkApi(token='vk1.a.AjJlanzA_3OnjQ_Ner63JArx3hdiggcE9TjZ9CfHyi7tblK8RioX0wHoJ1wOIl6eAjeLhuW9f1qvlhUgvjsF2aXqCxoVYFEQ742Xahb1jRfJxGuIS0YbUu1Wqc3rG87oOQkjhL2ql2pRxqPDCEU61_Zt7Am9agm-AJunCRg1hUlXqLwf8wtFQsmlXJfcfXMApoUcRuAD_BmN5n58SOS1Lw')
    longpoll = VkBotLongPoll(vk_session, '217027205')
    vk = vk_session.get_api()
    api = NetSchoolAPI("https://net-school.cap.ru/")
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                text = event.message.text
                user_id = event.message.from_id
                if event.message.peer_id < 2000000000:
                    if not user.is_reg(user_id):
                        if text.lower() == "начать":
                            user.insert(user_id)
                            user.update_registration(user_id, 1)
                            mes_text = f"Введите логин\n"
                            mes_text += f"пароль\n"
                            mes_text += f"название школы\n"
                            vk.messages.send(user_id=user_id,
                                             random_id=get_random_id(),
                                             message=mes_text)

                    else:
                        if user.get_registration(user_id)[0] == 1:
                            user.update_registration(user_id, 2)
                            user.update_login(user_id, str(text))

                        elif user.get_registration(user_id)[0] == 2:
                            user.update_registration(user_id, 3)
                            user.update_password(user_id, str(text))

                        elif user.get_registration(user_id)[0] == 3:
                            user.update_name_of_school(user_id, str(text))

                            try:
                                await api.login(
                                                user.get_login(user_id),  # Логин
                                                user.get_password(user_id),  # Пароль
                                                user.get_name_of_school(user_id))  # Название школы
                                vk.messages.send(user_id=user_id,
                                                 random_id=get_random_id(),
                                                 message="вход выполнен")
                                diary = await api.diary()

                                for i in range(len(diary.schedule)):
                                    await image_tests.wer(i, diary)
                                    upload = vk_api.VkUpload(vk)
                                    photo = upload.photo_messages('img.png')
                                    owner_id = photo[0]['owner_id']
                                    photo_id = photo[0]['id']
                                    access_key = photo[0]['access_key']
                                    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
                                    vk.messages.send(peer_id=user_id, random_id=0, attachment=attachment)
                                user.update_registration(user_id, 4)
                                await api.logout()

                            except Exception:
                                print(11)
                                user.update_registration(user_id, 1)
                                user.update_login(user_id, '')
                                user.update_password(user_id, '')
                                user.update_name_of_school(user_id, '')
                                vk.messages.send(user_id=user_id,
                                                 random_id=get_random_id(),
                                                 message="вход не выполнен, неверные данные, введите еще раз")

                        elif text.lower() == '!расписание':
                            print(10)
                            try:
                                await api.login(
                                    user.get_login(user_id),  # Логин
                                      user.get_password(user_id),  # Пароль
                                    user.get_name_of_school(user_id))  # Название школы
                                vk.messages.send(user_id=user_id,
                                                 random_id=get_random_id(),
                                                 message="РАСПИСАНИЕ НА НЕДЕЛЮ:")

                                diary = await api.diary()
                                for i in range(len(diary.schedule)):
                                    await image_tests.wer(i, diary)
                                    upload = vk_api.VkUpload(vk)
                                    photo = upload.photo_messages('img.png')
                                    owner_id = photo[0]['owner_id']
                                    photo_id = photo[0]['id']
                                    access_key = photo[0]['access_key']
                                    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
                                    vk.messages.send(peer_id=user_id, random_id=0, attachment=attachment)

                            except requests.exceptions:
                                vk.messages.send(user_id=user_id,
                                                 random_id=get_random_id(),
                                                    message='сначала введите данные')
    except requests.exceptions.ReadTimeout:
        print("--------------- [ СЕТЕВАЯ ОШИБКА ] ---------------")
        print("Переподключение  к серверам...")
        time.sleep(3)


if __name__ == '__main__':
    asyncio.run(main())