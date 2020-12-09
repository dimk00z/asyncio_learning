import time
import random
from threading import Thread


def random_delay():
    return random.random()*5


def random_countdown():
    return random.randrange(5)


def launch_rocket(delay, countdown, num):
    time.sleep(delay)
    for tick in reversed(range(countdown)):
        print(f"{tick+1}...")
        time.sleep(1)
    print(f'Rocket #{num+1} launched!')


def get_rockets():
    number = 10
    return [
        (random_delay(), random_countdown()) for _ in range(number)
    ]


def run_threads():
    threads = [
        Thread(target=launch_rocket, args=(d, c, num))
        for num, (d, c) in enumerate(get_rockets())
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def main():
    """
    docstring
    """
    # launch_rocket(2, 3)
    run_threads()


if __name__ == '__main__':
    main()
