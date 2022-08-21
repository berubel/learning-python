class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, message):
        self.message = message


while True:
    try:
        x = int(input('Type a number between 0 and 100: '))
        print(x)
        if x > 100 or x < 0:
            raise InputError('The grade must be less than 100 and greater than 0.')
        break
    except ValueError:
        print('Invalid input. Type numbers only.')
    except InputError as ex:
        print(ex)
