vowels = ['a', 'e', 'i', 'o', 'u']
inp = input("Enter alphabet: ")
for i in vowels:
    if i == inp:
        print("Entered alphabet is a vowel")
        exit(0)
print("Entered alphabet is a consonant")
