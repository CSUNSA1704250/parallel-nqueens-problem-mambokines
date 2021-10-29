from tragatraking import queens
from typing import List, Tuple
import sys, getopt

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
    '''problemType = ''
    n = ''
    try:
        opts, args = getopt.getopt(argv,"problemType:N:")
    except getopt.GetoptError:
        print('test.py -problemType [find, all] -N <queens>')
        sys.exit(2)
    print(opts, args, argv)

    for opt, arg in opts:
        if opt == '-h':
            print('test.py -problemType [find, all] -N <queens>')
            sys.exit()
        elif opt in ("-problemType"):
            problemType = arg
        elif opt in ("-N"):
            n = int(arg)'''
    #print(problemType)
    #print(n)
    
    tabla = [0] * N
    for i in range(N):
        tabla[i] = [0] * N
    
    queens(tabla, N, problemType)


if __name__ == "__main__":
    main(sys.argv[1:])