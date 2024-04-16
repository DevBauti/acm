import hashlib

hash_file = '2e530316cd3840ce8c3006953374c95e0df5aee3d974cfbe856e934fec40e45f'#pipo

dic_hash = input("agregar diccionario... proximamente")

with open(dic_hash, 'r') as file:
    
    folder = [line.strip() for line in file]
    for password in folder:
        hash_calc = hashlib.sha256(password.encode()).hexdigest()

        if hash_calc == hash_file:
            print('la contraseña es: '+ hash_calc)
            break
        else:
            print('No se encontro coincidencia')


"""
Hay muchisimo por hacer en esto, de puede hacer un servicio, creo, vere.
"""