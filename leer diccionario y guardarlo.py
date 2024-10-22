import pickle
from pathlib import Path

# Create an empty dictionary
d = dict()

# Ask for file name to load dictionary from
file_name = input ("Introducte el nombre del archivo de datos: ")

# Comprobamos que existe
path = Path(file_name)
if path.is_file():
    # Open file in reading mode
    input_file = open(file_name, 'rb')
    d = pickle.load(input_file)
    # Close de file
    input_file.close()
else:
    print ("El archivo o file no existe, creamos diccionario vacío")

#Check for values or add new ones

document_number = input("Introduce un documento de identidad: ")

if document_number in d: # Check wether it is on dict or not
        print("La edad de " + document_number + " es " + str(d[document_number]))
else:
     age = input("Documento no existente. Introduce edad: ")
     if age.isnumeric():
          
            num = int(age)
            d[document_number] = num
            print ("Añadido al diccionario")


# Save dict on file and close
output_file = open(file_name, 'wb')
pickle.dump(d, output_file)
output_file.close()

# read python dict from a file
#pkl_file = open('myfile.pkl', 'rb')
#mydict2 = pickle.load(pkl_file)
#pkl_file.close()

# write python dict to a file
#mydict = {'a': 1, 'b': 2, 'c': 3}
#output = open('myfile.pkl', 'wb')
#pickle.dump(mydict, output)
#output.close()