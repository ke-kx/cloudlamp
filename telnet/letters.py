#!/bin/python

all = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
print(all)

set_all = set(all)
# print(set_all)

hints = [
    #a
    'Gb6mBHIJ',
    'HNga8GCY',
    'ICj2Rb5f',
    'JYfr06gj',
    # 'JYfrO6gj',

    #t
    'pQZO',


    'S9rK',
    'uit9',
    'vdus',
    'WMvi',
    'x1Wd',
    'yOxM',
    'Zhy1',

    # video
    'Vz5AX',
    '4VL5w',
    'PzA4L',
    'AFD'
]

set_reduced = set_all
for hint in hints:
    set_reduced = set_reduced.difference(hint)

result = list(set_reduced) #.sort()
result.sort()
print(result)

3lTl3llcle

#37c3TelneT
#37c3TelnET
#37c3TElneT
#37c3TElnET

#TelneT37c3
#TelnET37c3
#TElneT37c3
#TElnET37c3


