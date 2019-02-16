with open('movie_quotes.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')

