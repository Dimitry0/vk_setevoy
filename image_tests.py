from PIL import Image, ImageDraw, ImageFont
import asyncio
from netschoolapi import NetSchoolAPI
from operator import itemgetter

api = NetSchoolAPI("https://net-school.cap.ru/")


#day = 1


async def wer(day, diary):
  #  await api.login(
    #    "ПетровД45",  # Логин
    #    "000000",  # Пароль
  #      "МБОУ Шемуршинская СОШ")  # Название школы
    #diary = await api.diary()
    numbers = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
    image = Image.open("image13.png")
    font = ImageFont.truetype("arial.ttf", 23)
    font1 = ImageFont.truetype("arial.ttf", 14)
    lesson_font = ImageFont.truetype("arial.ttf", 16)
    homework_font = ImageFont.truetype("arial.ttf", 14)
    mark_font = ImageFont.truetype("arial.ttf", 30)
    drawer = ImageDraw.Draw(image)


    lessons_in_setevoy = {}
    homework_in_setevoy = {}
    mark_in_setevoy = {}

    # уроки
    for j in range(len(diary.schedule[day].lessons)):
        w = f'{str(diary.schedule[day].lessons[j].number)}'
        r = f'{str(diary.schedule[day].lessons[j].subject)}'
        if w not in lessons_in_setevoy.keys():
            lessons_in_setevoy[int(w)] = r
        else:
            lessons_in_setevoy[int(w)] = r
   # print(lessons_in_setevoy)

    # домашка
    for j in range(len(diary.schedule[day].lessons)):
        if len(diary.schedule[day].lessons[j].assignments) == 0:
            e = f'{str(diary.schedule[day].lessons[j].number)}'
            f = f''
            homework_in_setevoy[int(e)] = f
        else:
            if diary.schedule[day].lessons[j].assignments[0].type == 'Домашнее задание':
                e = f'{str(diary.schedule[day].lessons[j].number)}'
                f = f'{diary.schedule[day].lessons[j].assignments[0].content}'
            else:
                e = f'{str(diary.schedule[day].lessons[j].number)}'
                f = f''
            homework_in_setevoy[int(e)] = f

    # оценки

    for j in range(len(diary.schedule[day].lessons)):
        if len(diary.schedule[day].lessons[j].assignments) == 0:
            n = f'{str(diary.schedule[day].lessons[j].number)}'
            m = f''
            mark_in_setevoy[int(n)] = m
        else:
            if diary.schedule[day].lessons[j].assignments == 1 and \
                    diary.schedule[day].lessons[j].assignments[0].mark is not None:
                n = f'{str(diary.schedule[day].lessons[j].number)}'
                m = f'{diary.schedule[day].lessons[j].assignments[0].mark}'
                mark_in_setevoy[int(n)] = m
            else:
                n = f'{str(diary.schedule[day].lessons[j].number)}'
                m = ''
                for k in range(len(diary.schedule[day].lessons[j].assignments)):
                    if diary.schedule[day].lessons[j].assignments[k].mark is not None:
                        m += f'{diary.schedule[day].lessons[j].assignments[k].mark} '
                mark_in_setevoy[int(n)] = m

    # уроки
    for i in numbers.keys():
        if i not in lessons_in_setevoy.keys():
            lessons_in_setevoy[i] = ''

    # домашка
    for i in numbers.keys():
        if i not in homework_in_setevoy.keys():
            homework_in_setevoy[i] = ''

    # оценки
    for i in numbers.keys():
        if i not in mark_in_setevoy.keys():
            mark_in_setevoy[int(i)] = ''

    # сортировка словарей
    lessons_in_setevoy = sorted(lessons_in_setevoy.items())
    homework_in_setevoy = sorted(homework_in_setevoy.items())
    mark_in_setevoy = sorted(mark_in_setevoy.items())

    # уроки

    s = 41
    q = 38
    for j, i in lessons_in_setevoy:
        drawer.text((50, s), str(j), font=font, fill='black')
        s += 46
        if len(i) > 17:
            drawer.text((70, q), f'{i[0:17]}…', font=lesson_font, fill='#308aff')
        else:
            drawer.text((70, q), i[0:17], font=lesson_font, fill='#308aff')
        q += 46.5

    # домашка

    t = 38
    for j, i in homework_in_setevoy:
        if len(i) > 33:
            drawer.text((250, t), i[0:33], font=homework_font, fill='gray')
            drawer.text((250, t+18), i[33:60], font=homework_font, fill='gray')
        else:
            drawer.text((250, t), i, font=homework_font, fill='gray')
        t += 46.5

    # оценки

    p = 38
    for j, i in mark_in_setevoy:
        if len(i) > 2:
            drawer.text((508, p), i, font=mark_font, fill='#308aff')
        else:
            drawer.text((520, p), i, font=mark_font, fill='#308aff')

       # else:
         #   drawer.text((350, q), i, font=lesson_font, fill='#308aff')
        p += 46

    drawer.text((50, 8), "УРОК", font=font1, fill='gray')
    drawer.text((245, 8), "ДОМАШНЕЕ ЗАДАНИЕ", font=font1, fill='gray')
    drawer.text((495, 8), "ОЦЕНКА", font=font1, fill='gray')
    image.save('img.png')
    #image.show()


#if __name__ == '__main__':
 #   asyncio.run(wer(3))