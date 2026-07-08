juegos = {
    'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
    'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
    'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
    'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
    'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
    'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate'],
}

inventario = {
    'G001': [9990, 7],
    'G002': [19990, 0],
    'G003': [42990, 3],
    'G004': [14990, 5],
    'G005': [17990, 9],
    'G006': [39990, 2],
}

def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")

def stock_plataforma(plataforma):
    total_stock = 0
    plataforma_buscada = plataforma.strip().lower()
    for codigo, datos in juegos.items():
        plataforma_juego = datos[1].lower()
        if plataforma_juego == plataforma_buscada:
            if codigo in inventario:
                total_stock += inventario[codigo][1]            
    print(f"\nTotal de stock para la plataforma '{plataforma}': {total_stock}")

def busqueda_precio(p_min, p_max):
    resultados = []
    for codigo, datos_inv in inventario.items():
        precio = datos_inv[0]
        stock = datos_inv[1]
        if p_min <= precio <= p_max and stock > 0:
            if codigo in juegos:
                titulo = juegos[codigo][0]
                resultados.append(f"{titulo}--{codigo}")        
    if resultados:
        resultados.sort()
        print("\nJuegos encontrados dentro del rango de precio:")
        for juego in resultados:
            print(f"- {juego}")
    else:
        print("\nNo hay juegos en ese rango de precios.")

def buscar_codigo(codigo):
    return codigo.upper() in inventario

def actualizar_precio(codigo, nuevo_precio):
    codigo_upper = codigo.upper()
    if buscar_codigo(codigo_upper):
        inventario[codigo_upper][0] = nuevo_precio
        return True
    return False

def main():
    while True:
        print("\n========== GameHUb ==========")
        print("1. Stock por plataforma")
        print("2. Búsqueda de juegos por rango de precio")
        print("3. Actualizar precio de juego")
        print("4. Agregar juego")
        print("5. Eliminar juego")
        print("6. Salir")
        print("=====================================")
        
        opcion = leer_opcion()
        
        if opcion == 1:
            plat = input("Ingrese el nombre de la plataforma: ")
            stock_plataforma(plat)        
        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese el precio mínimo: "))
                    p_max = int(input("Ingrese el precio máximo: ")) 
                    if p_min < 0 or p_max < 0 or p_min > p_max:
                        print("Valores inconsistentes. Asegúrese de que sean mayores a 0 y que el mínimo sea menor o igual al máximo.")
                        continue 
                    busqueda_precio(p_min, p_max)
                    break
                except ValueError:
                    print("Debe ingresar valores enteros")            
        elif opcion == 3:
            while True:
                cod = input("Ingrese el código del juego: ")
                try:
                    nuevo_p = int(input("Ingrese el nuevo precio: "))
                    if nuevo_p <= 0:
                        print("El precio debe ser un número entero mayor que cero.")
                        continue     
                    if actualizar_precio(cod, nuevo_p):
                        print("Precio actualizado")
                    else:
                        print("El código no existe")        
                except ValueError:
                    print("El precio debe ser un número entero válido.")
                    continue  
                resp = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
                if resp != 's':
                    break          
        elif opcion == 4:
            print("\n--- AGREGAR NUEVO JUEGO ---")
            cod = input("Código: ").strip().upper()
            if buscar_codigo(cod):
                print("Error: El código ya existe en el sistema.")
                continue     
            titulo = input("Título: ").strip()
            if not titulo:
                print("Error: El título no debe estar vacío.")
                continue    
            plataforma = input("Plataforma: ").strip()
            if not plataforma:
                print("Error: La plataforma no debe estar vacía.")
                continue     
            genero = input("Género: ").strip()
            if not genero:
                print("Error: El género no debe estar vacío.")
                continue    
            clasificacion = input("Clasificación (E, T, M): ").strip().upper()
            if clasificacion not in ['E', 'T', 'M']:
                print("Error: La clasificación debe ser exactamente 'E', 'T' o 'M'.")
                continue    
            multi = input("¿Es multiplayer? (s/n): ").strip().lower()
            if multi not in ['s', 'n']:
                print("Error: Debe ingresar 's' o 'n'.")
                continue
            multiplayer_bool = True if multi == 's' else False
            editor = input("Editor: ").strip()
            if not editor:
                print("Error: El editor no debe estar vacío.")
                continue   
            try:
                precio = int(input("Precio: "))
                if precio <= 0:
                    print("Error: El precio debe ser un número entero mayor que cero.")
                    continue
            except ValueError:
                print("Error: El precio debe ser un número entero.")
                continue   
            try:
                stock = int(input("Stock: "))
                if stock < 0:
                    print("Error: El stock debe ser un número entero mayor o igual a cero.")
                    continue
            except ValueError:
                print("Error: El stock debe ser un número entero.")
                continue
            juegos[cod] = [titulo, plataforma, genero, clasificacion, multiplayer_bool, editor]
            inventario[cod] = [precio, stock]
            print(f"¡Juego '{titulo}' registrado con éxito!")
            
        elif opcion == 5:
            print("\n--- ELIMINAR JUEGO ---")
            cod = input("Ingrese el código del juego a eliminar: ").strip().upper()
            if buscar_codigo(cod):
                del juegos[cod]
                del inventario[cod]
                print("Juego eliminado correctamente del sistema.")
            else:
                print("El código no existe.")     
        elif opcion == 6:
            print("Saliendo del sistema... ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
