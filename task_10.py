def common_letter(string1, string2):

    words = set(string1.lower()) & set(string2.lower())

    print(*{i for i in words}, sep=(', '))

common_letter('house', 'computers')



