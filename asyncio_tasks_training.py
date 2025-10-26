import asyncio
import time
import socket


def check_ipv4(adress):
    
    print("Enter download target IP")
    
    usr_inpt = input(">> ")
    
    try:
        socket.inet_aton(adress)
        return True
    except socket.error:
        return False




async def something_needing_time():
    print("retrieving data...\n")
    
    await asyncio.sleep(2) #zählt ab 0! // 4 = 3 
    print("Data received 10 / 10")
    
    await asyncio.sleep(4)
    print("Data received 30 / 30")

    await asyncio.sleep(8)
    print("Data saved successfully 60 / 60\n")
    input("Press 'Enter' to close\n")


async def counter_mts(): ##corutine
    for x in range(0, 60, +1):
        await asyncio.sleep(0.2) #await = sprungpunkt
        print(x, "mts", end="\r")


async def task_section():
    mts = asyncio.create_task(counter_mts())
    download = asyncio.create_task(something_needing_time())

    await mts
    await download

asyncio.run(task_section())
#event loop ist intern


