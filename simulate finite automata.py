class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.current_state = start_state
        self.accept_states = accept_states

    def reset(self):
        """Resets DFA to the start state."""
        self.current_state = start_state

    def process_input(self, input_string):
        """Processes an input string and returns True if accepted, otherwise False."""
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False  # Invalid input
            self.current_state = self.transition_function[self.current_state][symbol]
        return self.current_state in self.accept_states


# DFA Definition
states = {"q0", "q1"}
alphabet = {"0", "1"}
transition_function = {
    "q0": {"0": "q1", "1": "q0"},
    "q1": {"0": "q0", "1": "q1"}
}
start_state = "q0"
accept_states = {"q0"}

# DFA Instance
dfa = DFA(states, alphabet, transition_function, start_state, accept_states)

# Test DFA
test_strings = ["", "1", "0", "10", "110", "1010", "000"]
for test in test_strings:
    result = dfa.process_input(test)
    print(f"Input: {test.ljust(5)} -> {'Accepted' if result else 'Rejected'}")
