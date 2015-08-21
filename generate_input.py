import os
import sys

"""
"  Sudoku SAT solver input generator
" -----------------------------------
"
" This program generates the input to STP SAT solver.
"
" SAT solvers are awesome.
"
" @author: sg95
" @date: Nov 2014 - ish
"
"""

"""
" Generates the input that will be fed into the SAT solver. 
" Writes the output to SAT_inputs/<filename>.
" 
" @param puzzle
"       A list of lists representing the sudoku puzzle.
"""
def generateStr(puzzle, fp):
	op = "SAT_input/" + fp.split("puzzles/")[1]
	output = open(str(op), "w")

	line = ""
	for y in range(0, 9):
		for x in range(0, 9):
			for n in range(1, 10):
				line += "x" + str(x) + str(y) + "_" + str(n)

				if not (y == 8 and x == 8 and n == 9):
					line += ", "
				
	line += " : BOOLEAN;"
	output.write(line + "\n" * 3)

	for y in range(0, 9):
		for x in range(0, 9):
			if puzzle[y][x] != -1:
				output.write("ASSERT(" + "x" + str(x) + str(y) + "_" + str(puzzle[y][x]) + ");" + "\n")

	output.write("\n" * 3)

	# ROWS
	for y in range(0, 9):
		for x in range(0,9):
			line = "ASSERT(\n"
			for n in range(1,10):
				line += "("
				line += "x" + str(x) + str(y) + "_" + str(n) + " "
				for dx in range(1, 9):
					line += "AND NOT(x" + str((x + dx) % 9) + str(y) + "_" + str(n) + ") "

				line += ") "

				if(n != 9):
					line += "OR \n"

			line += "\n);"
			output.write(line + "\n")

	# COLUMNS
	for y in range(0, 9):
		for x in range(0, 9):
			line = "ASSERT(\n"
			for n in range(1,10):
				line += "("
				line += "x" + str(x) + str(y) + "_" + str(n) + " "
				for dy in range(1, 9):
					line += "AND NOT(x" + str(x) + str((y + dy) % 9) + "_" + str(n) + ") "

				line += ") "

				if(n != 9):
					line += "OR \n"

			line += "\n);"
			output.write(line + "\n")

	# BOXES
	for y in range(0, 9, 3):
		for x in range(0, 9, 3):
	
			for c in range(0, 9):
				boxX = c % 3
				boxY = c / 3
				line = "ASSERT(\n"
				for n in range(1,10):
					line += "("
					line += "x" + str(c % 3 + x) + str(c / 3 + y) + "_" + str(n) + " "
					for dc in range(1, 9):
						line += "AND NOT(x" + str(x + ((c + dc) % 9) % 3) + str(y + ((c + dc) % 9) / 3) + "_" + str(n) + ") "

					line += ") "

					if(n != 9):
							line += "OR \n"

				line += "\n);"
				output.write(line + "\n")
			

"""
" Given a path to a text file, creates a fills out a
" 9x9 list of lists representing the sudoku puzzle.
"
" @param filepath
"       The current puzzle that we're trying to generate input for
" @return
"       The 9x9 list of lists representing the sudoku puzzle
"""	
def createPuzzle(filepath):
    ret = []
    with open(filepath) as f:
        lines = f.readlines()
        for line in lines:
            curr = []
            for s in line.split(" "):
                curr += [s.rstrip("\n")]
            ret += [curr]
    return ret


def main(argv):
	fp = argv[1]
	puzzle = createPuzzle(fp)
	generateStr(puzzle, fp)

if __name__ == '__main__':
	main(sys.argv)






