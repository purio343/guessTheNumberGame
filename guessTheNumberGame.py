import random

def guessTheNumber():
    while True:
        print('system: Begin the game')

        while True:
            try:
                minimum = int(input('system: Enter the minimum value\n'))
                maximum = int(input('system: Enter the maximum vaue\n'))
                if(minimum > maximum):
                    print('system: Minimum number is bigger than maximum number')
                    continue            
                break
            except ValueError:
                print('system: Enter a valid number')    
            
        numList = list(range(minimum, maximum + 1))
        randomNum = random.randint(minimum, maximum)

        while True:
            print(numList)
            try:
                num = int(input('system: Select the number from the list\n'))
            except ValueError:
                print('system: Enter a valid number')
                continue

            if(randomNum == num):
                print('system: You guessed the correct number')
                if not isReplay():
                    print('system: End the game')
                    return
                break
            else:
                print('system: The number you choice is ' + str(num))
                if num in numList:
                    numList.remove(num)
                    if not numList:
                        print("system: No more numbers left to choose from.")
                        return                    

def isReplay():
    while True:
        userRes = input('system: Would you like to play again?\n').lower()
        if userRes == 'y' or userRes == 'yes':
            return True
        elif userRes == 'n' or userRes == 'no':
            return False
        else:
            print('system: Enter "yes" or "no"')

guessTheNumber()