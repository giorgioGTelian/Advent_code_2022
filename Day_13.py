import json

def cmp(a, b):
    # 1: a < b
    # 0: a == b
    # -1: a > b
    
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return 1
        elif a == b:
            return 0
        else:
            return -1
    
    elif isinstance(a, list) and isinstance(b, list):
        for i in range(min(len(a), len(b))):
            k = cmp(a[i], b[i])
            if k == 1:
                return 1
            elif k == -1:
                return -1
        
        if len(a) < len(b):
            return 1
        elif len(a) > len(b):
            return -1
        else:
            assert len(a) == len(b)
            return 0
        
    elif isinstance(a, list) and isinstance(b, int):
        return cmp(a, [b])
    
    else:
        assert isinstance(a, int)
        assert isinstance(b, list)
        return cmp([a], b)

# S = 0
# Ps = IN.split("\n\n")
# for i, P in enumerate(Ps, 1):
#     a, b = P.split("\n")
#     a = json.loads(a)
#     b = json.loads(b)
    
#     if cmp(a, b) == 1:
#         print(a, b)
#         S = S + i
        
# print(S)

Ps2 = [
    [[2]],
    [[6]],
]
Ps = IN.split("\n\n")
for P in Ps:
    a, b = P.split("\n")
    a = json.loads(a)
    b = json.loads(b)
    Ps2.append(a)
    Ps2.append(b)
    
Ps3 = sorted(Ps2, key=ft.cmp_to_key(lambda a, b: -cmp(a, b)))

S = 1
for i, k in enumerate(Ps3, 1):
    if k == [[2]]:
        S *= i
    elif k == [[6]]:
        S *= i
        
print(S)
