# SAT-Sudoku-Solver

Input
-----
A text file with the sudoku puzzle.

How to run 
----------
Run the command:
```
./solve.sh <filepath>
```
Where <i>filepath</i> is the relative path to the target sudoku puzzle.

Why?
----
SAT solvers are an incredibly powerful tool. Unfortunately, generating the input is repetitive and tiresome. This 
problem is made even worse by most SAT solvers expect their input to be provided a boolean formula in the CNF 
(Conjunctive Normal Form) form. This is why we use STP, which is a SAT solver with a more user-friendly interface.

STP
---
To use STP, you declare a number of boolean variables, write down some constraints on the boolean variables
that must be true (some boolean formulas that must be true), and then STP tries to see whether it can find
any assignment to the boolean variables that makes all of the constraints true. If it can find an assignment,
it reports “Satisfiable.” and outputs a satisfying assignment; otherwise, it reports “Unsatisfiable.” 

The following is a piece on STP by Professor David Wagner:

Let’s say we want to test whether the formula (x∨ ¬y)∧(¬x∨y) is satisfiable. We’re going to introduce a
constraint that encodes this formula.
```
x, y : BOOLEAN;
ASSERT((x OR NOT(y)) AND (NOT(x) OR y));
```
Log into a Linux machine (hive1.cs.berkeley.edu - hive24.cs.berkeley.edu), store the
constraints above into an input file, say test1.in, and run the following command:
```
/home/ff/cs170/bin/easystp test1.in
```
You should get the following output:
Satisfiable.
```
ASSERT( x = FALSE );
ASSERT( y = FALSE );
```

