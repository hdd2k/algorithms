
input_strs = [
    'hellloooooo',
    'couscousiscouscousiscouscous',
    'bookkeeper',
    'tctttttttttttcttttttttttctttttttttttct'
]

answer = [
    {'length': 6, 'sequence':'he3l6o'},
    {'length': 19, 'sequence':'2(cous)2(is2(cous))'},
    {'length': 10, 'sequence':'bookkeeper'},
    {'length': 14, 'sequence':'tc11tc2(t9tct)'}
]


def rep_count(in_str):
    sol_len = len(in_str)
    sol_str = in_str
    sol = {'length': len(in_str), 'sequence': in_str}
    return sol



def main():
    import time
    start_time = time.time()

    print('starting...')
    # Main loop
    len_counter, str_counter = 0, 0
    for idx, x in enumerate(input_strs):
        print("####################")
        print('input : [{}]'.format(x))
        curr_ans = answer[idx]
        print("--------------------")
        print('answer : [{}]'.format(curr_ans))
        solution = rep_count(x)
        print('output : [{}]'.format(solution))
        if (curr_ans.get('length') == solution.get('length')):
            len_counter += 1
        if (curr_ans.get('sequence') == solution.get('sequence')):
            str_counter += 1
    print("######### Results #########")
    print('Finished with [{} / {}] correct LENGTH\nFinished with [{} / {}] correct STRING'.format(len_counter, len(input_strs), str_counter, len(input_strs)))

    end_time = time.time()
    print('Time : [{}] seconds'.format(round(end_time - start_time, 3)))

if __name__ == "__main__":
    main()



