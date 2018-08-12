x = 10


def countdown(x):
    if x > 0:
        print('{}...'.format(x))
        countdown(x-1)
    else:
        print("Hello there")


if __name__ == '__main__':
    countdown(x)
