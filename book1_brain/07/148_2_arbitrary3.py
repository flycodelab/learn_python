def print_args(argc, *argv):
    for i in range(argc):
        print(argv[i])

print_args(3, 'argv1', 'argv2', 'argv3')
#print_args(argc=3, 'argv1', 'argv2', 'argv3')

