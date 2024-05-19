import time
import asyncio


async def cake_baking(time_sleep):
    print('Composition of cake ingredients')
    print(f"CakeBaking time is : {time.ctime()} ")
    await asyncio.sleep(time_sleep)
    print(f'selling cakes in {time.ctime()} seconds')


async def cake_baking2():
    print('Composition of cake ingredients')
    print(f"CakeBaking time is : {time.ctime()} ")
    await asyncio.sleep(5)
    print(f'selling cakes in {time.ctime()} seconds')


async def cake_baking3():
    print('Composition of cake ingredients')
    print(f"CakeBaking time is : {time.ctime()} ")
    await asyncio.sleep(5)
    print(f'selling cakes in {time.ctime()} seconds')

#new
async def cake_baking4():
    print('Composition of cake ingredients new')
    print(f"CakeBaking time is : {time.ctime()} ")
    await asyncio.sleep(5)
    print(f'selling cakes in {time.ctime()} seconds')


async def main():
    _a = []
    a = [cake_baking(1),cake_baking2(),cake_baking3(),cake_baking4()]
    for i in a:
        aw = asyncio.create_task(i)

        _a.append(aw)
    for i in _a:
        await i


asyncio.run(main())
