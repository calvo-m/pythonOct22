# calculate length of string
str = "example"

def stringLength(string):
    count = 0
    i = 0
    for char in string:
        count += 1
    return count

#print(stringLength(str))

# count number of characters (my solution)
def countCharacters(string):
    for char1 in string:
        count = 0
        for char2 in string:
            if char1 == char2:
                count +=1
        print(char1, " ", count)

#countCharacters(str)

# count number of characters (given solution)
def char_freq(string):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
