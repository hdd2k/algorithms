
input_strs = [
    'aaaaa',
    'hellohellohello',
    'xaaaxaaaxaaa',
    'hellloooooo',
    'couscousiscouscousiscouscous',
    'bookkeeper',
    'tctttttttttttcttttttttttctttttttttttct'
]

answer = [
    {'length': 2, 'sequence':'5a'},
    {'length': 8, 'sequence':'3(hello)'},
    {'length': 6, 'sequence':'3(x3a)'},
    {'length': 6, 'sequence':'he3l6o'},
    {'length': 19, 'sequence':'2(cous)2(is2(cous))'},
    {'length': 10, 'sequence':'bookkeeper'},
    {'length': 14, 'sequence':'tc11tc2(t9tct)'}
]


def full_2_short(full):
    
    return ''

def short_2_full(short):
    return ''



class RepStr:
    '''
    [Only represents 1 layer of compression] --- reference 'child' attribute for nested
    Repeating String with 2 representations
    - 1 : full string
    - 2 : Compressed version
    '''
    def __init__(self, full_str=''):
        # Assert full string is passed in
        assert '(' not in full_str
        assert ')' not in full_str

        self.full = full_str
        self.short = full_2_short(full_str)
        self.child = None

    def getChild(self):
        return self.child

    def setChild(self, child_repstr):
        self.child = child_repstr

def rep_count(in_str):

    '''
    if (expand())
    S(i,C) = S()

    * i    : full length from END of string
    * j    : Current full length of repeat string
    * S(i,C) : length from end of S, optimized to length C

    Solution = S(n) ... where n is len(S)
    '''

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
    print('Time : [{}] seconds'.format(round(end_time - start_time, 4)))

if __name__ == "__main__":
    main()



