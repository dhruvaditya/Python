# To write a program which return the no. of same character at same position between two strings



def matches(string1, string2):
    str1 = set(string1)  # set of characters of string1
    str2 = set(string2)  # set of characters of string2

    matched_characters = str1 & str2  # Here both of the strings are stored in matched_characters variable

    # printing the length of matched_characters variable and gives the numbers of matched characters
    print("Number of Matching String Characters are : " + str(len(matched_characters)))

s1=input("Enter first string")
s2=input("Enter second string")

print(matches(s1,s2))