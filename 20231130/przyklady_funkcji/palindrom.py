def palindrom(napis):
    for i in range (len (napis)):
        if napis[i] != napis[-i - 1]:
            return False
    return True


def main():
    while True:
        napis = input ('Podaj napis: ')
        if not napis:
            break
        if palindrom (napis):
            print (f'Napis "{napis}" jest palindromem')
        else:
            print (f'Napis "{napis}" nie jest palindromem')
        break


if __name__ == '__main__':
    main ()
