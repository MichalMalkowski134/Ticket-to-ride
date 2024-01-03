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
    Map[4][1] = "15_1"
    Map[4][6] = "9_2"
    Map[4][12] = "2_3"
    Map[5][0] = "12_3"
    Map[5][1] = "14_3"
    Map[5][2] = "3_2"
    Map[5][3] = "10_0"
    Map[5][4] = "1_0"
    Map[5][6] = "7_4"
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
def Translate_Map(map):
    x,y = map.shape
    new_map = []
    for i in range(x):
        new_row = []
        for j in range(y):
            tst = map[i][j]
            new_row.append([map[i][j],Check_Value([i,j],map[i][j])])
        new_map.append(new_row)
    return new_map
def Check_Value(state,value):
    if(value <100):
        match str(value)[0]:
            case "2":
                match str(value)[1]:
                    case "0":
                        if not (state[1] % 2):
                            return [[state[0], state[1] + 1], [state[0], state[1] - 1]]
                        else:
                            return [[state[0] + 1, state[1] + 1], [state[0] + 1, state[1] - 1]]
                    case "1":
                        #Jak są w boki to nieparzyste kolumny mają 0 i +1 przesunięcia w wierszach, w parzyste mają -1 i 00 w wierszach
                        if not (state[1] % 2):
                            return [[state[0] - 1, state[1] + 1], [state[0] + 1, state[1]]]
                        else:
                            return [[state[0], state[1] + 1], [state[0] + 1, state[1]]]
                    case "2":
                        if not(state[1] % 2):
                            return [[state[0], state[1] + 1], [state[0] - 1, state[1]]]
                        else:
                            return [[state[0]+1, state[1] + 1], [state[0] - 1, state[1]]]
                    case "3":
                        if not(state[1] % 2):
                            return [[state[0] - 1, state[1] + 1], [state[0] - 1, state[1] - 1]]
                        else:
                            return [[state[0], state[1] + 1], [state[0], state[1] - 1]]
                    case "4":
                        if not (state[1] % 2):
                            return [[state[0], state[1] - 1], [state[0] - 1, state[1]]]
                        else:
                            return [[state[0] + 1, state[1] - 1], [state[0] - 1, state[1]]]
                    case "5":
                        if not(state[1] % 2):
                            return [[state[0] - 1, state[1] - 1], [state[0] +1, state[1]]]
                        else:
                            return [[state[0], state[1] - 1], [state[0]+1, state[1]]]
            case "1":
                match str(value)[1]:
                    case "0":
                        if not(state[1] % 2):
                            return [[state[0] + 1, state[1]], [state[0], state[1] - 1]]
                        else:
                            return [[state[0] + 1, state[1]], [state[0]+1, state[1] - 1]]
                    case "1":
                        if not (state[1] % 2):
                            return [[state[0], state[1] + 1], [state[0] + 1, state[1]]]
                        else:
                            return [[state[0] + 1, state[1] + 1], [state[0] + 1, state[1]]]
                    case "2":
                        if not (state[1] % 2):
                            return [[state[0] -1, state[1] +1], [state[0], state[1] +1]]
                        else:
                            return [[state[0] , state[1] +1], [state[0] + 1, state[1] +1]]
                    case "3":
                        if not (state[1] % 2):
                            return [[state[0] -1, state[1] + 1], [state[0]-1, state[1]]]
                        else:
                            return [[state[0], state[1] +1 ], [state[0]-1, state[1]]]
                    case "4":
                        if not (state[1] % 2):
                            return [[state[0] , state[1]-1], [state[0]-1, state[1]]]
                        else:
                            return [[state[0] + 1, state[1]-1], [state[0]-1, state[1]]]
                    case "5":
                        if not (state[1] % 2):
                            return [[state[0]-1, state[1]-1], [state[0], state[1] - 1]]
                        else:
                            return [[state[0] , state[1] -1 ], [state[0] + 1, state[1] - 1]]
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
                match (str(value)[1]):
                    case "0":
                        if not (state[1] % 2):
                            return [[[state[0] - 1, state[1]-1], [state[0], state[1]+1]],
                                    [[state[0], state[1] - 1], [state[0]+1, state[1]]]]
                        else:
                            return [[[state[0], state[1]-1], [state[0]+1, state[1]+1]],
                                    [[state[0]+1, state[1] - 1], [state[0]+1, state[1]]]]
                    case "1":
                        if not (state[1] % 2):
                            return [[[state[0], state[1]-1], [state[0]-1, state[1]+1]],
                                    [[state[0] +1, state[1]], [state[0], state[1] + 1]]]
                        else:
                            return [[[state[0]+1, state[1]-1], [state[0], state[1]+1]],
                                    [[state[0] + 1, state[1]], [state[0]+1, state[1] + 1]]]
                    case "2":
                        if not (state[1] % 2):
                            return [[[state[0] - 1, state[1]], [state[0] + 1, state[1]]],
                                    [[state[0] - 1, state[1] +1], [state[0], state[1] +1]]]
                        else:
                            return [[[state[0] - 1, state[1]], [state[0] + 1, state[1]]],
                                    [[state[0] , state[1] +1], [state[0]+1, state[1] +1]]]
                    case "3":
                        if not (state[1] % 2):
                            return [[[state[0] - 1, state[1]-1], [state[0], state[1]+1]],
                                    [[state[0] - 1, state[1]], [state[0]-1, state[1] + 1]]]
                        else:
                            return [[[state[0], state[1]-1], [state[0]+1, state[1]+1]],
                                    [[state[0] - 1, state[1]], [state[0], state[1] + 1]]]
                    case "4":
                        if not (state[1] % 2):
                            return [[[state[0], state[1]-1], [state[0] - 1, state[1]+1]],
                                    [[state[0] - 1, state[1] - 1], [state[0]-1, state[1]]]]
                        else:
                            return [[[state[0]+1, state[1]-1], [state[0], state[1]+1]],
                                    [[state[0], state[1] - 1], [state[0]-1, state[1]]]]
                    case "5":
                        if not (state[1] % 2):
                            return [[[state[0] - 1, state[1]], [state[0] + 1, state[1]]],
                                    [[state[0]-1,state[1]-1],[state[0],state[1]-1]]]
                        else:
                            return [[[state[0] - 1, state[1]], [state[0] + 1, state[1]]],
                                    [[state[0], state[1] - 1], [state[0]+1, state[1] - 1]]]
            case "5":
                match (str(value)[1]):
                    case "0":
                        if not (state[1] % 2):
                            return [[[state[0] - 1, state[1] - 1], [state[0]-1, state[1] + 1]],
                                    [[state[0], state[1] - 1], [state[0] + 1, state[1]]]]
                        else:
                            return [[[state[0], state[1] - 1], [state[0], state[1] + 1]],
                                    [[state[0]+1, state[1] - 1], [state[0] + 1, state[1]]]]
                    case "1":
                        if not (state[1] % 2):
                            return [[[state[0]-1, state[1]], [state[0], state[1] - 1]],
                                    [[state[0] + 1, state[1]], [state[0], state[1] + 1]]]
                        else:
                            return [[[state[0], state[1] - 1], [state[0]+1, state[1] - 1]],
                                    [[state[0] + 1, state[1]], [state[0] + 1, state[1] + 1]]]
                    case "2":
                        if not (state[1] % 2):
                            return [[[state[0] - 1, state[1]-1], [state[0] + 1, state[1]]],
                                    [[state[0] - 1, state[1] + 1], [state[0], state[1] + 1]]]
                        else:
                            return [[[state[0], state[1]-1], [state[0] + 1, state[1]]],
                                    [[state[0], state[1] + 1], [state[0] + 1, state[1] + 1]]]
                    case "3":
                        if not (state[1] % 2):
                            return [[[state[0], state[1] - 1], [state[0], state[1] + 1]],
                                    [[state[0] - 1, state[1]], [state[0] - 1, state[1] + 1]]]
                        else:
                            return [[[state[0]+1, state[1] - 1], [state[0]+1, state[1] + 1]],
                                    [[state[0] - 1, state[1]], [state[0], state[1] + 1]]]
                    case "4":
                        if not (state[1] % 2):
                            return [[[state[0]+1, state[1]], [state[0], state[1] + 1]],
                                    [[state[0] - 1, state[1] - 1], [state[0] - 1, state[1]]]]
                        else:
                            return [[[state[0]+1, state[1]], [state[0]+1, state[1] + 1]],
                                    [[state[0], state[1] - 1], [state[0] - 1, state[1]]]]
                    case "5":
                        if not (state[1] % 2):
                            return [[[state[0] - 1, state[1]], [state[0], state[1]+1]],
                                    [[state[0] - 1, state[1] - 1], [state[0], state[1] - 1]]]
                        else:
                            return [[[state[0] - 1, state[1]], [state[0]+1, state[1]+1]],
                                    [[state[0], state[1] - 1], [state[0] + 1, state[1] - 1]]]
            case "6":
                match (str(value)[1]):
                    case "0":
                        if not (state[1] % 2):
                            return [[[state[0] - 1, state[1] - 1], [state[0] - 1, state[1] + 1]],
                                    [[state[0], state[1] - 1], [state[0], state[1] +1]]]
                        else:
                            return [[[state[0], state[1] - 1], [state[0], state[1] + 1]],
                                    [[state[0]+1, state[1] - 1], [state[0]+1, state[1] +1]]]
                    case "1":
                        if not (state[1] % 2):
                            return [[[state[0], state[1]-1], [state[0] -1, state[1]]],
                                    [[state[0] + 1, state[1]], [state[0]-1, state[1] + 1]]]
                        else:
                            return [[[state[0] +1, state[1]-1], [state[0] -1, state[1]]],
                                    [[state[0] + 1, state[1]], [state[0], state[1] + 1]]]
                    case "2":
                        if not (state[1] % 2):
                            return [[[state[0] - 1, state[1] - 1], [state[0] + 1, state[1]]],
                                    [[state[0] - 1, state[1]], [state[0], state[1] + 1]]]
                        else:
                            return [[[state[0], state[1] - 1], [state[0] + 1, state[1]]],
                                    [[state[0] - 1, state[1]], [state[0]+1, state[1] + 1]]]
            case "7":
                match (str(value)[1]):
                    case "0":
                        if not (state[1] % 2):
                            return [[[state[0] - 1, state[1] - 1], [state[0] + 1, state[1]]],
                                    [[state[0], state[1] - 1], [state[0], state[1]+1]]]
                        else:
                            return [[[state[0], state[1] - 1], [state[0] + 1, state[1]]],
                                    [[state[0]+1, state[1] - 1], [state[0]+1, state[1]+1]]]
                    case "1":
                        if not (state[1] % 2):
                            return [[[state[0], state[1] - 1], [state[0], state[1]+1]],
                                    [[state[0] + 1, state[1]], [state[0]-1, state[1] + 1]]]
                        else:
                            return [[[state[0]+1, state[1] - 1], [state[0]+1, state[1]+1]],
                                    [[state[0] + 1, state[1]], [state[0] , state[1] + 1]]]
                    case "2":
                        if not (state[1] % 2):
                            return [[[state[0] +1, state[1]], [state[0]-1, state[1]+1]],
                                    [[state[0], state[1] + 1], [state[0]-1, state[1]]]]
                        else:
                            return [[[state[0] +1, state[1]], [state[0], state[1]+1]],
                                    [[state[0]+1, state[1] + 1], [state[0]-1, state[1]]]]
                    case "3":
                        if not (state[1] % 2):
                            return [[[state[0]-1, state[1] - 1], [state[0]-1, state[1] + 1]],
                                    [[state[0] - 1, state[1]], [state[0], state[1] + 1]]]
                        else:
                            return [[[state[0], state[1] - 1], [state[0], state[1] + 1]],
                                    [[state[0] - 1, state[1]], [state[0]+1, state[1] + 1]]]
                    case "4":
                        if not (state[1] % 2):
                            return [[[state[0], state[1]-1], [state[0]-1, state[1]]],
                                    [[state[0] - 1, state[1] - 1], [state[0] - 1, state[1]+1]]]
                        else:
                            return [[[state[0]+1, state[1]-1], [state[0]-1, state[1]]],
                                    [[state[0], state[1] - 1], [state[0], state[1]+1]]]
                    case "5":
                        if not (state[1] % 2):
                            return [[[state[0] +1, state[1]], [state[0]-1, state[1] - 1]],
                                    [[state[0], state[1] - 1], [state[0]-1, state[1]]]]
                        else:
                            return [[[state[0] +1, state[1]], [state[0], state[1] - 1]],
                                    [[state[0]+1, state[1] - 1], [state[0]-1, state[1]]]]
            case "8":
                match (str(value)[1]):
                    case "0":
                        if not (state[1] % 2):
                            return [[[state[0] - 1, state[1] - 1], [state[0] + 1, state[1]]],
                                    [[state[0], state[1] -1], [state[0]-1, state[1] + 1]]]
                        else:
                            return [[[state[0], state[1] - 1], [state[0] + 1, state[1]]],
                                    [[state[0]+1, state[1] -1], [state[0], state[1] + 1]]]
                    case "1":
                        if not (state[1] % 2):
                            return [[[state[0]-1, state[1]], [state[0]+1, state[1]]],
                                    [[state[0], state[1]-1], [state[0], state[1] + 1]]]
                        else:
                            return [[[state[0]-1, state[1]], [state[0]+1, state[1]]],
                                    [[state[0]+1, state[1]-1], [state[0]+1, state[1] + 1]]]
                    case "2":
                        if not (state[1] % 2):
                            return [[[state[0]-1, state[1]-1], [state[0], state[1] + 1]],
                                    [[state[0]+1, state[1]], [state[0] - 1, state[1]+1]]]
                        else:
                            return [[[state[0], state[1]-1], [state[0]+1, state[1] + 1]],
                                    [[state[0]+1, state[1]], [state[0], state[1]+1]]]
                    case "3":
                        if not (state[1] % 2):
                            return [[[state[0], state[1] - 1], [state[0] - 1, state[1] + 1]],
                                    [[state[0] - 1, state[1]], [state[0], state[1] + 1]]]
                        else:
                            return [[[state[0]+1, state[1] - 1], [state[0], state[1] + 1]],
                                    [[state[0] - 1, state[1]], [state[0]+1, state[1] + 1]]]
                    case "4":
                        if not (state[1] % 2):
                            return [[[state[0]-1, state[1]], [state[0] + 1, state[1]]],
                                    [[state[0] - 1, state[1] - 1], [state[0] - 1, state[1] + 1]]]
                        else:
                            return [[[state[0]-1, state[1]], [state[0] + 1, state[1]]],
                                    [[state[0], state[1] - 1], [state[0], state[1] + 1]]]
                    case "5":
                        if not (state[1] % 2):
                            return [[[state[0] - 1, state[1]-1], [state[0], state[1] + 1]],
                                    [[state[0], state[1] - 1], [state[0] - 1, state[1]]]]
                        else:
                            return [[[state[0], state[1]-1], [state[0]+1, state[1] + 1]],
                                    [[state[0]+1, state[1] - 1], [state[0] - 1, state[1]]]]
            case "9":
                match (str(value)[1]):
                    case "0":
                        if not (state[1] % 2):
                            return [[[state[0] - 1, state[1] - 1], [state[0], state[1]+1]],
                                    [[state[0], state[1]+ 1], [state[0]-1, state[1] + 1]]]
                        else:
                            return [[[state[0], state[1] - 1], [state[0]+1, state[1]+1]],
                                    [[state[0]+1, state[1]+ 1], [state[0], state[1] + 1]]]
                    case "1":
                        if not (state[1] % 2):
                            return [[[state[0] - 1, state[1]], [state[0] + 1, state[1]]],
                                    [[state[0], state[1] - 1], [state[0]-1, state[1] + 1]]]
                        else:
                            return [[[state[0] - 1, state[1]], [state[0] + 1, state[1]]],
                                    [[state[0]+1, state[1] - 1], [state[0], state[1] + 1]]]
                    case "2":
                        if not (state[1] % 2):
                            return [[[state[0] - 1, state[1]], [state[0]+1, state[1]]],
                                    [[state[0] -1, state[1]-1], [state[0], state[1] + 1]]]
                        else:
                            return [[[state[0] - 1, state[1]], [state[0]+1, state[1]]],
                                    [[state[0] , state[1]-1], [state[0]+1, state[1] + 1]]]
    elif value <200:
        match str(value)[1]:
            # zrobić rozdział na 3 tory, bo są 3 różne
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
                    case "2":
                        if not (state[1] % 2):
                            return [[state[0] - 1, state[1]-1], [state[0], state[1]+1],
                                    [state[0]+1, state[1]]]
                        else:
                            return [[state[0], state[1]-1], [state[0]+1, state[1]+1],
                                    [state[0]+1, state[1]]]
                    case "3":
                        if not (state[1] % 2):
                            return [[state[0], state[1]-1], [state[0]-1 , state[1]+1],
                                    [state[0], state[1] +1]]
                        else:
                            return [[state[0]+1, state[1]-1], [state[0] , state[1]+1],
                                    [state[0]+1, state[1] +1]]
                    case "4":
                        if not (state[1] % 2):
                            return [[state[0] - 1, state[1]], [state[0] + 1, state[1]],
                                    [state[0]-1, state[1] + 1]]
                        else:
                            return [[state[0] - 1, state[1]], [state[0] + 1, state[1]],
                                    [state[0], state[1] + 1]]
                    case "5":
                        if not (state[1] % 2):
                            return [[state[0] - 1, state[1]-1], [state[0], state[1]+1],
                                    [state[0]-1, state[1]]]
                        else:
                            return [[state[0], state[1]-1], [state[0]+1, state[1]+1],
                                    [state[0]-1, state[1]]]
            case "1":
                match str(value)[2]:
                    case "0":
                        if not(state[1] % 2):
                            return [[state[0] - 1, state[1]], [state[0], state[1] + 1],
                                    [state[0], state[1] - 1]]
                        else:
                            return [[state[0], state[1] - 1], [state[0]+1, state[1] + 1], [state[0] + 1, state[1] - 1]]
                    case "1":
                        if not (state[1] % 2):
                            return [[state[0] + 1, state[1]], [state[0]-1, state[1] - 1],
                                    [state[0]-1, state[1]+ 1]]
                        else:
                            return [[state[0] + 1, state[1]], [state[0], state[1] - 1],
                                    [state[0], state[1]+ 1]]
            case "2":
                match str(value)[2]:
                    case "0":
                        if not(state[1] % 2):
                            return [[state[0] -1, state[1]-1], [state[0], state[1] - 1],
                                    [state[0]+1, state[1]]]
                        else:
                            return [[state[0] , state[1]-1], [state[0]+1, state[1] - 1],
                                    [state[0]+1, state[1]]]
                    case "1":
                        if not (state[1] % 2):
                            return [[state[0] + 1, state[1]], [state[0], state[1] + 1],
                                    [state[0], state[1] - 1]]
                        else:
                            return [[state[0], state[1] - 1], [state[0] + 1, state[1] + 1],
                                    [state[0] + 1, state[1] - 1]]
                    case "2":
                        if not (state[1] % 2):
                            return [[state[0] + 1, state[1]], [state[0], state[1] + 1],
                                    [state[0]-1, state[1] + 1]]
                        else:
                            return [[state[0] + 1, state[1]], [state[0]+1, state[1] + 1],
                                    [state[0], state[1] + 1]]
                    case "3":
                        if not(state[1] % 2):
                            return [[state[0] - 1, state[1]], [state[0]-1, state[1] + 1],
                                    [state[0], state[1] +1]]
                        else:
                            return [[state[0]-1, state[1]], [state[0] , state[1] + 1],
                                    [state[0] + 1, state[1] + 1]]
                    case "4":
                        if not (state[1] % 2):
                            return [[state[0] - 1, state[1]-1], [state[0] - 1, state[1]],
                                    [state[0]-1, state[1] + 1]]
                        else:
                            return [[state[0], state[1]-1], [state[0] - 1, state[1]],
                                    [state[0], state[1] + 1]]
                    case "5":
                        if not (state[1] % 2):
                            return [[state[0], state[1]-1], [state[0] - 1, state[1] - 1],
                                    [state[0]-1, state[1]]]
                        else:
                            return [[state[0]+1, state[1]-1], [state[0], state[1] - 1],
                                    [state[0]-1, state[1]]]
            case "3":
                match str(value)[2]:
                    case "0":
                        if not (state[1] % 2):
                            return [[state[0]-1, state[1] -1]]
                        else:
                            return [[state[0], state[1] - 1]]
                    case "1":
                        if not (state[1] % 2):
                            return [[state[0], state[1] - 1]]
                        else:
                            return [[state[0] + 1, state[1] - 1]]
                    case "2":
                        return [[state[0]+1,state[1]]]
                    case "3":
                        if not(state[1] % 2):
                            return [[state[0], state[1]+1]]
                        else:
                            return [[state[0]+1, state[1]+1]]
                    case "4":
                        if not (state[1] % 2):
                            return [[state[0]-1, state[1] + 1]]
                        else:
                            return [[state[0], state[1] + 1]]
                    case "5":
                        return [[state[0]-1, state[1]]]
            case "4":
                match str(value)[2]:
                    case "0":
                        if not (state[1] % 2):
                            return [[state[0] - 1, state[1]-1], [state[0], state[1] + 1],
                                    [state[0]-1, state[1] + 1]]
                        else:
                            return [[state[0], state[1]-1], [state[0]+1, state[1] + 1],
                                    [state[0], state[1] + 1]]
                    case "1":
                        if not (state[1] % 2):
                            return [[state[0] + 1, state[1]], [state[0], state[1] + 1],
                                    [state[0], state[1] - 1]]
                        else:
                            return [[state[0], state[1] - 1], [state[0] + 1, state[1] + 1],
                                    [state[0] + 1, state[1] - 1]]
                    case "2":
                        if not (state[1] % 2):
                            return [[state[0] - 1, state[1]], [state[0]+1, state[1]],
                                    [state[0]-1, state[1] - 1]]
                        else:
                            return [[state[0] - 1, state[1]], [state[0]+1, state[1]],
                                    [state[0], state[1] - 1]]
                    case "3":
                        if not (state[1] % 2):
                            return [[state[0] - 1, state[1]-1], [state[0] - 1, state[1] + 1],
                                    [state[0], state[1] + 1]]
                        else:
                            return [[state[0], state[1]-1], [state[0], state[1] + 1],
                                    [state[0] + 1, state[1] + 1]]
                    case "4":
                        if not (state[1] % 2):
                            return [[state[0], state[1]-1], [state[0]-1, state[1] + 1],
                                    [state[0]+1, state[1]]]
                        else:
                            return [[state[0]+1, state[1]-1], [state[0], state[1] + 1],
                                    [state[0]+1, state[1]]]
                    case "5":
                        if not (state[1] % 2):
                            return [[state[0] + 1, state[1]], [state[0]-1, state[1] ],
                                    [state[0], state[1] + 1]]
                        else:
                            return [[state[0] + 1, state[1]], [state[0]-1, state[1] ],
                                    [state[0]+1, state[1] + 1]]
            case "5":
                match str(value)[2]:
                    case "0":
                        if not (state[1] % 2):
                            return [[[state[0] - 1, state[1]-1], [state[0], state[1] - 1]],
                                    [[state[0]+1, state[1]],[state[0]-1, state[1]+1]]]
                        else:
                            return [[[state[0], state[1]-1], [state[0]+1, state[1] - 1]],
                                    [[state[0]+1, state[1]],[state[0], state[1]+1]]]
                    case "1":
                        if not (state[1] % 2):
                            return [[[state[0] , state[1] - 1], [state[0]+1, state[1]]],
                                    [[state[0] -1, state[1]], [state[0], state[1] + 1]]]
                        else:
                            return [[[state[0]+1 , state[1] - 1], [state[0]+1, state[1]]],
                                    [[state[0] -1, state[1]], [state[0]+1, state[1] + 1]]]
                    case "2":
                        if not (state[1] % 2):
                            return [[[state[0]-1, state[1] - 1], [state[0] - 1, state[1]+1]],
                                    [[state[0] + 1, state[1]], [state[0], state[1] + 1]]]
                        else:
                            return [[[state[0], state[1] - 1], [state[0], state[1]+1]],
                                    [[state[0] + 1, state[1]], [state[0]+1, state[1] + 1]]]
                    case "3":
                        if not (state[1] % 2):
                            return [[[state[0], state[1] - 1], [state[0] - 1, state[1]]],
                                    [[state[0]-1, state[1]+1], [state[0], state[1] + 1]]]
                        else:
                            return [[[state[0]+1, state[1] - 1], [state[0] - 1, state[1]]],
                                    [[state[0], state[1]+1], [state[0]+1, state[1] + 1]]]
                    case "4":
                        if not (state[1] % 2):
                            return [[[state[0] -1, state[1]-1], [state[0]+1, state[1]]],
                                    [[state[0]-1, state[1]],[state[0]-1, state[1] +1]]]
                        else:
                            return [[[state[0], state[1]-1], [state[0]+1, state[1]]],
                                    [[state[0]-1, state[1]],[state[0], state[1] + 1]]]
                    case "5":
                        if not (state[1] % 2):
                            return [[[state[0] - 1, state[1] - 1], [state[0] - 1, state[1]]],
                                    [[state[0], state[1]-1], [state[0], state[1] +  1]]]
                        else:
                            return [[[state[0] , state[1] - 1], [state[0] - 1, state[1]]],
                                    [[state[0]+1, state[1]-1], [state[0]+1, state[1] +  1]]]
            case"6":
                if not(state[1] %2):
                    return [[state[0]-1,state[1]-1],[state[0]-1,state[1]],[state[0]-1,state[1]+1],[state[0],state[1]+1],[state[0]+1,state[1]],[state[0],state[1]-1]]
                else:
                    return [[state[0],state[1]-1],[state[0]-1,state[1]],[state[0],state[1]+1],[state[0]+1,state[1]+1],[state[0]+1,state[1]],[state[0]+1,state[1]-1]]
            case "7":
                if not (state[1] % 2):
                    return [[state[0] - 1, state[1] - 1], [state[0] - 1, state[1]], [state[0] - 1, state[1] + 1],
                            [state[0], state[1] + 1], [state[0] + 1, state[1]], [state[0], state[1] - 1]]
                else:
                    return [[state[0], state[1] - 1], [state[0] - 1, state[1]], [state[0], state[1] + 1],
                            [state[0] + 1, state[1] + 1], [state[0] + 1, state[1]], [state[0] + 1, state[1] - 1]]
            case "8":
                if not (state[1] % 2):
                    return [[state[0] - 1, state[1] - 1], [state[0] - 1, state[1]], [state[0] - 1, state[1] + 1],
                            [state[0], state[1] + 1], [state[0] + 1, state[1]], [state[0], state[1] - 1]]
                else:
                    return [[state[0], state[1] - 1], [state[0] - 1, state[1]], [state[0], state[1] + 1],
                            [state[0] + 1, state[1] + 1], [state[0] + 1, state[1]], [state[0] + 1, state[1] - 1]]
            case "9":
                if not (state[1] % 2):
                    return [[state[0] - 1, state[1] - 1], [state[0] - 1, state[1]], [state[0] - 1, state[1] + 1],
                            [state[0], state[1] + 1], [state[0] + 1, state[1]], [state[0], state[1] - 1]]
                else:
                    return [[state[0], state[1] - 1], [state[0] - 1, state[1]], [state[0], state[1] + 1],
                            [state[0] + 1, state[1] + 1], [state[0] + 1, state[1]], [state[0] + 1, state[1] - 1]]
    else:
        match str(value)[1]:
            case "0":
                if not (state[1] % 2):
                    return [[state[0] - 1, state[1] - 1], [state[0] - 1, state[1]], [state[0] - 1, state[1] + 1],
                            [state[0], state[1] + 1], [state[0] + 1, state[1]], [state[0], state[1] - 1]]
                else:
                    return [[state[0], state[1] - 1], [state[0] - 1, state[1]], [state[0], state[1] + 1],
                            [state[0] + 1, state[1] + 1], [state[0] + 1, state[1]], [state[0] + 1, state[1] - 1]]
            case "1":
                if not (state[1] % 2):
                    return [[state[0] - 1, state[1] - 1], [state[0] - 1, state[1]], [state[0] - 1, state[1] + 1],
                            [state[0], state[1] + 1], [state[0] + 1, state[1]], [state[0], state[1] - 1]]
                else:
                    return [[state[0], state[1] - 1], [state[0] - 1, state[1]], [state[0], state[1] + 1],
                            [state[0] + 1, state[1] + 1], [state[0] + 1, state[1]], [state[0] + 1, state[1] - 1]]
            case "2":
                if not (state[1] % 2):
                    return [[state[0] - 1, state[1] - 1], [state[0] - 1, state[1]], [state[0] - 1, state[1] + 1],
                            [state[0], state[1] + 1], [state[0] + 1, state[1]], [state[0], state[1] - 1]]
                else:
                    return [[state[0], state[1] - 1], [state[0] - 1, state[1]], [state[0], state[1] + 1],
                            [state[0] + 1, state[1] + 1], [state[0] + 1, state[1]], [state[0] + 1, state[1] - 1]]
            case "3":
                if not (state[1] % 2):
                    return [[state[0] - 1, state[1] - 1], [state[0] - 1, state[1]], [state[0] - 1, state[1] + 1],
                            [state[0], state[1] + 1], [state[0] + 1, state[1]], [state[0], state[1] - 1]]
                else:
                    return [[state[0], state[1] - 1], [state[0] - 1, state[1]], [state[0], state[1] + 1],
                            [state[0] + 1, state[1] + 1], [state[0] + 1, state[1]], [state[0] + 1, state[1] - 1]]
    return []
