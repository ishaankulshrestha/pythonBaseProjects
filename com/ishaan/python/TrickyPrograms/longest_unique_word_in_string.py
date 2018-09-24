my_string = "abcdefghijabcdefghiklmnabcdefghijklmnopqrstuvabcdefghijklmn"

substr  = set()
current_start_pos = 0
current_end_pos = 0
ultimate_start_pos = 0
ultimate_end_pos = 0

for i in range(len(my_string)):
    if my_string[i] not in substr :
        substr.add(my_string[i])
        continue
    current_end_pos = i
   # print("dup at start_pos = {} and end_position = {} ".format(current_start_pos,current_end_pos))
    if ultimate_end_pos - ultimate_start_pos < current_end_pos - current_start_pos:
        ultimate_start_pos = current_start_pos
        ultimate_end_pos = current_end_pos
    new_current_start_pos = my_string.find(my_string[i],current_start_pos,current_end_pos)
    #print("in string {} position of {} is {} between {} and {} ".format(my_string,my_string[i],new_current_start_pos,current_start_pos,current_end_pos))
    for ch in my_string[current_start_pos:new_current_start_pos]:
        #if ch in substr:
        substr.remove(ch)
    current_start_pos = new_current_start_pos + 1

print(my_string[ultimate_start_pos:ultimate_end_pos])




