# Wap program to remove duplication in a given string till 
# there is no chance to remove any .
def remove(str):
    sta = []
    for words in str:
        if sta and words==sta[-1]:
            sta.pop()
        else:
            sta.append(words)
    return sta

str= 'leEeetcode'
res = ' '.join(str)
print(remove(str))
