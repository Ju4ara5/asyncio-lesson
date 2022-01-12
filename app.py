##  функция:
#def multiply(a, b):
#    return a * b
#
#
##  генератор:
#def generator(a, b):
#    while True:
#        yield a * b  # при каждом вызове будет возвращать результат
#        a += 1
#
#
##  асинхронная функция (корутина. похожа на обект генератор)
##  при вызове async_function - функция:
##  при вызове async_function(a) - корутина:
#async def async_function(a):
#    while True:
#        await a
#        a += 1
#
#import asyncio
##  функция засыпания (тоже является обектом корутина)
##  отдает управление другим функциям на время (сек):
#asyncio.sleep(1)
#

import asyncio


async def count(counter):
    print(f'Количество записей в списке {len(counter)}')

    while True:
        #  делаем паузу на 0.001 сек перед выполнением следующей строки:
        await asyncio.sleep(1/1000)  # в это время будут выполнятся другие функции (задачи) программы
        counter.append(1)  # после паузы выполнится эта строка


async def print_every_one_sec(counter):
    while True:
        await asyncio.sleep(1)
        print(f'- 1 секунда прошла.'
              f'Количество записей в списке: {len(counter)}')


async def print_every_5_sec():
    while True:
        await asyncio.sleep(5)
        print(f'---- 5 секунд прошло.')


async def print_every_10_sec():
    while True:
        await asyncio.sleep(10)
        print(f'-------- 10 секунд прошло.')

#  теперь надо запланировать работу функций написаных выше
#  для этого из них надо сделать обекты-корутины


async def main():
    counter = list()

    c = count(counter)  # с - это уже корутина, и.т.д. ниже:
    p1 = print_every_one_sec(counter)
    p5 = print_every_5_sec()
    p10 = print_every_10_sec()

    #  теперь из корутин создаём задачи(таски), мы должны их запланировать с помощью:
    tasks = [asyncio.create_task(c),
             asyncio.create_task(p1),
             asyncio.create_task(p5),
             asyncio.create_task(p10)
             ]

    #  перебираем таски
    await asyncio.gather(*tasks)

#  теперь запускать будем с помощью:
asyncio.run(main())
