def busca_arreglo(busca): #el peor ejemplo
       print(f"Buscando arreglo : {busca}")
       arreglo_palabras = ["rojo", "verde", "azul", "negro", "morado"]

       for item in arreglo_palabras:
              print(f"palabra : {item}")
              if busca == item:
                     print("Palabra encontrada")
                     return "Encontrada en el arreglo"
       return "No se encontro en el arreglo"
