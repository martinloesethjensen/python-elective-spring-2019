def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("This code is executed first.")
        func(*args, **kwargs)
        print("This code is executed last.")

    return wrapper


@my_decorator
def say_whee(name):
    print(f'Whee! {name}')


@my_decorator
def greet():
    print("Static method")


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def greet_twice(name):
    print(f'Hello {name}!')


if __name__ == '__main__':
    say_whee("Frank")
    greet()
    greet_twice("Bob")
