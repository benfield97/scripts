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


    # step through program 

    def step(self):
        if self.state != 'H':
            a = self.tape[self.head]
            action = self.trf.get((self.state, a))
            if action:
                r, d, s1 = action
                self.tape = self.tape[:self.head] + r + self.tape[self.head+1:]
                if d != '*':
                    self.head = self.head + (1 if d == 'r' else -1)
                self.state = s1
                print(self.tape.replace('_', ''), self.state)
    
    # run program

    def run(self, max_iter=9999):
        iter =0
        while self.state != 'H' and iter < max_iter:
            self.step()
            iter += 1
        print(self.tape.replace('_', ''), self.state)