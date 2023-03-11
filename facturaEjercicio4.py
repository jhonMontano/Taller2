invoices = {}

while True:
    print("\nQué quieres hacer?")
    print("1. Agregar una nueva factura")
    print("2. Pagar una factura existente")
    print("3. Salir")

    choice = input("Ingresa tu elección (1-3): ")

    if choice == "1":
        invoice_number = input("Ingresa el numero de factura: ")
        if invoice_number in invoices:
            print("La factura ya esta registrada.")
        else:
            invoice_cost = float(input("Ingresa el costo de la factura: "))
            invoices[invoice_number] = invoice_cost
            print(f"Factura {invoice_number} agregada exitosamente. Importe total pendiente: {sum(invoices.values())}")

    elif choice == "2":
        invoice_number = input("Ingrese el numero de la factura a pagar: ")
        if invoice_number in invoices:
            invoice_cost = invoices.pop(invoice_number)
            print(f"Factura {invoice_number} pagada. Cantidad total recaudado hasta el momento: {sum(invoices.values())}")
        else:
            print("Factura no encontrada.\n")

    elif choice == "3":
        break

    else:
        print("Elección invalida.")
    
print(f"Cantidad total recaudado: {sum(invoices.values())}")
print(f"Importe total pendiente: {0}")