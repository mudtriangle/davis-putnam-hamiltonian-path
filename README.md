# Davis-Putnam Hamiltonian Path
Solution to Programming Assignment 3 of Artificial Intelligence in NYU New York. It uses the Davis-Putnam algorithm to solve the Hamiltonian path problem. Full description of the assignment is on the _assignment.pdf_ file.

## Details
Tested using Python 3.6.1 (Anaconda version).\
No external libraries required.\
`front_end.py` reads the input from `input.txt` and outputs at `key.txt` and `clauses.txt`.\
`davis_putnam.py` reads the input from `clauses.txt` and outputs at `dp-output.txt`.\
`back_end.py` reads the input from `dp-output.txt` and `key.txt` and outputs at `output.txt`.\
Files `functions.py` and `classes.py` contain supporting functions and data structures for the main files, `front_end.py`, `davis_putnam.py`, and `back_end.py`.\
`main.py` runs `front_end.py`, `davis_putnam.py`, and `back_end.py`.

## How to Run
To run the entire algorithm, `python main.py`.\
To run the individual programs:\
`python front_end.py`\
`python davis_putnam.py`\
`python back_end.py`