def Handling_Complex_Neighbours(Map,neighbour,new_road,roads,new_neighbours,run,  neighValue):
    occurences = 0
    if (neighValue > 40):
        for sub in roads:
            occurences += sub.count(neighbour)
    if (neighValue < 40 and (new_road[-1] in new_neighbours[0] or new_road[-1] in new_neighbours[1])and not any(neighbour in sublist for sublist in roads)) or (
            ((neighValue < 100 and neighValue >= 40) or (neighValue >= 150 and neighValue < 160)) and (new_road[-1] in new_neighbours[0] or new_road [-1] in new_neighbours[1]) and occurences < 2) or (
            ((neighValue >= 100 and neighValue < 150) or neighValue >= 160) and (new_road[-1] in new_neighbours[0] or new_road[-1] in new_neighbours[1])):
        if(new_road[-1] in new_neighbours[0]):
            new_neighbours[0].remove(new_road[-1])
            del new_neighbours[1]
        elif(new_road[-1] in new_neighbours[1]):
            new_neighbours[1].remove(new_road[-1])
            del new_neighbours[0]
        if(run>0):
            new_road.insert(0,neighbour)
        else:
            new_road.append(neighbour)
        run+=1
        Collecting_Road(Map, new_neighbours, new_road, roads)

def Collecting_Road(Map,neighbours, new_road, roads):
    run = 0
    for neighbour in neighbours:
        if len(neighbour) >0 and (type(neighbour[0]) != int or type(neighbour[1]) != int):
            Collecting_Road(Map,neighbour,new_road, roads)
        else:
            neighValue = Map[neighbour[0],neighbour[1]]
            new_neighbours = Check_Value(neighbour,neighValue)
            if len(new_neighbours) >0 and type(new_neighbours[0][0]) != int:
                Handling_Complex_Neighbours(Map,neighbour,new_road,roads,new_neighbours,run,neighValue)
            else:
                occurences = 0
                if (neighValue > 40):
                    for sub in roads:
                        occurences += sub.count(neighbour)
                if (neighValue <40 and new_road[-1] in new_neighbours and not any(neighbour in sublist for sublist in roads)) or (((neighValue < 100 and neighValue >= 40) or (neighValue >=150 and neighValue <160)) and new_road[-1] in new_neighbours and occurences <2) or (((neighValue >= 100 and neighValue <150) or neighValue >=160) and new_road[-1] in new_neighbours ) :
                    new_neighbours.remove(new_road[-1])
                    if (run > 0):
                        new_road.insert(0, neighbour)
                    else:
                        new_road.append(neighbour)
                    run +=1
                    Collecting_Road(Map,new_neighbours,new_road, roads)
    return new_road
