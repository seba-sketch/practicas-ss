
lado_cuadrado = input("Dame una longitud para un cuadrado: ")
Area_cuadrado = lado_cuadrado * lado_cuadrado
Area_cuarto_de_circulo = (pi * lado_cuadrado * lado_cuadrado)/4
raiz_de_dos = math.sqrt(2)
Diagonal_cuadrado_pequeño = lado_cuadrado * raiz_de_dos - lado_cuadrado
Area_cuadro_chico = (Diagonal_cuadrado_pequeño * Diagonal_cuadrado_pequeño)2
Area_2S = Area_cuadrado - Area_cuarto_de_circulo - Area_cuadro_chico
Area_S = Area_2S/2
print("El area de S es: ", Area_S)
