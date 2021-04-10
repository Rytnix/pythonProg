str = (input( ))

res = ""
j=0
for i in range(len(str)):
    if str[i] == ' ':
        if i==1:
            if str[j].isalpha():
                 res = res + str[j:i].title()
                 j=i
            else :
                res = res + str[j:i]
                j=i
        else:
            if str[j+1].isalpha():
                 res = res + str[j:i].title()
                 j=i
            else :
                res = res + str[j:i]
                j=i

    elif i == len(str)-1:
        if str[j+1].isalpha():
          res = res + str[j:i+1].title()
          j=i
        else :
            res = res + str[j:i+1]
            j=i

print(res)










