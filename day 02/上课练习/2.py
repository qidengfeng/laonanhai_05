"倒序输出hello，word"

strvar = "hello，word"
for i in range(len(strvar)):
    listvar=strvar[len(strvar)-1-i]
    print(listvar, end="")
# print(listvar,end="")