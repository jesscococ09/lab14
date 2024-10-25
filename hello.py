color_list= [(227,66,52),(205,96,144),(28,134,238),(72,209,204),(237,145,33),(250,250,70),(245,50,245),(100,231,231)]
if color_list[7][0]>color_list[7][1] and color_list[7][0] > color_list[7][2]:
    print('The color is reddish')
elif color_list[7][1]>color_list[7][0] and color_list[7][1]>color_list[7][2]:
    print('The color is greenish')
elif color_list [7][0]==color_list [7][1]:
    print('The color is a shade of yellow')
elif color_list[7][0]==color_list [7][2]:
    print('The color is a shade of magenta')
elif color_list [7][1]==color_list[7][2]:
    print('The color is a shade of cyan')
else:
    print("The color is bluish")