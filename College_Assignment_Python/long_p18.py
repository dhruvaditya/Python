#2nd me * and last three !!! karna hai kisi v input string ka
def converter(string):
    ans = ""
    for index in range(n):

        if (index == 1):
            ans += '*'
        else:
            ans+=string[index]
    for i in range(n, n+3):
        ans += "!"

    return ans


string=input("Enter a string")
n=len(string)
print(converter(string))
