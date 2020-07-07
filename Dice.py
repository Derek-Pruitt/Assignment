
import random

        
class Dice():
    _Dice1 = random.randrange(1,20)
    __Dice2 = random.randrange(1,12)
    def useDice():
        D = input("Please select D12 or D20...\n   >")
        if D == 'D12':
            print('{}'.format(Dice.__Dice2))
            Dice.useDice()
        elif D == 'D20':
            print('{}'.format(Dice._Dice1))
            Dice.useDice()
        else:
            print('You did not select D12 or D20...\n')
            Dice.useDice();

if __name__ == '__main__':
    Dice.useDice()