def Main_Algorithm(Map):
    roads = []
    test = Translate_Map(Map)
    test2 = test[0][1]
    num_of_rows, num_of_cols = Map.shape
    for i in range(num_of_rows):
        for j in range(num_of_cols):
            value = Map[i][j]
            occurences = 0
            if(value > 40):
                for sub in roads:
                    occurences += sub.count([i, j])
            if ((value != 0 and value < 40 and not any([i, j] in sublist for sublist in roads)) or (((value < 100 and value >= 40) or (value >=150 and value <160))and occurences <2)) or (value >= 100 and value <150) or value >=160:
                neighbours = Check_Value([i, j], value)
                new_road = []
                new_road.append([i, j])
                Collecting_Road(Map,neighbours,new_road, roads)
                # for neighbour in neighbours:
                #     previous_neighbour = [i,j]
                #     checked_states = [neighbour]
                #     flag = True
                #     while flag:
                #         if(len(checked_states) == 0):
                #             flag = False
                #         for checked_state in checked_states:
                #             if(checked_state in new_road):
                #                 break
                #             try:
                #                 value = Map[checked_state[0],checked_state[1]]
                #             except:
                #                 value = 0
                #
                #             new_neighbours = Check_Value([checked_state[0],checked_state[1]],value)
                #             if(neighbour not in new_road):
                #                 if (previous_neighbour in new_neighbours):
                #                     new_road.append(neighbour)
                #                     new_neighbours.remove(previous_neighbour)
                #                     checked_states = new_neighbours
                #
                #                     previous_neighbour = neighbour
                #                     neighbour = checked_state
                #                 else:
                #                     flag = False
                #             elif (neighbour in new_neighbours):
                #                 new_road.append(neighbour)
                #                 new_neighbours.remove(previous_neighbour)
                #                 checked_states = new_neighbours
                #
                #                 previous_neighbour = neighbour
                #                 neighbour = checked_state
                #             else:
                #                 flag = False

                if(len(new_road) >1 ):
                    roads.append(new_road)
    return roads
