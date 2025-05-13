import numpy as np
import random as rand
import keyboard as keys


def generate(board_inuse):
    value_list = rand.choices([2, 4], weights=(90, 10), k=1)
    value = value_list[0]

    full_list = []
    #("board_inuse", board_inuse)
    for index, val in enumerate(np.nditer(board_inuse, order='C')):
        if int(val) != 0:
            full_list.append(index)

    if np.size(board_inuse) - len(full_list) == 0:
        global current
        print("You Lost")
        current = False

    else:
        full_set = set(full_list)
        #print("full", full_set)
        available_indices = [i for i in range(np.size(board_inuse)) if i not in full_set]
        comp_val = rand.choice(available_indices)

        row = comp_val // 4
        col = comp_val % 4
        position_coor = row, col
        #print(position_coor)

        board_inuse[position_coor] = value
        return board_inuse


def user_movement(key_pressed, board_inuse):
    update_board = np.zeros(16).reshape(4, 4)

    if key_pressed == "left":
        for index_outer, row in enumerate(board_inuse):
            temp = []

            for elem in row:
                elem = int(elem)
                if elem != 0:
                    temp.append(elem)
            if len(temp) > 1:
                deleted = 0
                for i in range(len(temp)):
                    if i < ((len(temp)-deleted)-1) and temp[i] == temp[i+1]:
                        temp[i] = temp[i] * 2
                        temp.pop(i+1)
                        deleted += 1
            for index, full_val in enumerate(temp):
                update_board[index_outer, index] = full_val


    if key_pressed == "right":
        for index_outer, row in enumerate(board_inuse):
            updated_row = row[::-1]

            temp = []
            for elem in updated_row:
                elem = int(elem)
                if elem != 0:
                    temp.append(elem)
            if len(temp) > 1:
                deleted = 0
                for i in range(len(temp)):
                    if i < ((len(temp)-deleted)-1) and temp[i] == temp[i+1]:
                        temp[i] = temp[i] * 2
                        temp.pop(i+1)
                        deleted += 1
            for index, full_val in enumerate(temp):
                update_board[index_outer, (3-index)] = full_val  
    
    if keys.is_pressed("up"):
        for index_outer, col in enumerate(np.transpose(board_inuse)):
            temp = []

            for elem in col:
                elem = int(elem)
                if elem != 0:
                    temp.append(elem)
            if len(temp) > 1:
                deleted = 0
                for i in range(len(temp)):
                    if i < ((len(temp)-deleted)-1) and temp[i] == temp[i+1]:
                        temp[i] = temp[i] * 2
                        temp.pop(i+1)
                        deleted += 1
            for index, full_val in enumerate(temp):
                update_board[index_outer, index] = full_val
            
        #print(update_board)
        update_board = np.transpose(update_board)
        #print(update_board)
            
    if keys.is_pressed("down"):
        for index_outer, col in enumerate(np.transpose(board_inuse)):
            updated_col = col[::-1]

            temp = []
            for elem in updated_col:
                elem = int(elem)
                if elem != 0:
                    temp.append(elem)
            if len(temp) > 1:
                deleted = 0
                for i in range(len(temp)):
                    if i < ((len(temp)-deleted)-1) and temp[i] == temp[i+1]:
                        temp[i] = temp[i] * 2
                        temp.pop(i+1)
                        deleted += 1
            for index, full_val in enumerate(temp):
                update_board[index_outer, (3-index)] = full_val  

        #print(update_board)
        update_board = np.transpose(update_board)
        #print(update_board)

    if key_pressed == "delete":
        global current
        current = False
        update_board = board_inuse
    
    return update_board



current = True
go_key = 0

init_board = np.zeros(16).reshape(4, 4)
current_board = generate(init_board)
print(current_board)
print("--------------------------------------")

while current == True:
    key_pressed = keys.read_key()

    if (key_pressed == "up" or key_pressed == "down" or key_pressed == "left" or key_pressed == "right" or key_pressed == "delete") and ((go_key%2) == 0):
        current_board = user_movement(key_pressed, current_board)
        current_board = generate(current_board)
        print(current_board)
        print("--------------------------------------")

    go_key += 1