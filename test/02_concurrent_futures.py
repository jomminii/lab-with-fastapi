import concurrent.futures
import time

def square(n):
    """주어진 숫자의 제곱을 계산합니다."""
    print(f'Squaring {n}:')
    return n * n

if __name__ == '__main__':
    numbers = range(0, 10**6)


    start_time = time.time()
    # ProcessPoolExecutor를 사용하여 프로세스 풀 생성
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # map을 사용하여 각 숫자에 대해 'square' 함수를 병렬로 실행
        results = list(executor.map(square, numbers))

        print(f'Results: {results}')

    print(f'ProcessPoolExecutor: {time.time() - start_time}')

    start_time = time.time()
    # submit을 사용하여 각 작업을 개별적으로 제출하고 Future 객체를 관리하는 방법
    futures = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number in numbers:
            # 각 숫자에 대해 'square' 함수를 비동기적으로 실행하고, 결과를 나중에 수집하기 위해 Future 객체를 저장
            future = executor.submit(square, number)
            futures.append(future)

        # Future 객체의 결과를 수집
        for future in concurrent.futures.as_completed(futures):
            print(f'Result: {future.result()}')

    print(f'ProcessPoolExecutor with submit: {time.time() - start_time}')

# Squaring 1:
# Squaring 2:
# Squaring 3:
# Squaring 4:
# Squaring 5:
# Results: [1, 4, 9, 16, 25]

# Squaring 1:
# Squaring 2:
# Squaring 3:
# Squaring 4:
# Squaring 5:
# Result: 1
# Result: 4
# Result: 9
# Result: 16
# Result: 25