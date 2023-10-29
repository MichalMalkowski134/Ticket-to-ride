import numpy as np
def Template_Map():
    Map = np.zeros([11,18])
    Map[0][1] = "2_1"
    Map[1][1] = "3_1"
    Map[1][3] = "8_1"
    Map[1][5] = "2_1"
    Map[1][6] = "3_0"
    Map[1][11] = "13_2"
    Map[2][3] = "4_5"
    Map[2][4] = "3_2"
    Map[2][5] = "6_2"
    Map[2][11] = "3_1"
    Map[3][6] = "2_5"
    Map[3][11] = "2_2"
    Map[4][6] = "9_2"
    Map[4][13] = "2_3"
    Map[5][0] = "12_3"
    Map[5][2] = "3_2"
    Map[5][3] = "10_0"
    Map[5][4] = "1_0"
    Map[5][6] = "7_4"
    Map[5][1] = "1_1"
    Map[6][2] = "2_1"
    Map[6][7] = "2_2"
    Map[6][11] = "10_0"
    Map[6][12] = "3_2"
    Map[6][13] = "3_2"
    Map[7][3] = "12_1"
    Map[7][8] = "3_2"
    Map[7][9] = "2_5"
    Map[7][11] = "10_1"
    Map[7][14] = "3_2"
    Map[7][15] = "3_2"
    Map[8][1] = "13_3"
    Map[8][9] = "11_0"
    Map[9][2] = "9_0"
    Map[9][3] = "2_3"
    Map[9][4] = "2_0"
    return Map

