import asyncio


async def add_numbers(a, b):
    print(f"Выполняется сложение {a} + {b}")
    await asyncio.sleep(2)
    result = a + b
    print(f"Результат сложения: {result}")


async def multiply_numbers(a, b):
    print(f"Выполняется умножение {a} * {b}")
    await asyncio.sleep(3)
    result = a * b
    print(f"Результат умножения: {result}")


async def divide_numbers(a, b):
    print(f"Выполняется деление {a} / {b}")
    await asyncio.sleep(1)
    result = a / b
    print(f"Результат деления: {result}")


loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(add_numbers(5, 10)),
    loop.create_task(multiply_numbers(7, 3)),
    loop.create_task(divide_numbers(15, 5))
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()