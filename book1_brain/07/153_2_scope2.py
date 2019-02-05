def scope_test():
    global a
    a = 1
    print('a: {0}'.format(a))

a = 0
scope_test()
print('a: {0}'.format(a))

