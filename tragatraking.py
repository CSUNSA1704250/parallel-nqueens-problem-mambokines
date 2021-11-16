import os, sys
import graphviz 

def print_graph(tabla,N):
	file = open("tablero.dot", "w")
	file.write("digraph G { bgcolor=\"white\" style=\"filled\" \n subgraph cluster1 {fillcolor=\"white\" style=\"filled\" \n node [shape=square fillcolor=\"white\" style=\"radial\" gradientangle=180] \n a0 [label=< \n <TABLE border=\"10\" cellspacing=\"10\" cellpadding=\"10\" style=\"rounded\" bgcolor=\"white\" gradientangle=\"315\">")
	for i in range(N):
		file.write("<TR>")
		for j in range(N):
			if tabla[i][j] == 0:
				file.write("<TD border=\"3\"  bgcolor=\"white\" gradientangle=\"315\">0</TD>\n")
			else:
				file.write("<TD border=\"3\"  bgcolor=\"gold\" gradientangle=\"315\">1</TD>\n")
		file.write("</TR>\n")
	file.write("</TABLE>>];}}")
	file.close()
	os.system("dot -Tpng tablero.dot -o q.png")

def print_tabla(tabla,N):
	file = open("solutions.txt", "w")
	reina = 1
	file.write("--------------------------------------------------------------------- \n BEGIN FILE solutions.txt \n ___________________________________________ \n #Solutions for <n_queens> queens#Solutions for ")
	file.write(str(N))
	file.write("queens\n")
	for i in range(N):
		for j in range(N):
			if tabla[i][j]== 1:
				file.write("<pos_queen_nmro ")   
				file.write(str(reina))
				file.write("_fila ")
				file.write(str(i))
				file.write("> <pos_queen_columna ")
				file.write(str(j))
				file.write("\n")
				reina+=1
	file.write("--------------------------------------------------------------------- \n END FILE solutions.txt \n ___________________________________________")
	file.close()

def isQueen_place(tabla, filas, culmnas,N):
	for i in range(culmnas):
		if tabla[filas][i] == 1:
			return False
	for i, j in zip(range(filas, -1, -1),range(culmnas, -1, -1)):
		if tabla[i][j] == 1:
			return False
	for i, j in zip(range(filas, N, 1),range(culmnas, -1, -1)):
		if tabla[i][j] == 1:
			return False
	return True

def tablero(tabla, culmnas, N):
	if culmnas >= N:
		return True
	for i in range(N):
		if isQueen_place(tabla, i, culmnas,N):
			tabla[i][culmnas] = 1
			if tablero(tabla, culmnas + 1,N) == True:
				return True
			tabla[i][culmnas] = 0

def queens(tabla, N, out_type):
	if tablero(tabla, 0, N) == False:
		print ("No existe")
		return False
	if out_type == 'find':
		print_graph(tabla,N)
	elif out_type == 'all':
		print_tabla(tabla,N)
	else:
		raise Exception('Seleccione un tipo')
	return True

'''N = int(input("tamanho tablero: "))
#tabla = crear_tablero(N)
tabla = [0] * N

for i in range(N):
    tabla[i] = [0] * N

queens(tabla, N)'''


