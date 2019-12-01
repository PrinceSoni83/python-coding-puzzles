#########################################################################
# first solution :                                                      #
# 1. sort both the string in lower case and remove the spaces if any    #
# 2. comparet the strings if they are equal                             #
# 3. if strings are equal they are anagarm                              #
#########################################################################


def anagram1(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

#########################################################################
# second solution :                                                      #
# 1. sort both the string in lower case and remove the spaces if any    #
# 2. comparet the strings if they are equal                             #
# 3. if strings are equal they are anagarm                              #
#########################################################################

def anagram2(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()


    return sorted(s1) == sorted(s2)


print(anagram2('dog','god '))
