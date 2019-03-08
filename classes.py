############################################
#
# Jose Marcelo Sandoval-Castaneda (jms1595)
# Artificial Intelligence, Fall 2018
# 01 Nov 2018
#
############################################


# Graph interpreter used in front_end.py.
class Graph:
    # Build graph from file.
    def __init__(self, file_name):
        with open(file_name) as f:
            self.num_vertices = f.readline()
            self.vertices = []
            self.connections = {}
            for line in f:
                elements = line.strip().split(' ')
                for el in elements:
                    if el not in self.vertices:
                        self.vertices.append(el)
                        self.connections[el] = []
                self.connections[elements[0]].append(elements[1])

    # Build a string of keys.
    def make_key(self):
        key = ''
        i = 1
        for vertex in self.vertices:
            j = 1
            for _ in self.vertices:
                key += str(i) + ' ' + vertex + ' ' + str(j) + '\n'
                j += 1
                i += 1

        return key[:-1]

    # Build a string of clauses.
    def make_clauses(self):
        # Load keys.
        key = self.make_key().strip().split('\n')
        key_list = []
        for line in key:
            line = line.split(' ')
            line = [''.join([line[1], line[2]]), line[0]]
            key_list.append(line)

        # Create clauses.
        clauses = ''

        # Clauses from proposition 1.
        for vertex in self.vertices:
            i = 1
            clause = ''
            for _ in self.vertices:
                clause += vertex + str(i) + ' '
                i += 1
            clauses += clause[:-1] + '\n'

        # Clauses from proposition 2.
        pairs_seen = []
        for vertex_1 in self.vertices:
            for vertex_2 in self.vertices:
                seen = False
                for pair in pairs_seen:
                    if vertex_1 in pair and vertex_2 in pair:
                        seen = True
                if vertex_1 == vertex_2 or seen:
                    continue
                i = 1
                for _ in self.vertices:
                    clauses += '-' + vertex_1 + str(i) + ' -' + vertex_2 + str(i) + '\n'
                    i += 1
                    pairs_seen.append([vertex_1, vertex_2])

        # Clauses from proposition 3.
        for vertex_1 in self.vertices:
            for vertex_2 in self.vertices:
                if vertex_1 == vertex_2:
                    continue
                if vertex_2 in self.connections[vertex_1]:
                    continue
                for i in range(1, len(self.vertices)):
                    clauses += '-' + vertex_1 + str(i) + ' -' + vertex_2 + str(i + 1) + '\n'

        # Clauses from optional proposition 1.
        for i in range(1, len(self.vertices) + 1):
            clause = ''
            for vertex in self.vertices:
                clause += vertex + str(i) + ' '
            clauses += clause[:-1] + '\n'

        # Clauses from optional proposition 2.
        for vertex in self.vertices:
            for i in range(1, len(self.vertices) + 1):
                for j in range(i + 1, len(self.vertices) + 1):
                    clauses += '-' + vertex + str(i) + ' -' + vertex + str(j) + '\n'

        clauses += '0'
        for key in key_list:
            clauses = clauses.replace(key[0], key[1])

        return clauses
