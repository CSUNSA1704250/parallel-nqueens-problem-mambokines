from queens import *
from graficar import *
from typing import List, Tuple
import sys, getopt

def entries(tabla_res, N, out_type):
    res = solve_queens(N)
    print(res)
    for j in range(N):
        a = int(res[0][j])
        tabla_res[j][a-1]=1
    print(tabla_res)
    if out_type == 'find':
        print('find: ')
        print_graph(tabla_res, N)
    elif out_type == 'all':
        print('all: ')
        print_tabla(tabla_res, N)
    else:
        raise Exception('Seleccione un tipo')
    return True


def main(argv):
    problemType = None
    N = None
    for idx, arg in enumerate(argv):
        if arg == '-problemType':
            problemType = argv[idx+1]
        if arg == '-N':
            N = argv[idx+1]

    if problemType is None or N is None:
        print('test.py -problemType [find, all] -N <queens>')
        sys.exit(2)
    
    print(problemType)
    try:
        N = int(N)
    except:
        print('N debe ser un numero')
        sys.exit(2)
    
    tabla = [0] * N
    for i in range(N):
        tabla[i] = [0] * N
    
    entries(tabla, N, problemType)


if __name__ == "__main__":
    main(sys.argv[1:])