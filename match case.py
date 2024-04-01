def calcular_total_sin_descuento(cantidad):
    precio_unitario_con_iva = 80000 * 1.16  # Precio unitario con IVA
    total_sin_descuento = cantidad * precio_unitario_con_iva
    return total_sin_descuento

def aplicar_descuento(total_sin_descuento, forma_pago):
    descuento = match forma_pago.upper():
        case 'E':
            total_sin_descuento * 0.05
        case 'T':
            total_sin_descuento * 0.10
        case 'C':
            total_sin_descuento * 0.15
        case _:
            raise ValueError("Forma de pago no válida")
    total_con_descuento = total_sin_descuento - descuento
    return descuento, total_con_descuento

def imprimir_detalle(cantidad, forma_pago, total_sin_descuento, descuento, total_con_descuento):
    print("\nDetalle del pago:")
    print("Cantidad de impresoras a comprar:", cantidad)
    print("Precio unitario de la impresora (con IVA): $80000")
    print("Total sin descuento: $", total_sin_descuento)
    print("Forma de pago:", forma_pago)
    print("Descuento realizado: $", descuento)
    print("Total a pagar: $", total_con_descuento)

cantidad_str = input("Ingrese la cantidad de impresoras a comprar: ")
cantidad = match cantidad_str.isdigit():
    case True:
        int(cantidad_str)
    case False:
        print("Error: La cantidad de impresoras debe ser un número entero.")
        exit()

forma_pago = input("Ingrese la forma de pago (Efectivo=E, Tarjeta=T, Cheque=C): ")
if forma_pago.upper() not in {'E', 'T', 'C'}:
    print("Error: Forma de pago no válida.")
    exit()

cantidad = int(cantidad_str)
total_sin_descuento = calcular_total_sin_descuento(cantidad)
descuento, total_con_descuento = aplicar_descuento(total_sin_descuento, forma_pago)
imprimir_detalle(cantidad, forma_pago.upper(), total_sin_descuento, descuento, total_con_descuento)
