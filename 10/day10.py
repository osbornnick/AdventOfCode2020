with open('day10.txt', 'r') as f: 
	data = [int(line) for line in f.readlines()]


with open('test.txt', 'r') as f:
	test = [int(line) for line in f.readlines()]


def part1(data):
	data.append(0)
	data.sort()
	data.append(data[-1] + 3) # add device joltage

	one_diffs = 0
	three_diffs = 0
	i = 1

	while i < len(data):
		diff = data[i] - data[i - 1]
		if diff == 3:
			three_diffs += 1
		elif diff == 1:
			one_diffs += 1
		i += 1
	
	return three_diffs * one_diffs


def part2(data):
	data.append(0)
	data.sort()
	data.append(data[-1] + 3) # add device joltage
	paths = [0] * (data[-1] + 1)
	paths[0] = 1
	for x in data:
		for i in range(1, 4):
			if (x - i) >= 0:
				paths[x] += paths[x - i]

	return paths[-1]
		
if __name__ == "__main__":
	print(part1(data))
	print(part2(data))