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
        type_id = int(mssg[3:6], 2)
        if type_id == 4:
            value, mssg = read_lit_value(mssg, 6)
            return type_id, value, mssg
        else:
            packets = []
            length_type = int(mssg[6])
            if length_type == 1:
                nr_sub_packets = int(mssg[7:18], 2) 
                mssg = mssg[18:]
                for i in range(nr_sub_packets):
                    _, value, mssg = read_mssg(mssg)
                    packets.append((_, value))
            elif length_type == 0:
                total_length_subs = int(mssg[7:22], 2)
                tmp_mssg = mssg[22:22+total_length_subs]
                mssg = mssg[22+total_length_subs:]
                while tmp_mssg:
                    _, value, tmp_mssg = read_mssg(tmp_mssg)
                    packets.append((_, value))
            return type_id, packets, mssg
def apply_operator(seq):
    if seq[0]  == 0:
        return sum(map(apply_operator, seq[1]))
    elif seq[0] == 1:
        tmp = 1
        for i in seq[1]:
            tmp *= apply_operator(i)
        return tmp
    elif seq[0] == 2:
        return min(map(apply_operator, seq[1]))
    elif seq[0] == 3:
        return max(map(apply_operator, seq[1]))
    elif seq[0] == 4:
        return seq[1]
    elif seq[0] == 5:
        return apply_operator(seq[1][0]) > apply_operator(seq[1][1])
    elif seq[0] == 6:
        return apply_operator(seq[1][0]) < apply_operator(seq[1][1])
    elif seq[0] == 7:
        return apply_operator(seq[1][0]) ==  apply_operator(seq[1][1])

operator = ['+', '*', 'min', 'max', 'value', '>', '<', '=='] 
sum_version = 0   
not_finished = True         
input = 'C20D42002ED333E7774EAAC3C2009670015692C61B65892239803536C53E2D307A600ACF324928380133D18361005B336D3600B4BF96E4A59FED94C029981C96409C4A964F995D2015DE6BD1C6E7256B004C0010A86B06A1F0002151AE0CC79866600ACC5CABC0151006238C46858200E4178F90F663FBA4FDEC0610096F8019B8803F19A1641C100722E4368C3351D0E9802D60084DC752739B8EA4ED377DE454C0119BBAFE80213F68CDC66A349B0B0053B23DDD61FF22CB874AD1C4C0139CA29580230A216C9FF54AD25A193002A2FA002AB3A63377C124205008A05CB4B66B24F33E06E014CF9CCDC3A2F22B72548E842721A573005E6E5F76D0042676BB33B5F8C46008F8023301B3F59E1464FB88DCBE6680F34C8C0115CDAA48F5EE45E278380019F9EC6395F6BE404016849E39DE2EF002013C873C8A401544EB2E002FF3D51B9CAF03C0010793E0344D00104E7611C284F5B2A10626776F785E6BD672200D3A801A798964E6671A3E9AF42A38400EF4C88CC32C24933B1006E7AC2F3E8728C8E008C759B45400B4A0B4A6CD23C4AF09646786B70028C00C002E6D00AEC1003440080024658086A401EE98070B50029400C0014FD00489000F7D400E000A60001E870038800AB9AB871005B12B37DB004266FC28988E52080462973DD0050401A8351DA0B00021D1B220C1E0013A0C0198410BE1C180370C21CC552004222FC1983A0018FCE2ACBDF109F76393751D965E3004E763DB4E169E436C0151007A10C20884000874698630708050C00043E24C188CC0008744A8311E4401D8B109A3290060BE00ACEA449214CD7B084B04F1A48025F8BD800AB4D64426B22CA00FC9BE4EA2C9EA6DC40181E802B39E009CB5B87539DD864A537DA7858C011B005E633E9F6EA133FA78EE53B7DE80'
mssg = hextobin(input)
result = read_mssg(mssg)

print('sum of all versions: ', sum_version)
print('resulting value: ', int(apply_operator(result)))
