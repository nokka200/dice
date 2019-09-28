# powerball
import random

def powerball():
    num1 = random.randrange(1, 60)
    num2 = random.randrange(1, 60)
    num3 = random.randrange(1, 60)
    num4 = random.randrange(1, 60)
    num6 = random.randrange(1, 60)
    num5 = random.randrange(1, 36)
    print("Today's numbers are " + str(num1)+", "+str(num2)+", "+str(num3)+", "+str(num6)+" and "+str(num4)+". The Powerball number is "
          +str(num5))

#powerball()

def roller():
    dice_list = []
    while True:
        dice = random.randint(1, 6)
        dice_list.append(dice)
        dice_list.sort()
        if len(dice_list) > 6:
            break
    return dice_list


print(roller())