# import milibreria

# Librerias no hacen nada a menos que las importes
#milibreria.lee_archivo()
print("File one __name__ is set to: {}" .format(__name__))
from dos import saluda

def main():
    saluda()

if __name__ == "__main__":
    main()