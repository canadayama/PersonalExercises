N = 0 # array pos num bushes
M = 1 # array pos num rabbits
K = 2 # array pos num jumps/iterations
EMPTY=0
OCCUPIED=1

input_line = input().split()
#print(input_line)
if len(input_line) != 3:
    raise Exception('Not 3 integers')

int_inputs = [int(i) for i in input_line]
#print(int_inputs)

bushes = [EMPTY] * int_inputs[N]


rabbit_pos = [0] * int_inputs[M]
for r in range(int_inputs[M]):
    rabbit_pos[r] = int(input())
    if rabbit_pos[r] < 1 or rabbit_pos[r] > int_inputs[N]:
        raise Exception(f'Must be in [1, {int_inputs[N]}]')
    if bushes[rabbit_pos[r]-1] == OCCUPIED:
        raise Exception(f'Already a rabbit in bush #{rabbit_pos[r]}')
    bushes[rabbit_pos[r]-1] = OCCUPIED
#print(bushes)
#print(rabbit_pos)

# Go through jumps/iterations
for j in range(int_inputs[K]):
    for r in range(int_inputs[M]):
        next_idx = rabbit_pos[r]
        cur_idx = rabbit_pos[r] - 1
        for _ in range(int_inputs[N]):
            if next_idx >= int_inputs[N]:
                next_idx = 0
            if bushes[next_idx] == EMPTY:
                rabbit_pos[r] = next_idx + 1
                bushes[cur_idx] = EMPTY
                bushes[next_idx] = OCCUPIED
                break
            next_idx += 1
# print(bushes)
print('Output:')
for rpos in rabbit_pos:
    print(rpos)
