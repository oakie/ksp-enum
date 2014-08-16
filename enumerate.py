import re
import argparse

parser = argparse.ArgumentParser(description='Enumerates your KSP spaceship\'s parts for easier save-file editing.')
parser.add_argument('path', help='Path to your save-file (.sfs)')

args = parser.parse_args()
print(args.path)

with open(args.path, 'r') as f:
	
	vp = re.compile(r'VESSEL')
	np = re.compile(r'[.]* \= (.*)$')
	pp = re.compile(r'PART')

	vessel_cnt = 0
	part_cnt = 0

	for line in f:		
		m = vp.findall(line)
		if len(m) > 0:
			next(f)
			next(f)
			line = next(f)
			name = np.search(line).group(1)
			print('\n\n', vessel_cnt, ' - ', name)
			part_cnt = 0
			vessel_cnt += 1

		m = pp.findall(line)
		if len(m) > 0:
			next(f)
			line = next(f)
			name = np.search(line).group(1)
			print('\t', part_cnt, ': ', name)
			part_cnt += 1
