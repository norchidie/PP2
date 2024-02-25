import re
txt="Hello_World_pp2"
ans=""
res=re.split(r"[_]",txt)
for i in res:
    ans+=i.capitalize()
print(ans)