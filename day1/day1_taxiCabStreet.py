import math, copy, os

file_directory = os.path.dirname(os.path.realpath(__file__))

with open("%s/day1_input.txt"%file_directory,"r") as file_open:
    path_taken = file_open.read().split(', ')

compass = ['N', 'E', 'S', 'W']
direction_facing = 'N'
direction_facing_multiplier = {'N':1, 'E':1, 'S':-1, 'W':-1}

startpoint_vector = [0,0]
endpoint_vector = [0,0]

history_vectors = []
history_vectors.append(startpoint_vector)

for i in range(len(path_taken)):
    if path_taken[i][0] == 'R':
        direction_facing = compass[(compass.index(direction_facing)+1)%4]
        endpoint_vector[compass.index(direction_facing)%2] += direction_facing_multiplier[direction_facing] * int(path_taken[i][1:])
    elif path_taken[i][0] == 'L':
        direction_facing = compass[(compass.index(direction_facing)-1)%4]
        endpoint_vector[compass.index(direction_facing)%2] += direction_facing_multiplier[direction_facing] * int(path_taken[i][1:])
    current_vector = copy.deepcopy(endpoint_vector)
    history_vectors.append(current_vector)
taxicab_vector = math.fabs(endpoint_vector[0] - startpoint_vector[0]) + math.fabs(endpoint_vector[1] - startpoint_vector[1])
print int(taxicab_vector)

#### PART 2

def get_index_zero_diff(history_step_current, history_step_after):
    if history_step_after[0]-history_step_current[0]!=0:
        sign = (history_step_after[0]-history_step_current[0])/math.fabs(history_step_after[0]-history_step_current[0])
        return 0, sign
    else:
        sign = (history_step_after[1]-history_step_current[1])/math.fabs(history_step_after[1]-history_step_current[1])
        return 1, sign

stepwise_history_vectors = []
steps_intersected = []
for step in range(len(history_vectors)):
    current_step = copy.deepcopy(history_vectors[step])
    stepwise_history_vectors.append(copy.deepcopy(current_step))
    if step == len(history_vectors)-1:
        continue

    index_with_change, sign = get_index_zero_diff(history_vectors[step], history_vectors[step+1])
    while current_step[index_with_change] - history_vectors[step+1][index_with_change] != 0:
        current_step[index_with_change]+=1*int(sign)
        if current_step in stepwise_history_vectors:
            steps_intersected.append(copy.deepcopy(current_step))
        stepwise_history_vectors.append(copy.deepcopy(current_step))

print steps_intersected
