def casting():
    precio = int(input("precio: "))
    descuento = float(input("descuento: "))
    cantidad = int(input("cantidad: "))
    precio_descuento = (precio - descuento)
    total = precio_descuento * cantidad
    print(precio)
    print(descuento)
    print(cantidad)
    print(total)