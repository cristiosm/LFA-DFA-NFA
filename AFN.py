#CITIRE
def read(file):
    with open(file) as f:
        lines = f.readlines()
        states = set(lines[0].strip().split())
        symbols = set(lines[1].strip())
        nfa = {}
        for line in lines[2:-2]:
            state, symbol, *next_states = line.strip().split()
            next_states = set(next_states)
            if state not in nfa:
                nfa[state] = {}
            if symbol not in nfa[state]:
                nfa[state][symbol] = set()
            nfa[state][symbol].update(next_states)

        initial_state = lines[-2].strip()
        final_states = set(lines[-1].strip().split())
    return states, symbols, nfa, initial_state, final_states

#FUNCTIE NFA-LAMBDA
def lambdaf(nfa, states):
    closure = set(states)
    stack = list(states)
    while stack:
        state = stack.pop()
        if state in nfa and '' in nfa[state]:
            for s in nfa[state]['']:
                if s not in closure:
                    closure.add(s)
                    stack.append(s)
    return closure


def move(nfa, states, symbol):
    moves = set()
    for state in states:
        if state in nfa and symbol in nfa[state]:
            moves.update(nfa[state][symbol])
    return moves

#FUNCTIE NFA
def verif(states, symbols, nfa, initial_state, final_states, word):
    current_states = lambdaf(nfa, {initial_state})
    path = [initial_state]
    for symbol in word:
        current_states = lambdaf(nfa, move(nfa, current_states, symbol))
        path.extend(current_states)
    if any(state in final_states for state in current_states):
        return True, path
    else:
        return False, None

#MAIN
states, symbols, nfa, initial_state, final_states = read('input.in')
word = input('Introduceti un cuvant: ')
accepted, path = verif(states, symbols, nfa, initial_state, final_states, word)
if accepted:
    print(f'Cuvantul "{word}" este acceptat de NFA.')
    print('Drumul: ',end='')
    print(' '.join(path))
else:
    print(f'Cuvantul "{word}" nu este acceptat de NFA.')
