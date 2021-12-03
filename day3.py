input_file = 'input3.txt'
input = []
with open(input_file) as f:
    for line in f:
        input.append(int(line, 2))
nr_bits = 12

#nr_bits = 5
#input = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
#input = [int(i, 2) for i in input]
nr_inputs = len(input)

ones = [0]*nr_bits
for i in range(0, nr_bits):
    for k in input:
        ones[i] += (k & 2**(nr_bits-i-1)) >> (nr_bits-1-i)

gamma = 0
epsilon = 0
for i in ones:
    if i > nr_inputs/2:
        gamma += 1
    else:
        epsilon += 1
    gamma = gamma << 1
    epsilon = epsilon << 1
gamma = gamma >> 1
epsilon = epsilon >> 1


print(gamma, epsilon)
print(gamma*epsilon)


oxy_rating = input
for i in range(0, nr_bits):
    if len(oxy_rating) > 1:
        #update the ones count:
        ones = 0
        for k in oxy_rating:
            ones += (k & 2**(nr_bits-i-1)) >> (nr_bits-i-1)
        if ones >= len(oxy_rating)/2:
            oxy_rating = [j for j in oxy_rating if j & 2**(nr_bits-i-1) != 0]
        else:
            oxy_rating = [j for j in oxy_rating if j & 2**(nr_bits-i-1) == 0 ]
            print('meh')
print(oxy_rating)



co2_rating = input
for i in range(0, nr_bits):
    if len(co2_rating) > 1:
        #update the ones count:
        ones = 0
        for k in co2_rating:
            ones += (k & 2**(nr_bits-i-1)) >> (nr_bits-i-1)
        if ones >= len(co2_rating)/2:
            co2_rating = [j for j in co2_rating if j & 2**(nr_bits-i-1) == 0]
        else:
            co2_rating = [j for j in co2_rating if j & 2**(nr_bits-i-1) != 0 ]
            print('meh')
print(co2_rating)

print(co2_rating[0] * oxy_rating[0])
