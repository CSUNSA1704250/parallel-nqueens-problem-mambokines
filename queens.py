from typing import List
import threading

result = []
def checkRow(board, row, col, res, idx):
    for i in range(col):
        if (board[row][i]):
            res[idx] = False
            return False

def checkUpperDiag(board, row, col, res, idx):
    i = row
    j = col
    while i >= 0 and j >= 0:
        if(board[i][j]):
            res[idx] = False
            return False
        i -= 1
        j -= 1

def checkLowerDiag(board, row, col, res, idx):
    i = row
    j = col
    while j >= 0 and i < 4:
        if(board[i][j]):
            res[idx] = False
            return False
        i = i + 1
        j = j - 1

'''def isQueen_place(tabla, filas, culmnas, N):
	#Filas
	for i in range(culmnas):
		if tabla[filas][i] == 1:
			return False
	#Diagonales
	for i, j in zip(range(filas, -1, -1),range(culmnas, -1, -1)):
		if tabla[i][j] == 1:
			return False
	#Rectas
	for i, j in zip(range(filas, N, 1),range(culmnas, -1, -1)):
		if tabla[i][j] == 1:
			return False
	return True'''

functions = [
    checkRow,
    checkUpperDiag,
    checkLowerDiag
]

def multiprocess(tabla, filas, columnas):
	set_thr:List[threading.Thread] = [0, 0, 0]
	thr_res = [None, None, None]
	#print(len(set_thr))
	for idx, function in enumerate(functions):
		set_thr[idx] = threading.Thread(target=function, args=(tabla, filas, columnas, thr_res, idx))
		set_thr[idx].start()

	for idx, thread in enumerate(set_thr):
		thread.join()
		if thr_res[idx] == False: return False
	return True

def tableSolve(tabla, columnas,n):
	if (columnas == n):
		v = []
		for i in tabla:
			for j in range(len(i)):
				if i[j] == 1:
					v.append(j+1)
		result.append(v)
		return True
	res = False
	for i in range(n):
		safe = multiprocess(tabla, i, columnas)	
		if (safe):
			tabla[i][columnas] = 1
			res = tableSolve(tabla, columnas + 1, n) or res
			tabla[i][columnas] = 0
	return res

def solve_queens(n):
	result.clear()
	tabla = [[0 for j in range(n)]
		for i in range(n)]
	tableSolve(tabla, 0, n) 
	result.sort()
	return result

'''n = 4

import time

start = time.time()
res = solve_queens(n)
ellapsed = time.time() - start

print(ellapsed, res)'''