vowel="aeiou"
consonent="bcdnghjklmnpqrstvwxyz"
ans=""
inp="hello world"
for i in inp:
    if(i not in ans):
        ans+=i
print(ans)