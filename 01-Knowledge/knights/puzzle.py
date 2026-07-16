from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Common rules
base = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave))
)

# Puzzle 0
# A says "I am both a knight and a knave."

statement0 = And(AKnight, AKnave)

knowledge0 = And(
    base,

    Implication(AKnight, statement0),
    Implication(AKnave, Not(statement0))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.

statement1 = And(AKnave, BKnave)

knowledge1 = And(
    base,

    Implication(AKnight, statement1),
    Implication(AKnave, Not(statement1))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

same_kind = Or(
    And(AKnight, BKnight),
    And(AKnave, BKnave)
)

different_kind = Or(
    And(AKnight, BKnave),
    And(AKnave, BKnight)
)

knowledge2 = And(
    base,

    Implication(AKnight, same_kind),
    Implication(AKnave, Not(same_kind)),

    Implication(BKnight, different_kind),
    Implication(BKnave, Not(different_kind))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave."
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

ASaidKnight = Symbol("A said I am a Knight")
ASaidKnave = Symbol("A said I am a Knave")

knowledge3 = And(
    base,

    Or(ASaidKnight, ASaidKnave),
    Not(And(ASaidKnight, ASaidKnave)),

    Implication(
        AKnight,
        Or(
            And(ASaidKnight, AKnight),
            And(ASaidKnave, AKnave)
        )
    ),

    Implication(
        AKnave,
        Or(
            And(ASaidKnight, Not(AKnight)),
            And(ASaidKnave, Not(AKnave))
        )
    ),

    Implication(BKnight, ASaidKnave),
    Implication(BKnave, Not(ASaidKnave)),

    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),

    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]

    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()