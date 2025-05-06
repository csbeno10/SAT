from pysat.formula import CNF
from pysat.solvers import Minisat22
##from pysat.examples.enumerate import Enumerator


def haAkkor2(input_str):
    a, b, zero = map(int, input_str.split())
    for i in range (5):
        print(f"{a-i} {b+i} 0")
        ##print(f"{b - i} {a + i} 0")

def haAkkorNem2(input_str):
    a, b, zero = map(int, input_str.split())
    for i in range (5):
        print(f"{a-i} {b-i} 0")

def haAkkorNem4(input_str):
    a, b, c, d, zero = map(int, input_str.split())
    for i in range (5):
        print(f"{a-i} {b-i} {c-i} {d-i} 0")


def telepiAHoszabbMintMalnaB(input_str):
    a, b, c, d, zero = map(int, input_str.split())
    for i in range(5):
        for j in range(5):
            print(f"{a - i} {b - i} {c - j} {d - j} 0")

def ossz1():
    for i in range(15):
        print(f"{i*5+1} {i*5+2} {i*5+3} {i*5+4} {i*5+5} 0")
        for j in range(5):
            for f in range (5):
                if(f > j):
                    print(f"-{(i*5+1)+j} -{(i*5+1)+f}  0")

def ossz2():
    for i in range(3):
        for j in range(5):
            print(f"{i*25+1+j} {i*25+6+j} {i*25+11+j} {i*25+16+j} {i*25+21+j} 0")
            for f in range (5):
                for g in range(5):
                    if(g > f):
                        print(f"-{i*25+1+j+f*5} -{i*25+1+j+g*5}  0")


def clauses():
    with open("Ezermester SAT.txt") as f:
        clauses = [line for line in f if not line.startswith('c') and line.strip().endswith('0')]
        print(clauses)
        print(len(clauses) -1)

def elojelCsere(input):
    numbers = input.split()
    flipped_numbers = ['-' + num[0:] if num[0] != '-' else num[1:] for num in numbers]
    print(' '.join(flipped_numbers))

# Example usage:
if __name__ == "__main__":
    input_str = "5 10 0"  # You can change this as needed
    ##haAkkor2("-41 56 0")
    elojelCsere("-1 -2 -3 4 -5 -6 -7 -8 -9 10 11 -12 -13 -14 -15 -16 -17 18 -19 -20 -21 22 -23 -24 -25 -26 -27 -28 29 -30 31 -32 -33 -34 -35 -36 -37 38 -39 -40 -41 -42 -43 -44 45 -46 47 -48 -49 -50 -51 52 -53 -54 -55 -56 -57 -58 -59 60 -61 -62 -63 64 -65 66 -67 -68 -69 -70 -71 -72 73 -74 -75")
    clauses()
    cnf = CNF(from_file='Ezermester SAT.txt')
    with Minisat22(bootstrap_with=cnf.clauses) as solver:
        model_count = 0

        while solver.solve():
            model = solver.get_model()
            model_count += 1
            print(f"Model {model_count}: {model}")

            # Add a blocking clause: prevent the same model from appearing again
            # This blocks the *exact* assignment we just got
            blocking_clause = [-lit if lit > 0 else -lit for lit in model]
            solver.add_clause(blocking_clause)

        if model_count == 0:
            print("No solutions found.")
        else:
            print(f"Total models found: {model_count}")
    #telepiAHoszabbMintMalnaB("-71 -36 -46 -66 0")
    #haAkkorNem2("-56 -46 0")