'''
Vytvoření tabulky sinusových hodnot po 30 stupních
sin(000°) = +0.00
sin(030°) = +0.50
sin(060°) = +0.87
sin(090°) = +1.00
sin(120°) = +0.87
sin(150°) = +0.50
sin(180°) = +0.00
sin(210°) = -0.50
sin(240°) = -0.87
sin(270°) = -1.00
sin(300°) = -0.87
sin(330°) = -0.50
sin(360°) = -0.00
'''
import math

for angle in range(0, 361, 30):
    sin_value = math.sin(math.radians(angle))
    if sin_value >=0:
        sign =  '+'
    else:
        sign = ''
    formated_angle = '{:03d}'.format(angle)
    sin_value_rounded = round(sin_value, 2)
    print(f"sin({formated_angle}°) = {sign}{sin_value_rounded:.2f}")