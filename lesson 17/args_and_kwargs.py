"""
    Create an application that takes an arbitrary amount of comandline arguments
    (ie. python args_and_kwargs.py arg1 arg2 arg3 name='jens') and print them all to the console.
    Remember to test the edge cases.
"""


def args_and_kwargs(*args, **kwargs):
    for arg in args:
        print("{arg} is of type: {type}".format(arg=arg, type=type(arg)))

    for key, item in kwargs.items():
        print(f'{key} {item}')


if __name__ == '__main__':
    args_and_kwargs("arg1", "arg2", "arg3", name='jens')
