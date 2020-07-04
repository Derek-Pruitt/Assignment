







class Dragon():
    legs = 0
    power_scale = 0
    Num_of_wings = 0
    breath = ''
    origin = ''

    def info(self):
        msg = ("legs: {}\npower scale:{}\nnumber of wings: {}\nBreath weapon:{}\nOrigin:{}\n------------".format(self.legs,self.power_scale,self.Num_of_wings,self.breath,self.origin))
        print(msg)

class Red(Dragon):
    name = 'Red Dragon'
    legs = 6
    power_scale = 7
    Num_of_wings = 4
    breath = 'breaths fire'
    magic = 'can use telepathy'
    origin = 'Center of Earth'
    location = 'Dimension 23'

    def red(self):
        msg = ("Name: {}\nMagic: {}\nLocation: {}".format(self.name,self.magic,self.location))
        print(msg)
    


class Black(Dragon):
    name = 'Black Dragon'
    power_scale = 10
    breath = 'breaths acid'
    Power = 'They can really use magic, not just telepathy.'
    origin = 'Neptune'
    location = 'all dimensions'
    speech = 'Norwigin'

    def black(self):
        msg = ("Name: {}\nPower: {}\nLocation: {}\nSpeech: {}".format(self.name,self.Power,self.location,self.speech))
        print(msg)
    





if __name__=='__main__':
    D=Dragon()
    D.info()

    R=Red()
    R.red()
    R.info()

    B=Black()
    B.black()
    B.info()
