import parser as parser

print("Bienvendio al Parser")
print("Ingrese el nombre del archivo a leer")
archivo = input()+'.txt'
print(parser.leer_archivo(archivo))