with open('day12.txt', 'r') as f: 
	data = f.readlines()

with open('test.txt', 'r') as f: 
	test = f.readlines()

def part1(data):
	loc = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
	direction = 'E'
	for line in data:
		char = line[0]
		num = int(line[1:])
		if char in loc:
			loc[char] += num
		elif char == "F":
			loc[direction] += num
		else:
			direction = update_direction(direction, char, num)
	
	vert = abs(loc['N'] - loc['S'])
	horz = abs(loc['E'] - loc['W'])
	return vert + horz


def update_direction(direction, turn, angle):
	order = ['N', 'E', 'S', 'W']
	angle = int(angle / 90)
	sign = 1 if turn == 'R' else -1
	direction = order.index(direction)
	return order[(direction + sign*angle) % 4]


def part2(data):
	waypoint = {'N': 1, 'E': 10, 'S': 0, 'W': 0}
	loc = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
	for line in data:
		char = line[0]
		num = int(line[1:])
		if char in waypoint:
			waypoint[char] += num
		elif char == "F":
			for k in loc:
				loc[k] += num * waypoint[k]
		else:
			waypoint = rotate_waypoint(waypoint, char, num)

	vert = abs(loc['N'] - loc['S'])
	horz = abs(loc['E'] - loc['W'])
	return vert + horz



def rotate_waypoint(waypoint, turn, angle):
	loc = ['N', 'E', 'S', 'W']
	out = {}
	angle = int(angle / 90)
	sign = 1 if turn == 'R' else -1
	for d in waypoint:
		i = loc.index(d)
		out[loc[(i + (sign * angle)) % 4]] = waypoint[d]

	return out


if __name__ == "__main__":
	print(part1(test))
	print(part1(data))

	print(part2(test))
	print(part2(data))