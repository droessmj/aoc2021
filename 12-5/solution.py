
class Point:
    x = 0
    y = 0

    def __init__(self, point_string, x = None, y = None):
        if point_string: 
            pieces = point_string.split(',')
            self.x = int(pieces[0])
            self.y = int(pieces[1])
        elif x or y:
            self.x = x
            self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"[{self.x},{self.y}]"

    def __repr__(self):
        return f"[{self.x},{self.y}]"

    def  __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Line:
    point_one = None
    point_two = None
    is_vertical = False
    is_diagonal = False
    process_points = False

    def __init__(self, point_one, point_two):
        self.point_one = point_one
        self.point_two = point_two
        # determine if vertical or horizontal line
        if self.point_one.x == self.point_two.x:
            self.is_vertical = True
            self.process_points = True
        elif self.point_one.y == self.point_two.y:
            self.is_vertical = False
            self.process_points = True
        if self.is_vertical == False and self.point_one.y != self.point_two.y:
            self.is_diagonal = True
            # TODO: check for 45 degree diagonal before marking to process
            # diff x1 and x2 == diff y1 and y2?
            if abs(self.point_one.x - self.point_two.x) == abs(self.point_one.y - self.point_two.y):
                self.process_points = True

    # pretty sure my off by ones / dupes here won't matter due to hashing downstream
    def get_all_points(self):
        points = [self.point_one, self.point_two]
        if self.is_diagonal:
            idx = 0
            # up right
            if self.point_one.x < self.point_two.x and self.point_one.y < self.point_two.y:
                for x in range(self.point_one.x, self.point_two.x):
                    points.append(Point(None,x,self.point_one.y+idx))
                    idx+=1
            # down right
            elif self.point_one.x < self.point_two.x and self.point_one.y > self.point_two.y:
                for x in range(self.point_one.x, self.point_two.x):
                    points.append(Point(None,x,self.point_one.y-idx))
                    idx+=1
            # up left
            elif self.point_one.x > self.point_two.x and self.point_one.y < self.point_two.y:
                for x in range(self.point_two.x, self.point_one.x):
                    points.append(Point(None,x,self.point_two.y-idx))
                    idx+=1
            # down left
            else:
                for x in range(self.point_two.x, self.point_one.x):
                    points.append(Point(None,x,self.point_two.y+idx))
                    idx+=1
        elif self.is_vertical: # vertical -- x remains the same
            if self.point_one.y < self.point_two.y:
                for y in range(self.point_one.y, self.point_two.y):
                    points.append(Point(None,self.point_one.x,y))
            else:
                for y in range(self.point_two.y, self.point_one.y):
                    points.append(Point(None,self.point_one.x,y))
        else: # horizontal -- y remains the same
            if self.point_one.x < self.point_two.x:
                for x in range(self.point_one.x, self.point_two.x):
                    points.append(Point(None,x,self.point_one.y))
            else:
                for x in range(self.point_two.x, self.point_one.x):
                    points.append(Point(None,x,self.point_one.y))
        return list(set(points))

    def __str__(self):
        return f"[{point_one},{point_two}]\n"

    def __repr__(self):
        return f"[{point_one},{point_two}]\n"


all_points_dict = {}
danger_count = 0

# read the points in
with open("./input.txt") as f:
    for line in f:
        point_strings = line.split("->")

        point_one = Point(point_strings[0].strip())
        point_two = Point(point_strings[1].strip())

        map_line = Line(point_one, point_two)

        if map_line.process_points:
            all_points = map_line.get_all_points()
            for point in all_points:
                if point in all_points_dict:
                    all_points_dict[point] += 1
                    if all_points_dict[point] == 2:
                        danger_count += 1
                else:
                    all_points_dict[point] = 1 

print(danger_count)


