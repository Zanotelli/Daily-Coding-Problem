# Problema do dia 28/03/2023
def check_sum(list, k):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if (list[i] + list[j]) == k:
                return True
    return False

int_list = []
print("Input number separated by \"ENTER\" (write anythong else to stop):")
while True:
    try:
        int_list.append(int(input("> ")))
    except:
        break

print("\nInput number k: ")
try:
    k = int(input("> "))
except:
    raise Exception("Wrong input!")

print("\nDoes it pass? ", check_sum(int_list, k))