
precio = {"manzana": 2.5, "banano": 1.5, "naranja": 3.0, "pera": 2.0}

# Ask user for a fruit and a number of kilos
fruta = input("\nIngrese una fruta: ")
kilos = float(input("\nIngrese el numero de kilos: "))

# Check if the fruit is in the dictionary
if fruta in precio:
    # Calculate the price and display it
    precio = precio[fruta] * kilos
    print(f"\nEl precio de {kilos} kilos de {fruta} es {precio:.2f} dolares.\n")
else:
    # If the fruit is not in the dictionary, ask user to add it
    print(f"\n{fruta} no esta en la lista de frutas.\n")
    agregar_fruta = input("Quieres agregarla? (s/n): \n")
    if agregar_fruta.lower() == "s":
        price = float(input("Ingrese el precio de la fruta: \n"))
        precio[fruta] = precio
        print(f"{fruta} ha sido agregada a la lista de frutas con un precio de {price:.2f} dolares'n.")


