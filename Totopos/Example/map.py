__author__ = 'qunox'

def isittrue(item):

    if not len(item[0]) == item[1]:
        return False


dictSample = { 'a' : {'vector' : [1,3,5,1]},
               'b' : {'vector' : [1,3,5,6,1]},
               'c' : {'vector' : [1,3,5,1]}
            }

item_l = [[dictSample[item]['vector'], 4] for item in dictSample]
print item_l
l = list(map(isittrue , item_l))
print l