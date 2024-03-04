import os
import time
import asyncio
import threading

#########################
# 한 요청에서의 병렬처리가 아닌, 여러 요청에 의한 처리 과정을 확인하고자 함
# 1. 동기적으로 처리
# 2. 비동기적으로 처리
###########################

# curl_sync.txt
# url = http://localhost:8001/03_eventloop/1
# url = http://localhost:8001/03_eventloop/2
# url = http://localhost:8001/03_eventloop/3


############## with sync
def test_eventloop_sync(idx: int):
    loop = asyncio.get_running_loop()
    print(f"Event loop: {loop}, id: {idx}")

    square_sync(10**3, idx=idx)

def square_sync(n, idx):
    result = 1
    start_time = time.time()
    pid = os.getpid()
    print(f"Process {pid} starting calculation for {n}")

    for i in range(1000):
        result = 1
        for j in range(1, n + 1):
            result *= j
            print(f"{pid}, {i*j}, id: {idx}, threading: {threading.get_ident()}")


    print(f"Process {pid} finished calculation for {n} in {time.time() - start_time} seconds")

    return pid


########### with async

async def test_eventloop_async(idx: int):
    loop = asyncio.get_running_loop()
    print(f"Event loop: {loop}, id: {idx}")

    await square_async(10**3, idx=idx)

async def square_async(n, idx):
    result = 1
    start_time = time.time()
    pid = os.getpid()
    print(f"Process {pid} starting calculation for {n}")
    await asyncio.sleep(3)

    for i in range(100):
        result = 1
        for j in range(1, n + 1):
            result *= j
            print(f"{pid}, {i*j}, id: {idx}, threading: {threading.get_ident()}")


    print(f"Process {pid} finished calculation for {n} in {time.time() - start_time} seconds")

    return pid
######## worker 2개
# Event loop: <uvloop.Loop running=True closed=False debug=False>, id: 2
# Event loop: <uvloop.Loop running=True closed=False debug=False>, id: 1
# Process 10745 starting calculation for 1000
# Process 10746 starting calculation for 1000
# Event loop: <uvloop.Loop running=True closed=False debug=False>, id: 3
# Process 10746 starting calculation for 1000
# 10746, 0, id: 1, threading: 8136761472
# 10746, 0, id: 1, threading: 8136761472
# 10746, 0, id: 1, threading: 8136761472
# 10746, 0, id: 1, threading: 8136761472
# 10746, 0, id: 1, threading: 8136761472
# 10746, 0, id: 1, threading: 8136761472
# 10745, 59994, id: 2, threading: 8136761472
# 10745, 60093, id: 2, threading: 8136761472
# 10745, 60192, id: 2, threading: 8136761472
# 10745, 60291, id: 2, threading: 8136761472
# 10745, 60390, id: 2, threading: 8136761472
# 10745, 60489, id: 2, threading: 8136761472
# 10745, 60588, id: 2, threading: 8136761472
# 10746, 46995, id: 3, threading: 8136761472
# 10746, 47060, id: 3, threading: 8136761472
# 10746, 47125, id: 3, threading: 8136761472
# 10746, 47190, id: 3, threading: 8136761472
# 10746, 47255, id: 3, threading: 8136761472
# 10746, 47320, id: 3, threading: 8136761472


# # 1
# Process 10746 finished calculation for 1000 in 3.7979447841644287 seconds
# # 2
# Process 10745 finished calculation for 1000 in 3.800737142562866 seconds
# # 3
# Process 10746 finished calculation for 1000 in 4.197996139526367 seconds

# await 를 하게되면 sleep 를 하는 동안 일단 3번까지 실행은 시킴
# threading id 가 같지만 실제로 같은 쓰레드는 아님
#