def Check_Value(state,value):
    if(value <100):
        match str(value)[0]:
            case "2":
                match str(value)[1]:
                    case "1":
                        if not (state[1] % 2):
                            return [[state[0] - 1, state[1] + 1], [state[0] + 1, state[1]]]
                        else:
                                return [[state[0], state[1] + 1], [state[0] + 1, state[1]]]
                    case "0":
                        if not (state[1] % 2):
                            return [[state[0], state[1] + 1], [state[0], state[1] - 1]]
                        else:
                            return [[state[0] + 1, state[1] + 1], [state[0] + 1, state[1] - 1]]
                    case "2":
                        if not(state[1] % 2):
                            return [[state[0], state[1] + 1], [state[0], state[1]]]
                        else:
                            return [[state[0], state[1] + 1], [state[0] - 1, state[1]]]
                    case "3":
                        if not(state[1] % 2):
                            return [[state[0] - 1, state[1] + 1], [state[0] - 1, state[1] - 1]]
                        else:
                            return [[state[0], state[1] + 1], [state[0], state[1] - 1]]
                    case "5":
                        if not(state[1] % 2):
                            return [[state[0] - 1, state[1] - 1], [state[0] - 1, state[1]]]
                        else:
                            return [[state[0], state[1] - 1], [state[0]-1, state[1]]]
            case "1":
                match str(value)[1]:
                    case "1":
                        if not(state[1] % 2):
                            return [[state[0], state[1] + 1], [state[0] + 1, state[1]]]
                        else:
                            return [[state[0] + 1, state[1] + 1], [state[0] + 1, state[1]]]
                    case "0":
                        if not(state[1] % 2):
                            return [[state[0] + 1, state[1]], [state[0], state[1] - 1]]
                        else:
                            return [[state[0] + 1, state[1]], [state[0]+1, state[1] - 1]]
            case"3":
                match(str(value)[1]):
                    case "0":
                        if not(state[1] % 2):
                            return [[state[0],state[1]-1],[state[0]-1,state[1]+1]]
                        else:
                            return [[state[0]+1, state[1] - 1], [state[0], state[1] + 1]]
                    case "1":
                        return [[state[0]-1, state[1]], [state[0] + 1, state[1]]]
                    case "2":
                        if not(state[1] % 2):
                            return [[state[0]-1, state[1] - 1], [state[0], state[1] + 1]]
                        else:
                            return [[state[0], state[1] - 1], [state[0]+1, state[1] + 1]]
            case "4":
                #zrobić rozdział na 2 tory, bo są 2 różne
                match (str(value)[1]):
                    case "5":
                        return [[state[0]-1, state[1]], [state[0] + 1, state[1]]]
            case "6":
                match (str(value)[1]):
                    case"2":
                        if not(state[1] % 2):
                            return [[state[0]-1,state[1]-1],[state[0]+1,state[1]]]
                        else :
                            return [[state[0], state[1] - 1], [state[0] + 1, state[1]]]
            case "7":
                match (str(value)[1]):
                    case "4":
                        if not(state[1] % 2):
                            return [[state[0], state[1] - 1], [state[0] - 1, state[1]]]
                        else:
                            return [[state[0]+1, state[1] - 1], [state[0] - 1, state[1]]]
            case "8":
                match (str(value)[1]):
                    case "1":
                        if not(state[1] % 2):
                            return [[state[0], state[1] - 1], [state[0], state[1]+1]]
                        else:
                            return [[state[0] + 1, state[1] - 1], [state[0] + 1, state[1]+1]]
            case "9":
                match (str(value)[1]):
                    case "0":
                        if not(state[1] % 2):
                            return [[state[0]-1, state[1] - 1], [state[0], state[1] + 1]]
                        else:
                            return [[state[0], state[1] - 1], [state[0] + 1, state[1] + 1]]
                    case "2":
                        return [[state[0] - 1, state[1]], [state[0]+1, state[1]]]
    else:
        match str(value)[1]:
            case"0":
                match str(value)[2]:
                    case"0":
                        if not(state[1] % 2):
                            return [[state[0] - 1, state[1] - 1], [state[0]-1, state[1] + 1],[state[0],state[1]-1]]
                        else:
                            return [[state[0], state[1] - 1], [state[0], state[1] + 1],[state[0]+1,state[1]-1]]
                    case "1":
                        if not(state[1] % 2):
                            return [[state[0] - 1, state[1]], [state[0] + 1, state[1]],
                                    [state[0], state[1] - 1]]
                        else:
                            return [[state[0]-1, state[1] ], [state[0]+1, state[1] ], [state[0] + 1, state[1] - 1]]
            case "1":
                match str(value)[2]:
                    case "0":
                        if not(state[1] % 2):
                            return [[state[0] - 1, state[1]], [state[0], state[1] + 1],
                                    [state[0], state[1] - 1]]
                        else:
                            return [[state[0], state[1] - 1], [state[0]+1, state[1] + 1], [state[0] + 1, state[1] - 1]]
            case "2":
                match str(value)[2]:
                    case "1":
                        if not(state[1] % 2):
                            return [[state[0] + 1, state[1]], [state[0], state[1] + 1],
                                    [state[0], state[1] - 1]]
                        else:
                            return [[state[0], state[1] - 1], [state[0] + 1, state[1] + 1],
                                    [state[0] + 1, state[1] - 1]]
                    case "3":
                        if not(state[1] % 2):
                            return [[state[0] - 1, state[1]], [state[0]-1, state[1] + 1],
                                    [state[0], state[1] +1]]
                        else:
                            return [[state[0]-1, state[1]], [state[0] , state[1] + 1],
                                    [state[0] + 1, state[1] + 1]]
            case "3":
                match str(value)[2]:
                    case "2":
                        return [[state[0]+1,state[1]]]
                    case "3":
                        if not(state[1] % 2):
                            return [[state[0], state[1]+1]]
                        else:
                            return [[state[0]+1, state[1]+1]]
    return []

def Main_Algorithm(Map):
    roads = []
    num_of_rows, num_of_cols = Map.shape
    for i in range(num_of_rows):
        for j in range(num_of_cols):
            value = Map[i][j]
            if (value != 0 and [i, j] not in roads):
                neighbours = Check_Value([i, j], value)
                for neighbour in neighbours:
                    new_road  = []
                    new_road.append([i, j])
                    previous_neighbour = [i,j]
                    checked_states = [neighbour]
                    flag = True
                    while flag:
                        if(len(checked_states) == 0):
                            flag = False
                        for checked_state in checked_states:
                            if(checked_state in new_road):
                                break
                            try:
                                value = Map[checked_state[0],checked_state[1]]
                            except:
                                value = 0

                            new_neighbours = Check_Value([checked_state[0],checked_state[1]],value)
                            if (previous_neighbour in new_neighbours):
                                new_road.append(neighbour)
                                new_neighbours.remove(previous_neighbour)
                                checked_states = new_neighbours

                                previous_neighbour = checked_state
                            else:
                                flag = False
                    if(len(new_road) >1 ):
                        roads.append(new_road)
    return roads
Map = Template_Map()
roads = Main_Algorithm(Map)
print(roads)
