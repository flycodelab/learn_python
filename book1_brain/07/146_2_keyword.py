def print_personnel(name, position = 'staff', nationality = 'Korea'):
    print('name = {0}\nposition = {1}\nnationality = {2}'.format(name, position, nationality))

print_personnel(name = '박상현')
print_personnel(name = '박상현', nationality = 'ROK')
print_personnel(name = '박상현', position = '인턴')