##Aktualnie używane są te translated
def Main_Algorithm_Translated_Map(Map):
    roads = []
    num_of_rows, num_of_cols = Map.shape
    Map = Translate_Map(Map)
    for i in range(num_of_rows):
        for j in range(num_of_cols):
            value, neighbours = Map[i][j]
            occurences = 0
            if(value > 40):
                for sub in roads:
                    occurences += sub.count([i, j])
            if ((value != 0 and value < 40 and not any([i, j] in sublist for sublist in roads)) or (((value < 100 and value >= 40) or (value >=150 and value <160))and occurences <2)) or (value >= 100 and value <150) or value >=160:
                new_road = []
                new_road.append([i, j])
                state = [i,j]
                Collecting_Road_Translated_Map(Map,neighbours,new_road, roads,state )
                # for neighbour in neighbours:
                #     previous_neighbour = [i,j]
                #     checked_states = [neighbour]
                #     flag = True
                #     while flag:
                #         if(len(checked_states) == 0):
                #             flag = False
                #         for checked_state in checked_states:
                #             if(checked_state in new_road):
                #                 break
                #             try:
                #                 value = Map[checked_state[0],checked_state[1]]
                #             except:
                #                 value = 0
                #
                #             new_neighbours = Check_Value([checked_state[0],checked_state[1]],value)
                #             if(neighbour not in new_road):
                #                 if (previous_neighbour in new_neighbours):
                #                     new_road.append(neighbour)
                #                     new_neighbours.remove(previous_neighbour)
                #                     checked_states = new_neighbours
                #
                #                     previous_neighbour = neighbour
                #                     neighbour = checked_state
                #                 else:
                #                     flag = False
                #             elif (neighbour in new_neighbours):
                #                 new_road.append(neighbour)
                #                 new_neighbours.remove(previous_neighbour)
                #                 checked_states = new_neighbours
                #
                #                 previous_neighbour = neighbour
                #                 neighbour = checked_state
                #             else:
                #                 flag = False

                if(len(new_road) >1 ):
                    roads.append(new_road)
    return roads

