import concurrent.futures
import os
import time


def square(n):
    result = 1
    start_time = time.time()
    pid = os.getpid()
    print(f"Process {pid} starting calculation for {n}")

    """주어진 숫자의 제곱을 계산합니다."""
    for i in range(1000):
        result = 1
        for i in range(1, n + 1):
            result *= i


    print(f"Process {pid} finished calculation for {n} in {time.time() - start_time} seconds")

    return pid

if __name__ == '__main__':
    start_time = time.time()
    numbers = range(0, 10**3)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        # map을 사용하여 각 숫자에 대해 'square' 함수를 병렬로 실행
        results = list(executor.map(square, numbers))
        print(f'Results: {set(results)}')

    print(f'ProcessPoolExecutor took: {time.time() - start_time} seconds')

# ...
# Process 2026 finished calculation for 748 in 0.1912829875946045 seconds
# Process 2026 starting calculation for 759
# Process 2025 finished calculation for 750 in 0.16740918159484863 seconds
# Process 2025 starting calculation for 760
# Process 2022 finished calculation for 751 in 0.1850879192352295 seconds
# Process 2022 starting calculation for 761
# Process 2023 finished calculation for 752 in 0.17101120948791504 seconds
# Process 2023 starting calculation for 762
# Process 2031 finished calculation for 753 in 0.18919610977172852 seconds
# Process 2031 starting calculation for 763
# Process 2028 finished calculation for 754 in 0.18654680252075195 seconds
# Process 2028 starting calculation for 764
# Process 2027 finished calculation for 755 in 0.18515610694885254 seconds
# Process 2029 finished calculation for 757 in 0.16410374641418457 seconds
# Process 2027 starting calculation for 765
# Process 2029 starting calculation for 766
# ...
# Results: {2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031}
# ProcessPoolExecutor took: 11.050187110900879 seconds