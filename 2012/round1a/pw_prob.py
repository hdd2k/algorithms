'''
Case #1: 7.000000
Case #2: 20.000000
Case #3: 4.500000

T (num tests)
A B 
where
A : num keys already typed
B : num total chars in password
p_i : prob of correctly typing i_th password
'''


'''
3 choices

1) start over (enter + len(password) + enter)
2) keep typing (len(pw) - curr chars)
- if ANY wrong... expected = len(pw) - curr chars + len(pw)
- if NONE wrong... expected = len(pw) - curr chars
3) press delete {1..curr_chars}
- i_th WRONG char, all chars after it prob * CORRECT... and i_th WRONG
- if ANY (i-)_th char is WRONG --->  
'''
def expected(AB, probs):
  prev_len = int( AB[0] )
  pw_len = int( AB[1] )

  # Pick MINIMUM of 3 strategies (optimal)

  # Start over = 1(enter) + len(pw) + 1(enter)
  startover = 1 + (pw_len) + 1

  # keep typing = num(enter) + expected(if ANY wrong OR if NONE wrong)
  prob_none_wrong = reduce(lambda acc, p: acc * float(p), probs, 1)
  prob_any_wrong = 1 - prob_none_wrong
  keeptyping = ((prob_any_wrong)*(pw_len+(pw_len-prev_len)+1+1) + (prob_none_wrong)*(pw_len-prev_len+1))

  print(probs)
  # press delete(s)
  # Find expected value for each DELETE key num times pressed (1..prev_len)
  deletes = 0
  for d in range(1,prev_len+1):
    print('$$$$$$$$$$$$')
    print(prev_len)
    print(d)
    # For each DELETE key num, find prob of earliest wrong being contained
    # prob contained = first portion ALL correct
    prob_contained = reduce(lambda acc, p : acc*float(p), probs[:(prev_len-d)], 1)
    # expected = (prob earliest wrong contained * (correct the 1st time) ) + ((1-prob earliest wrong) * (2nd time correct))
    deletes += ((prob_contained)*(d+d+(pw_len-prev_len)+1) + (1-prob_contained)*(d+d+(pw_len-prev_len)+1 + pw_len+1))
    print(deletes)
  print("#######")
  deletes /= prev_len
  print(deletes)

  ######## (?) Find EARLIEST wrong position...(geometric distribution... correct until 1st wrong)
  return min(startover, keeptyping, deletes)

def main():
  # TODO: Read stdin
  import sys
  # Tokenize stdin for meaningful variables
  input = [x.split() for x in  sys.stdin.readlines() ]
  num_tests = int( input[0][0] )
  content = input[1:]
  # print(num_tests)
  # print(content)
  line_idx = 0
  for t in range(num_tests):
    curr_AB = content[ line_idx ]
    line_idx += 1
    curr_probs = content[ line_idx ]
    line_idx += 1

    # TODO: apply algorithm
    answer = expected(curr_AB, curr_probs)
    print("Case #" + str(t) + ": " + '{0:.6f}'.format( answer ))

main()



