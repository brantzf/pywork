try:
    with open('missing.txt', 'w') as data:
        print("It's...", file=data)
except IOError as err:
    print('File error: ' + str(err))
