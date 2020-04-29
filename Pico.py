def get_max(string):
    maxDepth = 0
    yuh = []
    for a in string:
        if a == "(":
            maxDepth += 1
            yuh.append(maxDepth)
        else:
            maxDepth -= 0
    return max(yuh)

def get_difference(x, y):
    return get_max(x) - get_max(y)

def combine(x, y):
    return x + y

def absorb_right(x,y):
    x = x[:-1]
    return x + y + ")"

def absorb_left(x,y):
    y = y[0:]
    return "(" + x + y

#print(get_difference("() + ((()))"))
string = input()
x, y = string.split()
dif = get_difference(x,y)

if dif == 0:
    print(combine(x, y))
elif dif < 0:
    print(absorb_left(x, y))
else:
    print(absorb_right(x, y))
#if get_difference(stringList)[1] > 0:
