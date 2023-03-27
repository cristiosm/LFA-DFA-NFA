#CITIRE
def read(file):
    with open(file) as f:
        lines = f.readlines()
        states = set(lines[0].strip().split())
        symbols = set(lines[1].strip())
        dfa = {}
        for line in lines[2:-2]:
            state, symbol, next_state = line.strip().split()
            if state not in dfa:
                dfa[state] = {}
            dfa[state][symbol] = next_state

        initial_state = lines[-2].strip()
        final_states = set(lines[-1].strip().split())
    return states, symbols, dfa, initial_state, final_states


#FUNCTIE DFA
def verif(states, accepted_symbols, dfa, initial_state, final_states, word):
    current_state = initial_state
    path = [current_state]
    for symbol in word:
        if symbol not in accepted_symbols:
            return False, None
        if symbol not in dfa[current_state]:
            return False, None
        current_state = dfa[current_state][symbol]
        path.append(current_state)
    if current_state in final_states:
        return True, path
    else:
        return False, None

#MAIN
states, symbols, dfa, initial_state, final_states = read('input.in')
word = input('Introduceti un cuvant: ')
accepted, path = verif(states, symbols, dfa, initial_state, final_states, word)
if accepted:
    print(f'Cuvantul "{word}" este acceptat de DFA.')
    print('Drumul: ',end='')
    print(' '.join(path))
else:
    print(f'Cuvantul "{word}" nu este acceptat de DFA.')
