with open('day11.txt', 'r') as f: 
	data = [line.strip() for line in f.readlines()]

with open('test.txt', 'r') as f:
	test = [line.strip() for line in f.readlines()]


def part1(data):
	cur = data
	changed = True
	while changed:
		cur, changed = model_step(cur)

	occupied = 0
	for line in cur:
		for seat in line:
			if seat == "#":
				occupied += 1
	return occupied

def model_step(data):
	should_change = make_tracker(data)
	changed = False
	out = []
	for y, line in enumerate(data):
		for x, seat in enumerate(line):
			if seat == "L":
				adjacent_to = adjacent(x, y, data)
				if num_occupied(adjacent_to, data) == 0:
					should_change[y][x] = 1
					changed = True
			elif seat == "#":
				adjacent_to = adjacent(x, y, data)
				if num_occupied(adjacent_to, data) >= 4:
					should_change[y][x] = 1
					changed = True
	
	for y in range(len(should_change)):
		out_line = ""
		for x in range(len(should_change[0])):
			if should_change[y][x] == 1:
				if data[y][x] == "#":
					out_line +=  "L"
				elif data[y][x] == "L":
					out_line +=  "#"
			else:
				out_line += data[y][x]
		out.append(out_line)

	return out, changed


def num_occupied(seats, data):
	count = 0
	for seat in seats:
		if data[seat[1]][seat[0]] == "#":
			count += 1
	return count


def make_tracker(data):
	out = []
	for line in data:
		out.append([0] * len(line))
	return out


def adjacent(x, y, data):
	y_max = len(data) - 1
	x_max = len(data[0]) - 1
	adj = set()
	for i in [-1, 0, 1]:
		for j in [-1, 0, 1]:
			adj_x = max(min(x + i, x_max), 0)
			adj_y = max(min(y + j, y_max), 0)
			adj.add((adj_x, adj_y))

	adj.remove((x, y))
	adj = list(adj)
	# adj.sort()
	return adj


def part2(data):
	cur = data
	changed = True
	while changed:
		cur, changed = model_step2(cur)

	occupied = 0
	for line in cur:
		for seat in line:
			if seat == "#":
				occupied += 1
	return occupied


def model_step2(data):
	should_change = make_tracker(data)
	changed = False
	out = []
	for y, line in enumerate(data):
		for x, seat in enumerate(line):
			if seat != ".":
				occupied = visible_occupied(x, y, data)
			if seat == "#":
				if occupied >= 5:
					should_change[y][x] = 1
					changed = True
			elif seat == "L":
				if occupied == 0:
					should_change[y][x] = 1
					changed = True

	for y in range(len(should_change)):
		out_line = ""
		for x in range(len(should_change[0])):
			if should_change[y][x] == 1:
				if data[y][x] == "#":
					out_line +=  "L"
				elif data[y][x] == "L":
					out_line +=  "#"
			else:
				out_line += data[y][x]
		out.append(out_line)

	return out, changed


def visible_occupied(x, y, data):
	num_occupied = 0
	y_max = len(data) - 1
	x_max = len(data[0]) - 1
	i = 1
	while x - i >= 0: # to left
		if data[y][x-i] != ".":
			if data[y][x-i] == "#":
				num_occupied += 1
			break
		i += 1
	i = 1
	while x + i <= x_max: # to right
		if data[y][x+i] != ".":
			if data[y][x+i] == "#":
				num_occupied += 1
			break	
		i += 1
	i = 1
	while y + i <= y_max: # above
		if data[y+i][x] != ".":
			if data[y+i][x] == "#":
				num_occupied += 1
			break	
		i += 1
	i = 1
	while y - i >= 0: # below
		if data[y-i][x] != ".":
			if data[y-i][x] == "#":
				num_occupied += 1
			break	
		i += 1
	i = 1
	while (x + i <= x_max) and (y + i <= y_max): # right bottom diag
		if data[y+i][x+i] != ".":
			if data[y+i][x+i] == "#":
				num_occupied += 1
			break
		i += 1
	i = 1
	while (x - i >= 0) and (y - i >= 0): # left top diagonal
		if data[y-i][x-i] != ".":
			if data[y-i][x-i] == "#":
				num_occupied += 1
			break
		i += 1
	i = 1
	while (x - i >= 0) and (y + i <= y_max): # left bottom diagonal
		if data[y+i][x-i] != ".":
			if data[y+i][x-i] == "#":
				num_occupied += 1
			break
		i += 1
	i = 1
	while (x + i <= x_max) and (y - i >= 0): # right top diagonal
		if data[y-i][x+i] != ".":
			if data[y-i][x+i] == "#":
				num_occupied += 1
			break
		i += 1
	
	return num_occupied
	

if __name__ == "__main__":
	print(part1(data))
	print(part2(data))