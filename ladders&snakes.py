def check_position_ladder(position):
    ladder_lst = [1, 4, 8, 21, 28, 50, 80, 71]
    return position in ladder_lst

def check_postion_snake(position):
    snake_lst = [32, 36, 48, 62, 88, 95, 97]
    return position in snake_lst


def change_position_ladder(position):
    ladder_dict = {1:38, 4:14, 8:30, 21:42, 28:76, 50:67, 80:99, 71:92}
    position = ladder_dict[position]
    return position

def change_position_snake(position):
    snake_dict = {31:10, 36:6, 48:26, 62:18, 88:24, 95:56, 97:78}
    position = snake_dict[position]
    return position
