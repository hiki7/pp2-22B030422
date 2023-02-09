def solve(numheads, numlegs):
    for chicken in range(numheads + 1):
        rabbit = numheads - chicken 
        if chicken * 2 + rabbit * 4 == numlegs:
            return chicken, rabbit

numheads = 35
numlegs = 94
chicken, rabbit = solve(numheads, numlegs)
print("Num of chickens =", chicken)
print("Num of rabbits =", rabbit)
