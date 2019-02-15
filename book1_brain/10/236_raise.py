try:
    raise Exception('예외를 일으킵니다')
except Exception as err:
    print('예외가 일어났습니다. {0}'.format(err))

