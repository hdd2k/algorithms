
import sys

def main():
# Read standard input
  lines = sys.stdin.readlines()
  count = 1
  for x in lines[1:]:
    s = list( x.strip() )
    answer = ""
    for c in s:
      if len(answer) == 0:
        answer = c
      else:
        if c >= answer[0]:
          answer = c + answer
        else:
          answer = answer + c
    print("Case #" + str(count) + ": " + answer)
    count += 1

main()
