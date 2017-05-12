import sys

def main():
  # Read input
  lines = sys.stdin.readlines()
  test_cases = int( lines[0].strip() )
  inputs = lines[1:]
  curr_line_idx = 0
  for t_idx in range( test_cases ):
    # 1 line = N
    currN = int( inputs[curr_line_idx].strip()[0] )
    curr_line_idx += 1
    # 2N-1 lines = sequences
    curr_soldier_lines = inputs[curr_line_idx:(curr_line_idx + 2*currN )]
    curr_line_idx += (2*currN-1)

    # curr_soldier_lines ---> 1D list
    # Store INDEX of number as well
    all_nums = []
    for s in curr_soldier_lines:
      # all_nums += s.strip().split()
      for idx, x in enumerate( s.strip().split() ):
        all_nums.append( [int(x),idx] )

    # 2D list  ---> dictionary  (allow for repeat entries)
    from collections import defaultdict
    num_pos = defaultdict(list)
    for num in all_nums:
      num_pos[num[0]] += [num[1]]

    # For each key, eliminate 2 same position entries OR 2 entries that sum to (currN-1)
    # print (num_pos)
    for k,v in num_pos.items():
      # print(k)
      # print(v)
      occur_count = defaultdict(int)
      for elem in v:
        occur_count[elem] += 1
      # Getting rid of duplicated (in same position)
      for k_2, v_2 in occur_count.items():
        occur_count[k_2] = v_2 % 2
      # Getting rid of opposite end indices
      for k_2, v_2 in occur_count.items():
        opposite_num = ((currN - 1) - v_2)
        match_exists = (opposite_num in occur_count.keys() and occur_count[opposite_num] == 1)
        if match_exists:
          # Erase current k_2 && match_idx
          occur_count[opposite_num] = 0
          occur_count[k_2] = 0
      # print(occur_count)
      # Update num_pos[k] = occur_count
      num_pos[k] = [k for k,v in occur_count.items() if v == 1]
    # Find correct missing nums
    missing_nums = []
    for entry, idx_list in num_pos.items():
      for idx in idx_list:
        missing_nums += [ entry ]
    missing_nums.sort()
    answer = ""
    for n in ( missing_nums ):
      answer += str(n) + " "

    # print(currN)
    # print(curr_soldier_lines)
    # print(all_nums)
    # print(missing_nums)
    # print("#####")
    print("Case #" + str(t_idx+1) + ": " + answer)

# Sort missing
# Output



# 

# Sort number sequences
# ALL numbers should occur in EVEN number counts. If not, add to missing_num
# With missing_num list, sort in increasing order
# Print result

main()
