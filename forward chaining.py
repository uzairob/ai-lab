# Define initial facts and rules 
facts = {"InAmerica(West)", "SoldWeapons(West, Nono)", "Enemy(Nono, America)"} rules = [ 
    { 
        "conditions": ["InAmerica(x)", "SoldWeapons(x, y)", "Enemy(y, America)"], 
        "conclusion": "Criminal(x)", 
    }, 
    { 
        "conditions": ["Enemy(y, America)"], 
        "conclusion": "Dangerous(y)", 
    }, 
]  
# Forward chaining function def forward_chaining(facts, rules): 
    derived_facts = set(facts)  # Initialize derived facts     while True:         new_fact_found = False 
 
        for rule in rules: 
            # Substitute variables and check if conditions are met             for fact in derived_facts:                 if "x" in rule["conditions"][0]: 
                    # Substitute variables (x, y) with specific instances                     for condition in rule["conditions"]: 
                        if "x" in condition or "y" in condition:                             x = "West"  # Hardcoded substitution for simplicity                             y = "Nono"                             conditions = [                                 cond.replace("x", x).replace("y", y) 
                                for cond in rule["conditions"] 
                            ] 
                            conclusion = ( 
                                rule["conclusion"].replace("x", x).replace("y", y) 
                            ) 
                             # Check if all conditions are satisfied 
                            if all(cond in derived_facts for cond in conditions) and conclusion not in derived_facts: 
                                derived_facts.add(conclusion)                                 print(f"New fact derived: {conclusion}")                                 new_fact_found = True 
 
        # Exit loop if no new fact is found         if not new_fact_found:             break 
 
    return derived_facts 
 
# Run forward chaining 
final_facts = forward_chaining(facts, rules) print("\nFinal derived facts:") for fact in final_facts: 
    print(fact)

##
class FirstOrderLogicKB:
    def __init__(self):
        """Initialize the knowledge base with an empty set of facts and rules."""
        self.facts = set()  # Set to hold facts
        self.rules = []     # List to hold rules (premise, conclusion)

    def add_fact(self, fact):
        """Add a fact to the knowledge base."""
        self.facts.add(fact)

    def add_rule(self, premise, conclusion):
        """Add a rule to the knowledge base: premise => conclusion."""
        self.rules.append((premise, conclusion))

    def forward_reasoning(self):
        """Apply forward reasoning to deduce new facts from the knowledge base."""
        new_facts = set(self.facts)
        inferred = True

        # Keep inferring new facts until no new facts can be deduced
        while inferred:
            inferred = False
            for premise, conclusion in self.rules:
                if premise.issubset(new_facts) and conclusion not in new_facts:
                    new_facts.add(conclusion)
                    inferred = True
        self.facts = new_facts

    def query(self, fact):
        """Check if a fact is in the knowledge base after reasoning."""
        return fact in self.facts

    def display_facts(self):
        """Display all the facts in the knowledge base."""
        print("Known Facts:")
        for fact in self.facts:
            print(fact)


def input_facts_and_rules():
    kb = FirstOrderLogicKB()

    # Input facts
    kb.add_fact("American(Robert)")
    kb.add_fact("Enemy(A, America)")
    kb.add_fact("Owns(A, T1)")
    kb.add_fact("Missile(T1)")
    kb.add_fact("SellsWeapon(Robert, T1)")

    # Input rule for being a criminal
    rule_premise = {"American(Robert)", "SellsWeapon(Robert, T1)", "Enemy(A, America)"}
    rule_conclusion = "Criminal(Robert)"
    kb.add_rule(rule_premise, rule_conclusion)

    # Perform forward reasoning to deduce new facts
    kb.forward_reasoning()

    return kb

def main():
    # Input the knowledge base facts and rules
    kb = input_facts_and_rules()

    # Display all the facts entered
    kb.display_facts()

    # Query the knowledge base to prove if Robert is a criminal
    if kb.query("Criminal(Robert)"):
        print("\nYes, Robert is a criminal.")
    else:
        print("\nNo, Robert is not a criminal.")

if __name__ == "__main__":
    main() 
 
