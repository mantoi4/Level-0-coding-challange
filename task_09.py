def vowels(string):

    string = str.lower(string)
    print(*{i for i in string if i in 'aeiou'}, sep=(','))

vowels("Umuzi")
