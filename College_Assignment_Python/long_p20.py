def check(str1,str2):
    n1=len(str1)
    n2=len(str2)

    if(n1!=n2):
        return "Strings length are not same"
    else:
        ans=""
        for i in range(n1):
            ans+=str1[i]

            ans+=str2[i]
    return ans


string1=input("Enter first string")
string2=input("Enter the second string")
print(check(string1,string2))