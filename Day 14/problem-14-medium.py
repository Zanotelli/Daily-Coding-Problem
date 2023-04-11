import random as rd

n_points = int(input("> "))
n_pass = 0

for i in range(n_points):
    if (rd.random() ** 2) + (rd.random() ** 2) <= 1:
        n_pass += 1

pi = 4 * (n_pass/n_points)

print("Pi: ", pi)
