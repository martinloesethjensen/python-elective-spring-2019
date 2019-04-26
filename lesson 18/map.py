import string

if __name__ == '__main__':
    items = string.ascii_lowercase
    all_capital = list(map(lambda x: x.upper(), items))
    print(all_capital)
