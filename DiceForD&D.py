
import random

        
class Dice():
    _Dice20 = random.randrange(1,21)
    __Dice12 = random.randrange(1,13)
    Dice100 = random.randrange(1,101)
    Dice10 = random.randrange(1,11)
    Dice8 = random.randrange(1,9)
    Dice6 = random.randrange(1,7)
    Dice4 = random.randrange(1,5)
    Dice3 = random.randrange(1,4)
    def useDice():
            D = input("Please select D100, D20, D12, D10, D8, D6, D4, D3...\n   >")
            if D == 'D12':
                print('{}'.format(Dice.__Dice12))
                Dice.useDice()
            elif D == 'D20':
                print('{}'.format(Dice._Dice20))
                Dice.useDice()
            elif D == 'D100':
                print('{}'.format(Dice.Dice100))
                Dice.useDice()
            elif D == 'D10':
                print('{}'.format(Dice.Dice10))
                Dice.useDice()
            elif D == 'D8':
                print('{}'.format(Dice.Dice8))
                Dice.useDice()
            elif D == 'D6':
                print('{}'.format(Dice.Dice6))
                Dice.useDice()
            elif D == 'D4':
                print('{}'.format(Dice.Dice4))
                Dice.useDice()
            elif D == 'D3':
                print('{}'.format(Dice.Dice3))
                Dice.useDice()
            else:
                print('You did not select a D100, D20, D12, D10, D8, D6, D4, D3\n')
                YorN = input('Use again? Y/N\n')
                if YorN == 'Y':
                    Dice.useDice()
                else:
                    quit()
                


if __name__ == '__main__':
    Dice.useDice()
