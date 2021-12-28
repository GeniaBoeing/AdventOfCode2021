#hexa to bin
#first 3 bits: version
#second 3 bits: type id. if 4: literal value single value. all other types are
#operators

#if operator 7th bit: length type ID. 0: next 15 bits nr represents total length
#in bits of the sub-packets #if 1: next 11 bits represent nr of sub Packets


def hextobin(h):
  return bin(int(h, 16))[2:].zfill(len(h) * 4)

def read_lit_value(mssg, start):
    not_last_group = True
    i = start + 1
    value = ''
    while(not_last_group):
        value += mssg[i:i+4]
        if mssg[i-1] == '0':
            not_last_group = False
        i += 5
    value = int(value, 2)
    mssg = mssg[i-1:]
    return value, mssg

def read_mssg(mssg):
    global sum_version
    global not_finished 
    while(not_finished):
        if mssg == '' or '1' not in mssg:
            not_finished = False
            break
        version = int(mssg[0:3], 2)
        sum_version += version
        print(version)
        type_id = int(mssg[3:6], 2)
        if type_id == 4:
            value, mssg = read_lit_value(mssg, 6)
        else:
            length_type = int(mssg[6])
            if length_type == 1:
                nr_sub_packets = int(mssg[7:18], 2)
                print('nr_sub_packets ', nr_sub_packets)
                read_mssg(mssg[18:])                        
            elif length_type == 0:
                total_length_subs = int(mssg[7:22], 2)
                print('total length sub packages: ', total_length_subs)
                read_mssg(mssg[22:])
sum_version = 0   
not_finished = True         
input = 'A0016C880162017C3686B18A3D4780'
mssg = hextobin(input)
read_mssg(mssg)

print('sum of all versions: ', sum_version)
