#To count no. of words in a sentence
def word_count(string):
    count=0
    word=len(string.split())
    return word

str=input("Enter the string of which you wanna count word")
print(word_count(str))