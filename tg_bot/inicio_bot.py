def busca_arreglo(busca): #el peor ejemplo
       print(f"Buscando arreglo : {busca}")
       arreglo_palabras = ["rojo", "verde", "azul", "negro", "morado"]

       for item in arreglo_palabras:
              print(f"palabra : {item}")
              if busca == item:
                     print("Palabra encontrada")
                     return "Encontrada en el arreglo"
       return "No se encontro en el arreglo"
"""
    #if busca in arreglo_palabras:
     #  print ("tambien lo encontre")
     
     def busca_in_file(busca):
        file = open('palabras.txt', 'r')
        if busca in file.read():
               print("Lo encontre con file read")
               return 1
        file = open('groserias.txt', 'r')
        if busca in file.read():
               print("\n\t\tlo encontre c on file read")
               return 3
        file.close()
        return False
def busca_with_file(buscas):
       with open('palabras .txt') as file:
              data = True
              while data:
              data = file.readline()
              print(data)
              texto = "Micasa es grren"

              texto_analizar = texto.split()
              print(texto_analizar)
              for item in texto_analizar:
                     print(f"analizando{item}")
                     analisis = busca_arreglo(item)
                     if not analisis:
                            print("El texto contiene algo invalido")
                print(busca_in_file(item))

file = open('palabras.txt', 'r')
print(file)
print(type(file))
print(dir(file))
print(file.read)

print("lo ebcontre con")

file.close()"
"""