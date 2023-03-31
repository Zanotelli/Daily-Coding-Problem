in_str = input("> ")
vec = sorted([int(i) for i in in_str.split(" ")])
filter_vec = []
[filter_vec.append(x) for x in vec if x not in filter_vec]
lower = 0
i = 0
while True:
    if vec[i] >= 0:
        if vec[i] == lower:
            lower += 1
        else:
            break
    i += 1
print(lower)