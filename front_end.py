############################################
#
# Jose Marcelo Sandoval-Castaneda (jms1595)
# Artificial Intelligence, Fall 2018
# 01 Nov 2018
#
############################################

import classes
import functions

# Load graph from file input.txt.
graph = classes.Graph('input.txt')

# Write key and clauses onto key.txt and clauses.txt, respectively.
functions.write_to_file('key.txt', graph.make_key())
functions.write_to_file('clauses.txt', graph.make_clauses())
