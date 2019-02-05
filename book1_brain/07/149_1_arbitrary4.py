def print_args(*argv, argc):
    for i in range(argc):
        print(argv[i])

print_args('argv1', 'argv2', 'argv3', argc=3)
#print_args('argv1', 'argv2', 'argv3', 3)

