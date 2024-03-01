menu = dict({
    'pan_salado': {
        "productos": list([     
            {"nombre":"Baguette","valor":3.000},
            {"nombre":"Ciabatta","valor":3.200},
            {"nombre":"Pan de masa madre","valor":3.000},
            {"nombre":"Pan de centeno","valor":1.600},
            {"nombre":"Pan de molde","valor":1.600},
            {"nombre":"Pan pita","valor":2.500},
            {"nombre":"Bolillo","valor":3.000},
            {"nombre":"Pan de maíz","valor":3.200},
            {"nombre":"Pan de semillas","valor":2.500},
            {"nombre":"Pan de ajo","valor":1.600},
        ])
    },
    "postres":{
        "productos": list([
            {"nombre":"Tarta de manzana","valor":2.500},
            {"nombre":"Brownies","valor":1.600},
            {"nombre":"Cheesecake","valor":3.000},
            {"nombre":"Helado de vainilla","valor":1.600},
            {"nombre":"Crema catalana","valor":1.600},
            {"nombre":"Mousse de chocolate","valor":2.500},
            {"nombre":"Flan","valor":3.000},
            {"nombre":"Crepes con Nutella","valor":3.200},
            {"nombre":"Pastel de zanahoria","valor":1.600},
            {"nombre":"Profiteroles","valor":3.200},   
        ])
    },
    "cafes":{
        "productos": list([
            {"nombre":"Espresso","valor":3.000},
            {"nombre":"Latte","valor":1.600},
            {"nombre":"Cappuccino","valor":2.500},
            {"nombre":"Americano","valor":3.200},
            {"nombre":"Mocha","valor":1.600},
            {"nombre":"Affogato","valor":3.200},
            {"nombre":"Flat White","valor":1.600},
            {"nombre":"Irish Coffee","valor":1.600},
            {"nombre":"Cortado","valor":3.000},
            {"nombre":"Macchiato","valor":2.500}  
        ])
    }
})    

print("Bienvenido a la panaderia MAI")
print("1. Pan_salado")
print("2. Postres")
print("3. Cafes")

eleccion_categoria = input("seleccione el servicio que desea: ")

# entrada del usuario y ver los productos de la categoría que eligio
if eleccion_categoria in ["1", "2", "3"]:
    print("\n Productos ")
    categoria = menu[list(menu.keys())[int(eleccion_categoria) - 1]]
    for i, producto in enumerate(categoria['productos'], 1):
        print(f"{i}. {producto['nombre']}: ${producto['valor']}")

    eleccion_producto = input("Seleccione el número del producto deseado: ")

    if eleccion_producto.isdigit() and 0 < int(eleccion_producto) <= len(categoria['productos']):
        eleccion_producto = int(eleccion_producto) - 1
        producto_elegido = categoria['productos'][eleccion_producto]['nombre']
        precio_producto = categoria['productos'][eleccion_producto]['valor']

        print(f"Ha seleccionado: {producto_elegido}")
        print(f"Precio: ${precio_producto}")

        # Solicitar el monto pagado y calcular los vueltos
        monto_pagado = float(input("Ingrese el monto : "))
        vueltos = monto_pagado - precio_producto

        if  vueltos >= 0:
            print(f"Su cambio es: ${ vueltos : }")
        else:
            print("El monto pagado es insuficiente.")
    else:
        print("su eleccion no es valida")
else:
    print(" no se encontro esta categoria")

    
    
    
    
    