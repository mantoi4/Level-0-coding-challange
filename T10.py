def common_characters():
    string1 = 'house'
    string2 = 'computers'

    s1 = set(string1)
    s2 = set(string2)

    common_characters = s1 & s2

    print(s1 & s2)

common_characters()