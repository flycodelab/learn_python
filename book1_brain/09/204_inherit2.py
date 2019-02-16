class ArmorSuite:
    def armor(self):
        print("armored")

def get_armored(suite):
    suite.armor()

suite = ArmorSuite()
get_armored(suite)

class IronMan(ArmorSuite):
    pass

iron_man = IronMan()
get_armored(iron_man)

