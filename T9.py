def vowel(string):
    vowels = "aeiouAEIOU"
    print([letter for letter in string if letter in vowels.lower()])
    
vowel("Umuzi")