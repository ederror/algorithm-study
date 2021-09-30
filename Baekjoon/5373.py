# Baekjoon - 5373
import sys
from copy import deepcopy
input = sys.stdin.readline


def clockwise(face):
    tmp = deepcopy(face)
    for i in range(3):
        for j in range(3):
            tmp[j][2 - i] = face[i][j]
    
    for i in range(3):
        for j in range(3):
            face[i][j] = tmp[i][j]


def counter_clockwise(face):
    tmp = deepcopy(face)
    for i in range(3):
        for j in range(3):
            tmp[2-j][i] = face[i][j]

    for i in range(3):
        for j in range(3):
            face[i][j] = tmp[i][j]


surface_dict = { # 0 top, 1 front, 2 left, 3 back, 4 right, 5 bottom
    'U': [0, 1, 2, 3, 4, 5, [], []],
    'F': [1, 5, 2, 0, 4, 3, [4], [2]],
    'L': [2, 1, 5, 3, 0, 4, [1,2,2,5,5], [3]],
    'B': [3, 0, 2, 5, 4, 1, [2], [4]],
    'R': [4, 1, 0, 3, 5, 2, [3,4,4,5,5], [1]],
    'D': [5, 3, 2, 1, 4, 0, [2, 2], [4, 4]]
}


T = int(input())
for tc in range(T):
    side = [[['w','w','w'] for __ in range(3)],
            [['r','r','r'] for __ in range(3)],
            [['g','g','g'] for __ in range(3)],
            [['o','o','o'] for __ in range(3)],
            [['b','b','b'] for __ in range(3)],
            [['y','y','y'] for __ in range(3)]
    ]
    n = int(input())
    instructions = input().split()
    for inst in instructions:
        cube = [side[i] for i in surface_dict[inst[0]][:6]]
        for f in surface_dict[inst[0]][6]:
            clockwise(cube[f])
        for f in surface_dict[inst[0]][7]:
            counter_clockwise(cube[f])
            
        if inst[1] == '+':
            clockwise(cube[0])
            tmp = [cube[4][2][0], cube[4][1][0], cube[4][0][0]]
            cube[4][2][0], cube[4][1][0], cube[4][0][0] = cube[3][2][2], cube[3][2][1], cube[3][2][0]
            cube[3][2][2], cube[3][2][1], cube[3][2][0] = cube[2][0][2], cube[2][1][2], cube[2][2][2]
            cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[1][0][0], cube[1][0][1], cube[1][0][2]
            cube[1][0][0], cube[1][0][1], cube[1][0][2] = tmp[0], tmp[1], tmp[2]
        else:
            counter_clockwise(cube[0])
            tmp = [cube[1][0][0], cube[1][0][1], cube[1][0][2]]
            cube[1][0][0], cube[1][0][1], cube[1][0][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2]
            cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[3][2][2], cube[3][2][1], cube[3][2][0]
            cube[3][2][2], cube[3][2][1], cube[3][2][0] = cube[4][2][0], cube[4][1][0], cube[4][0][0]
            cube[4][2][0], cube[4][1][0], cube[4][0][0] = tmp[0], tmp[1], tmp[2]

        for f in surface_dict[inst[0]][6]:
            counter_clockwise(cube[f])
        for f in surface_dict[inst[0]][7]:
            clockwise(cube[f])

    for row in side[0]:
        print("".join(row))