def vowel_count(s): # time complexity - > O(n^2)
    s = s.lower()
    tup = ('a','e','i','o','u')
    strLength = len(s)
    count = 0
    items= dict()
    for char in tup:
        count = 0
        for i in range(0,strLength):
            if char == s[i]:
                count += 1
        if count != 0:
            items[char] = count
    return(items)
print(vowel_count('Elie'))

# Optimised solution
def vowel_count1(string):
    lower_s = string.lower()
    return {letter: lower_s.count(letter) for letter in lower_s if letter in 'aeiou'}
print(vowel_count1('Elie'))