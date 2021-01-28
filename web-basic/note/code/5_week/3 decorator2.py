import time


def performance_clock(func):

    """ 함수의 퍼포먼스를 체크하는 함수 """

    def performance_clocked(*args):
        start_time = time.perf_counter()
        result = func(*args)
        end_time = time.perf_counter()
        print(f"Duration : {round(end_time - start_time, 8)}")
        return result

    return performance_clocked


if __name__ == "__main__":

    @performance_clock
    def time_func(second):
        time.sleep(second)

    @performance_clock
    def sum_func(*numbers):
        return sum(numbers)

    time_func(3)  # Duration : 3.00169363
    sum_func(1, 2, 3, 4, 5)  # Duration : 1.14e-05
    sum_func(1, 2, 3, 4, 5, 6, 7, 8, 9)  # Duration : 3.24e-06
