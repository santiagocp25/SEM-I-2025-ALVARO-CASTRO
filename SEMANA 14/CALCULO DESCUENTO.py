def calcular_descuento(monto_total, porcentaje_descuento=10):

    # Convertir porcentaje a decimal
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

def main():
    # Primera llamada: porcentaje (10%)
    monto1 = 200.0
    descuento1 = calcular_descuento(monto1)
    monto_final1 = monto1 - descuento1
    print(f"Monto original: {monto1}")
    print(f"Descuento aplicado (usando porcentaje por defecto): {descuento1:.2f}")
    print(f"Monto final a pagar: {monto_final1:.2f}")
    print("---")

    # Segunda llamada: porcentaje (25%)
    monto2 = 300.0
    porcentaje2 = 15
    descuento2 = calcular_descuento(monto2, porcentaje2)
    monto_final2 = monto2 - descuento2
    print(f"Monto original: {monto2}")
    print(f"Descuento aplicado ({porcentaje2}%): {descuento2:.2f}")
    print(f"Monto final a pagar: {monto_final2:.2f}")


if __name__ == "__main__":
    main()
