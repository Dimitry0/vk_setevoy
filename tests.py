import asyncio
from netschoolapi import NetSchoolAPI
mes_text = ''

async def main():
    day = 1
    numbers_in_setevoy = {}
    global mes_text
    api = NetSchoolAPI("https://net-school.cap.ru/")
    await api.login(
        "ПетровД45",  # Логин
        "000000",  # Пароль
        "МБОУ Шемуршинская СОШ")  # Название школы
    diary = await api.diary()
    print(diary.schedule[0].lessons[0].assignments)
    print(diary.schedule[4].lessons[0].assignments)
 #   for j in range(len(diary.schedule[day].lessons)):
  #      if len(diary.schedule[day].lessons[j].assignments) == 0:
 #           w = f'{str(diary.schedule[day].lessons[j].number)}'
  #          r = f'{str(diary.schedule[day].lessons[j].subject)}'
   #         if w not in numbers_in_setevoy.keys():
  #              numbers_in_setevoy[int(w)] = r
   #         else:
   #             numbers_in_setevoy[int(w)] = r

  #      else:
  #          if diary.schedule[day].lessons[j].assignments[0].type == 'Домашнее задание':
  #              w = f'{str(diary.schedule[day].lessons[j].number)}'
  #              r = f'{str(diary.schedule[day].lessons[j].subject)}'
   #             s = f'{diary.schedule[i].lessons[j].assignments[0].content}'
   #             if w not in numbers_in_setevoy.keys():
   #                 numbers_in_setevoy[int(w)] = r, s
   #             else:
    #                numbers_in_setevoy[int(w)] = r, s
    #        else:
    #            w = f'{str(diary.schedule[day].lessons[j].number)}'
    #            r = f'{str(diary.schedule[day].lessons[j].subject)}'
     #           if w not in numbers_in_setevoy.keys():
    #                numbers_in_setevoy[int(w)] = r
    #            else:
     #               numbers_in_setevoy[int(w)] = r
  #  for i in range(len(diary.schedule)):
    #    mes_text = ''
    #    for j in range(len(diary.schedule[i].lessons)):
    #        if len(diary.schedule[i].lessons[j].assignments) == 0:
   #             w = f'{str(diary.schedule[i].lessons[j].number)} {str(diary.schedule[i].lessons[j].subject)}\n'
    ##            mes_text += w
    #        else:
     #           if diary.schedule[i].lessons[j].assignments[0].type == 'Домашнее задание':
    #                w = f'{str(diary.schedule[i].lessons[j].number)} {str(diary.schedule[i].lessons[j].subject)}  {diary.schedule[i].lessons[j].assignments[0].content}\n'
    #            else:
     #               w = f'{str(diary.schedule[i].lessons[j].number)} {str(diary.schedule[i].lessons[j].subject)}\n'
    #            mes_text += w
    for i in range(len(diary.schedule)):
        mes_text = ''
        for j in range(len(diary.schedule[i].lessons)):
            if len(diary.schedule[i].lessons[j].assignments) == 0:
                w = f'{str(diary.schedule[i].lessons[j].number)} {str(diary.schedule[i].lessons[j].subject)}\n'
                mes_text += w
            else:
                if diary.schedule[i].lessons[j].assignments == 1 and \
                        diary.schedule[i].lessons[j].assignments[0].mark is not None:
                    w = f'{str(diary.schedule[i].lessons[j].number)} {str(diary.schedule[i].lessons[j].subject)}  {diary.schedule[i].lessons[j].assignments[0].mark}\n'
                    mes_text += w
                else:
                    w = f'{str(diary.schedule[i].lessons[j].number)} {str(diary.schedule[i].lessons[j].subject)}  '
                    for k in range(len(diary.schedule[i].lessons[j].assignments)):
                        if diary.schedule[i].lessons[j].assignments[k].mark is not None:
                            w += f'{diary.schedule[i].lessons[j].assignments[k].mark} '
                    w += f'\n'
                    mes_text += w
        print(mes_text)
    s = (await api.overdue())[0]
  #  print(s.type, s.content)
   # print(s)
    await api.logout()

if __name__ == '__main__':
    asyncio.run(main())