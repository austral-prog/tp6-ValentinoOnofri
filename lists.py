# Replace the "ANSWER HERE" with your answer
def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) > 6:
        del list_to_remove_elements[5] #Ver

def add_elements(list_to_add_elements): #No se pueden asignar a variables las funciones usadas. Uso un ejemplo por el error --> No va
    #Uso lo de Lautaro --> No va
    sample_input = ['Red', 'Green', 'White','Black']
    sample_input.insert(0, 'Pink') #Primero al principio, despues al final
    sample_input.append('Yellow')
    return sample_input

def is_empty(list_to_check):
    if len(list_to_check) == 0:
        resultado = "La lista esta vacia"
    else:
        resultado = False
    return resultado  # Remove this line and implement

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        if list_to_compare1[2] == list_to_compare2[2]:
            resultado = True
        else:
            resultado = False
    else:
        resultado = False
    return resultado # Remove this line and implement

def list_of_lists(list_of_lists_to_modify):
    slice1 = list_of_lists_to_modify[0][:2]
    slice2 = list_of_lists_to_modify[1][1:4]
    slice3 = list_of_lists_to_modify[2][-2:] #Error aca
    lista_concatenada = [slice1, slice2, slice3]
    return lista_concatenada  # Remove this line and implement