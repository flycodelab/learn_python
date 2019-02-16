def print_team(**players):
    for k in players.keys():
        print('{0} = {1}'.format(k, players[k]))

print_team(카시야스='GK', 호날두='FW', 알론소='MF', 페페='DF')

