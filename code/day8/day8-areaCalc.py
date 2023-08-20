#To calculate number of cans of paint we need to paint the wall
import math 

def paint_calc(height, width, cover):
    num_cans = (height*width)/cover
    print(f"You'll need {math.ceil(num_cans)} of paint.") 

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w , cover=coverage)
