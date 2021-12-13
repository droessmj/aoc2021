import sys
import matplotlib.pyplot as plt

def fold(points, fold):
    plane, loc = fold[0], fold[1]
    new_points = set()

    cur_height = max([p[1] for p in points])
    cur_length = max([p[0] for p in points])

    new_height = cur_height - loc
    new_length = cur_length - loc

    for point in points:
        new_point = ()
        if plane == 'y' and point[1] > loc:
            new_point = (point[0],abs(point[1] - loc - new_height)) # 0,13 -> 0,0 for y=7
        elif plane == 'x' and point[0] > loc:
            new_point = (abs(point[0] - loc - new_length),point[1])
        else:
            new_point = point

        new_points.add(new_point)

    return new_points


in_file = 'test'
if len(sys.argv) > 1:
    in_file = sys.argv[1]

points = []
folds = []
with open(f"./{in_file}.txt") as f:
    for line in f:
        line = line.strip()

        if ',' in line:
            point = line.split(',')
            points.append((int(point[0]),int(point[1])))
        elif '=' in line:
            parts = line.split(' ')
            fold_parts = parts[2].split('=')
            folds.append((fold_parts[0],int(fold_parts[1])))
            

new_points = fold(points, folds[0])
# part 1
# print(len(new_points))

# part 2
count = 0
for f in folds:
    print(f)
    points = fold(points, f)
    count+=1

X = [p[0] for p in points]
Y = [p[1] for p in points]

plt.scatter(X,Y)
plt.show()