class Magia_num:
    def magia_numerica(lista):
        '''Crea una nueva lista con la suma de los números pares de la lista original
        y los números pares ordenados de mayor a menor.'''
        lista_sin_duplicados = list(set(lista))
        lista_ordenada = sorted(lista_sin_duplicados, reverse=True)
        lista_pares = [num for num in lista_ordenada if num % 2 == 0]
        suma = sum(lista_pares)
        nueva_lista = [suma] + lista_pares
        
        if suma != sum(nueva_lista[1:]):
            raise ValueError("La suma no coincide con el primer elemento")
        
        return nueva_lista
