st1=input("Input first string ")
st2=input("Input second string ")
print(set(st1.replace(" ","")).intersection(set(st2.replace(" ",""))))
