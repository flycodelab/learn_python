class HasPrivate:
    def __init__(self):
        self.public = 'Public.'
        self.__private = 'Private.'

    def __print_from_in(self):
        print(__class__.__name__)

    def print_from_internal(self):
        self.__print_from_in()
        print(self.public)
        print(self.__private)

obj = HasPrivate()
obj.print_from_internal()
#obj.__print_from_in()
print(obj.public)
#print(obj.__private)

