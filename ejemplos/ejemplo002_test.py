from ejemplos.ejemplo002 import Medicamento

# La siguiente linea me genera una excepcion porque estoy intentado
# crear un objeto sin los parametros requeridos por el constructor
# de la clase Medicamento
# dolofin = Medicamento()
dolofin = Medicamento("Dolofin", "Dolores")
print(dolofin.nombre_generico)
print(dolofin.descripcion)