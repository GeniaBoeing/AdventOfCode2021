input_file = 'input19'

with open(input_file) as f:
    lines = f.readlines()

scanners = []
for i in lines:
    if i == '\n':
        scanners.append(scanner)
    elif i[1] == '-': 
        scanner = []
    else:
        scanner.append([int(j) for j in i.strip().split(',')])    
scanners.append(scanner)


#at least 12 overlapping beacons to get scanners position relative to scanner 0
def sign(i):
    if i >= 0:
        return 1
    else:
        return -1

#generate the rotation_matrices
rotation_vectors = [[0,0,0] for i in range(0, 24)]
rotation_vectors = [[1, 2, 3],
                    [1, -3, 2],
                    [1, -2, -3], 
                    [1, 3, -2],
                    [-1, 2, -3], 
                    [-1, 3, 2], 
                    [-1, -2, 3], 
                    [-1, -3, -2],
                    [2, -1, 3],
                    [2, 1, -3],
                    [2, 3, 1],
                    [2, -3, -1],
                    [-2, -3, 1],
                    [-2, 3, -1],
                    [-2, 1, 3],
                    [-2, -1, -3],
                    [3, 2, -1], 
                    [3, -2, 1],
                    [3, 1, 2], 
                    [3, -1, -2],
                    [-3, 2, 1],
                    [-3, 1, -2],
                    [-3, -1, 2],
                    [-3, -2, -1]]
def rotate_beacons(scanner):
    all_rotations = []
    for rot in rotation_vectors:
        rot_scanner = []
        for beacon in scanner:
           rot_scanner.append([beacon[abs(rot[i])-1]*sign(rot[i]) for i in range(len(rot))]) 
        all_rotations.append(rot_scanner)
    return all_rotations



def add_common_beacons(reference, scanner):

    all_rotations = rotate_beacons(scanner)
    for rot in range(0, 24):
        rotated_scanner = all_rotations[rot]
        for beacon in range(0, len(reference)):
            for beacon_other in range(0, len(rotated_scanner)):
                difference = [reference[beacon][i] - rotated_scanner[beacon_other][i] for i in range(3)]
                adapted_scanner = []
                
                for b in range(0, len(rotated_scanner)):
                    adapted_scanner.append([rotated_scanner[b][i] + difference[i] for i in range(3)])
                
                counter = 0 
                for b in range(0, len(reference)):
                    for bb in range(0, len(adapted_scanner)):
                        if reference[b] == adapted_scanner[bb]:
                            counter += 1
                
                if counter >= 12: 
                    for bb in range(0, len(adapted_scanner)):
                        if adapted_scanner[bb] not in reference:
                            reference.append(adapted_scanner[bb])
                            
                    return reference, difference
    return reference, 0

beacons_in_common = scanners[0]
scanners_assimilated = [0]*len(scanners)
scanners_assimilated[0] = 1
scanner_positions = [[0,0,0]]
for j in range(0, len(scanners)):
    for i in range(1, len(scanners)):
        if scanners_assimilated[i] == 0:
            print(j, i)
            len_before = len(beacons_in_common)
            beacons_in_common, difference = add_common_beacons(beacons_in_common, scanners[i])
            len_after = len(beacons_in_common)
            if len_before != len_after:
                scanners_assimilated[i] = 1
                scanner_positions.append(difference)
    if sum(scanners_assimilated) == len(scanners):
        break


def manhatten_distance(v1, v2):
    dist = 0
    for i in range(0, len(v1)):
        dist += abs(v1[i] - v2[i])
    return dist

scanner_distances = []
for i in range(0, len(scanner_positions)):
    for j in range(0, len(scanner_positions)):
        scanner_distances.append(manhatten_distance(scanner_positions[i], scanner_positions[j]))


print('max manhatten distance   ', max(scanner_distances))        
print('nr of beacons in common  ', len(beacons_in_common))
