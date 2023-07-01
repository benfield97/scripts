N = 1000

class TuringMachine:

    #initiliaze turing machine
    def __init__(self, program, input, state=0):
        self.trf = {}
        self.state = str(state)
        self.tape = ''.join(['_']*N)
        self.head = N//2
        self.tape = self.tape[:self.head] + input + self.tape[self.head:]
        for line in program.splitlines():
            s, a, r, d, s1 = line.split(' ')
            self.trf[(s, a)] = (r, d, s1)