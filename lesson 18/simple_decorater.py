def my_decorator(func):
    def wrapper():
        print("This code is executed first.")
        func()
        print("This code is executed last.")

    return wrapper


def say_whee():
    print("Whee!")


whee = my_decorator(say_whee)

if __name__ == '__main__':
    whee()
