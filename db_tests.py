import asyncio
from netschoolapi import NetSchoolAPI
import image_tests
s = []
async def q():
    api = NetSchoolAPI("https://net-school.cap.ru/")
    await api.login(
        "ПетровД45",  # Логин
        "000000",  # Пароль
        "МБОУ Шемуршинская СОШ")  # Название школы
    diary = await api.diary()
    for i in range(6):
        print( )
        print(await image_tests.wer(diary))
    await api.logout()
print(s)
if __name__ == '__main__':
    asyncio.run(q())