def Collecting_Road_Translated_Map(Map,neighbours, new_road, roads, state):
    for neighbour in neighbours:
        if len(neighbour) >0 and (type(neighbour[0]) != int or type(neighbour[1]) != int):
            Collecting_Road_Translated_Map(Map,neighbour,new_road, roads,state)
        elif neighbour[0] >= len(Map) or neighbour[1] >= len(Map[0]):
            return
        else:
            neighValue, new_neighbours= Map[neighbour[0]][neighbour[1]]
            if len(new_neighbours) >0 and  type(new_neighbours[0][0]) != int:
                Handling_Complex_Neighbours_Translated_Map(Map,neighbour,new_road,roads,new_neighbours,neighValue,state)
            else:
                occurences = 0
                if (neighValue > 40):
                    for sub in roads:
                        occurences += sub.count(neighbour)
                if (neighValue <40 and (new_road[-1] in new_neighbours or new_road[0] in new_neighbours) and not any(neighbour in sublist for sublist in roads)) or (((neighValue < 100 and neighValue >= 40) or (neighValue >=150 and neighValue <160)) and (new_road[-1] in new_neighbours or new_road[0] in new_neighbours) and occurences <2) or (((neighValue >= 100 and neighValue <150) or neighValue >=160) and (new_road[-1] in new_neighbours or new_road[0] in new_neighbours)):
                    if(new_road[-1] in new_neighbours):
                        new_neighbours.remove(new_road[-1])
                        new_road.append(neighbour)
                    elif new_road[0] in new_neighbours:
                        new_neighbours.remove(new_road[0])
                        new_road.insert(0, neighbour)
                    Collecting_Road_Translated_Map(Map,new_neighbours,new_road, roads,state)
    return new_road

