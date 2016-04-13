import nester

man = []
other = []
try:
    data = open('../sketch.txt')
    for line in data:
        try:
            (role, line_spoken) = line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')

try:
    # man_file = open('man_data.txt', 'w')
    # other_file = open('other_data.txt', 'w')
    
    with open('man_data2.txt', 'w') as man_file:
        nester.print_lol(man, fh=man_file)
        
    with open('other_data2.txt', 'w') as other_file:
        nester.print_lol(other, fh=other_file)

except IOError as err:
    print('File error: ' + str(err))