from time import time

elapsed_time = time()

print(max([sum([int(str(i)[j]) for j in range(0, len(str(i)))]) for i in [a**b for a in range(1, 100) for b in range(1, 100)]]))

elapsed_time = time() - elapsed_time
print('Time: ' + str(elapsed_time))
