def generate_acronym(input_phrase):
    word=input_phrase.split()
    acronym=""
    for i in word:
        acronym+=i[0].upper()
    return acronym;

phrase=input("Enter a sentence of which you wanna know acronym")
print(generate_acronym(phrase))