def Handling_Complex_Neighbours_Translated_Map(Map,neighbour,new_road,roads,new_neighbours, neighValue, state):
    occurences =0
    if(len(new_neighbours) == 1):
        Additional_Translate(Map,neighbour,new_road,roads,new_neighbours[0], neighValue, state)
        return
    if(neighValue <40):
        print("AAAAA")
    if (neighValue > 40):
        for sub in roads:
            occurences += sub.count(neighbour)
    if ((neighValue < 100 and neighValue >= 40) or (neighValue >= 150 and neighValue < 160)) and occurences < 2:
        if(new_road[-1] in new_neighbours[0]):
            new_neighbours[0].remove(new_road[-1])
            del new_neighbours[1]
            x,y = new_road[-1]
            del Map[x][y][1][0]
            new_road.append(neighbour)
        elif (new_road[0] in new_neighbours[0] and len(new_neighbours) >1):
            new_neighbours[0].remove(new_road[0])
            del new_neighbours[1]
            x, y = new_road[0]
            del Map[x][y][1][0]
            new_road.insert(0, neighbour)
        elif(new_road[-1] in new_neighbours[1]):
            new_neighbours[1].remove(new_road[-1])
            del new_neighbours[0]
            x, y = new_road[-1]
            del Map[x][y][1][1]
            new_road.append(neighbour)
        elif (new_road[0] in new_neighbours[1]):
            new_neighbours[1].remove(new_road[0])
            del new_neighbours[0]
            x, y = new_road[0]
            del Map[x][y][1][1]
            new_road.insert(0, neighbour)
        Collecting_Road_Translated_Map(Map, new_neighbours, new_road, roads, state)
def Additional_Translate(Map,neighbour,new_road,roads,new_neighbours, neighValue, state):
    occurences = 0
    if (neighValue > 40):
        for sub in roads:
            occurences += sub.count(neighbour)
    if (neighValue <40 and (new_road[-1] in new_neighbours or new_road[0] in new_neighbours) and not any(neighbour in sublist for sublist in roads)) or (((neighValue < 100 and neighValue >= 40) or (neighValue >=150 and neighValue <160)) and (new_road[-1] in new_neighbours or new_road[0] in new_neighbours) and occurences <2) or (((neighValue >= 100 and neighValue <150) or neighValue >=160) and (new_road[-1] in new_neighbours or new_road[0] in new_neighbours)):
        if (new_road[-1] in new_neighbours):
            new_neighbours.remove(new_road[-1])
            new_road.append(neighbour)
        elif new_road[0] in new_neighbours:
            new_neighbours.remove(new_road[0])
            new_road.insert(0, neighbour)
        Collecting_Road_Translated_Map(Map, new_neighbours, new_road, roads, state)
#Map = Template_Map()
#roads = Main_Algorithm(Map)
#new_roads = Main_Algorithm_Translated_Map(Map)
#print(new_roads)
