#Libraries
import os, msvcrt
#Libraries
#MenuText
menu = """===MENU===
1. Agregar pokemon.
2. Ver pokemones.
3. Eliminar pokemon.
0. Salir."""
#MenuText
#Resources
pokemon_index = []
#Resources
#Menu
while True:
    os.system('cls')
    #-Welcome-
    print(menu)
    option = input("Ingrese opción (-): ")
    #-Welcome-
    os.system('cls')
    #-Options-
    #Option1
    if option == '1':
        print("=== AGREGAR POKEMON ===")
        #ID
        while True:
            try:
                pokemon_id = int(input("Otorge un ID al pokemon a agregar: "))
                if not pokemon_id > 0:
                    print("Error. ID debe ser mayor que 0.")
                else:
                    break
            except:
                print("Error. ID ingresado inválido.")
        print("ID guardado con éxito!")
        #ID
        #Name
        while True:
            try:
                pokemon_name = input(f"Ingrese el nombre del pokemon: ").strip().title()
                if not len(pokemon_name) > 3:
                    print("Error. Nombre debe ser igual o mayor a 4 carácteres.")
                else:
                    break
            except:
                print("Error. Nombre ingresado inválido")
        print("Nombre guardado con éxito!")
        #Name
        #Height
        while True:
            try:
                pokemon_height = float(input(f"Ingrese la altura (en metros) del pokemon: "))
                if pokemon_height > 0:
                    break
                else:
                    print("Error. Altura debe ser mayor que 0.")
            except:
                print("Error. Altura ingresada inválida")
        #Height
        #PokemonInfo
        pokemon = {
            "id": pokemon_id,
            "name": pokemon_name,
            "height": pokemon_height
        }
        #PokemonInfo
        #AddPokemonToIndex
        pokemon_index.append(pokemon)
        print("Pokemon agregado!")
    #Option1
    #Option2
    elif option == '2':
        print("=== VER POKEMONES ===")
        #PokemonIndex
        for pokemon in pokemon_index:
            print(pokemon)
        #PokemonIndex
    #Option2
    #Option3
    elif option == '3':
        print("=== ELIMINAR POKEMON ===")
    #Option3
    #Option0
    elif option == '0':
        break
    #Option0
    #OptionErrorControl
    else:
        print("Opción ingresada inválida.")
    #OptionErrorControl
    print("...Presione una tecla para continuar...")
    msvcrt.getch()
    #-Options-
#Menu