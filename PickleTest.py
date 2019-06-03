import pickle
#Short program to save a pickle into a file.
#The x values are always the same for all y-values!
import random

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]

y1 = [2, 3, 6, 9, 4, 7, 7, 4, 3, 1, 6, 8, 3, 9, 10, 12, 7, 3, 5, 12, 11, 15, 17, 10, 20, 25, 50, 19]

y_arr = [y1]

for j in range(0,5) :
    y = []
    for i in range(0,len(y1)) :
        y.append(random.randint(1,50))
    y_arr.append(y)
    

with open("xyvalues", "wb") as file :
    pickle.dump(x,file)
    pickle.dump(y_arr,file)

