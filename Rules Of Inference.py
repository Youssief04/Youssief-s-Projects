def translate_to_logic(sentence):
    translations = {
        'and': '&',
        'or': '|',
        'not': '~',
        'if': '->',
        'then': '->',
        'iff': '<->',
        'if and only if': '<->',
        'implies': '->',
        'is equivalent to': '<->',
        'equals': '<->'
    }

    # Replace English words with logical symbols
    for word, symbol in translations.items():
        sentence = sentence.replace(word, symbol)

    # Add spaces around parentheses for consistent parsing
    sentence = sentence.replace('(', '( ')
    sentence = sentence.replace(')', ' )')

    return sentence


def apply_rule_of_inference(rule, premises):
    rules_of_inference = {
        'modus ponens': '(p -> q), p |- q',
        'modus tollens': '(p -> q), ~q |- ~p',
        'disjunctive syllogism': 'p | q, ~p |- q',
        'constructive dilemma': '(p -> q), (r -> s), p | r |- q | s',
        'hypothetical syllogism': '(p -> q), (q -> r) |- p -> r'
    }

    if rule not in rules_of_inference:
        return 'Invalid rule of inference'

    variables = [x.strip() for x in rules_of_inference[rule].split(' |- ')[0].split(',')]
    conclusion = rules_of_inference[rule].split(' |- ')[1]
    for i, variable in enumerate(variables):
        conclusion = conclusion.replace(variable, ['p', 'q'][i])
    for i, premise in enumerate(premises):
        for j, variable in enumerate(variables):
            premises[i] = premise.replace(variable, ['p', 'q'][j])
    rule = rules_of_inference[rule].format(*premises)
    for i, variable in enumerate(variables):
        conclusion = conclusion.replace(variable, ['p', 'q'][i])

    return conclusion
english_sentence = input("Enter an English sentence: ")
propositional_logic = translate_to_logic(english_sentence)
print("Propositional logic: ", propositional_logic)
premises = input("Enter premises in propositional logic separated by commas: ")
premises = premises.split(',')
rule = input("Enter a rule of inference: ")
conclusion = apply_rule_of_inference(rule, premises)
print("Conclusion in terms of p and q: ", conclusion)
                     