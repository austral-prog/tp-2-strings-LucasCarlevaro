def casting():
    precio = input()
    descuento = input()
    cantidad = input()

    precio_descuento = int(precio) - float(descuento)
    total = precio_descuento * int(cantidad)

    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precio_descuento}")
    print(f"Total: {total}")