# Paradigmas 2do Parcial

## Estructura del Proyecto

```sh
    ├── auth
    │   └── auth.py
    │
    ├── components
    │   ├── add_menu.py
    │   ├── cart_menu.py
    │   └── check_menu.py
    │
    ├── db
    │   ├── db_init.py
    │   ├── inventory.pickle
    │   ├── test@test.com
    │   └── inventory.txt
    │
    ├── schemas
    │   ├── client_manager.py
    │   ├── polymorphism.py
    │   └── product_manager.py
    │
    ├── utils
    │    ├── menu_table.py
    │    └── os_utils.py
    │
    ├── main.py
    └── README.md
```

## Pasos para Ejecutar el Proyecto

1. Asegúrate de tener `Python3` o una versión superior instalado en tu sistema:

```sh
python --version
git --version
```

2. Descarga el proyecto desde GitHub:

```sh
git clone https://github.com/ianmrc23/paradigmas-2do-Parcial.git .
```

3. Navega hasta la ubicación donde has descargado el proyecto (eliminar la carpeta .git es opcional):

```sh
cd paradigmas-2do-Parcial
rm -rf .git
```

4. Ejecuta el archivo `main.py`:

```sh
python3 main.py
```

## Uso del Programa

### Guía Rápida de Indicadores

```sh
[*]: Se espera una entrada por teclado.
[+]: Mensajes de éxito.
[-]: Mensajes de advertencia o error.
```

### Mensajes Comunes:

```sh
[*] Press RETURN to continue:
[-] Invalid choice. Please enter a valid option:
```

### Primera Ejecución

Si es la primera vez que ejecutas el programa verás algo así:

```sh
[+] Inventory data has been saved as inventory.pickle
[*] Press RETURN to continue
```

Esto ocurre ya que no se encontró el archivo `inventory.pickle` que sirve para la persistencia
de datos de los productos, por lo tanto se crea uno nuevo.

Después aparecerá el banner auspiciado por ChatGPT.

Luego verás el primer menú con las siguientes opciones:

```sh
╔════════════════════════════════════════════════════╗
║                     AUTH MENU                      ║
╠════════════════════════════════════════════════════╣
║   1. Register                                      ║
║   2. Login                                         ║
║   3. Exit                                          ║
╚════════════════════════════════════════════════════╝
```

Si no has creado ningún usuario, elige la opción `1` para crear tu usuario:

```sh
[*] Enter the NUMBER of your choice: 1
[*] Enter your ID: 1
[*] Enter your name: test
[*] Enter your email: test@test.com
[*] Enter your password: 1234
[*] Enter your address: paraguay
[*] Enter your distance from the store: 10
[+] User test has been registered successfully!
```

Si ya tienes usuario, elige la opción `2` para iniciar sesión:

```sh
[*] Enter the NUMBER of your choice: 2
[*] Enter your email: test@test.com
[*] Enter your password: 1234
[+] Welcome back, test!
```

Luego aparecerá el menú principal:

```sh
╔════════════════════════════════════════════════════╗
║                     MAIN MENU                      ║
╠════════════════════════════════════════════════════╣
║   1. Add Product                                   ║
║   2. My Cart                                       ║
║   3. Checkout                                      ║
║   4. Profile                                       ║
║   5. Exit                                          ║
╚════════════════════════════════════════════════════╝
```

Primero agregaremos un producto a nuestro carrito, eligiendo la opción `1`:

```sh
╔════════════════════════════════════════════════════╗
║                AVAILABLE CATEGORIES                ║
╠════════════════════════════════════════════════════╣
║   1. Fruits                                        ║
║   2. Vegetables                                    ║
║   3. Dairy                                         ║
║   4. Bakery                                        ║
║   5. Beverages                                     ║
╚════════════════════════════════════════════════════╝
```

Se nos mostrarán las categorías disponibles, y una vez más elegimos una de las opciones:

```sh
╔════════════════════════════════════════════════════╗
║                  Category: Fruits                  ║
╠════╦═══════════════════════════╦═══════╦═══════════╣
║ ID ║       Product Name        ║ Stock ║   Price   ║
╠════╬═══════════════════════════╬═══════╬═══════════╣
║ 1  ║ Apple                     ║ 50    ║ $1.99     ║
║ 2  ║ Banana                    ║ 100   ║ $0.59     ║
║ 3  ║ Orange                    ║ 80    ║ $0.79     ║
║ 4  ║ Grape                     ║ 60    ║ $2.49     ║
║ 5  ║ Mango                     ║ 70    ║ $1.99     ║
║ 6  ║ Pineapple                 ║ 40    ║ $2.99     ║
║ 7  ║ Strawberry                ║ 90    ║ $3.49     ║
║ 8  ║ Kiwi                      ║ 85    ║ $1.29     ║
║ 9  ║ Pear                      ║ 75    ║ $1.79     ║
║ 10 ║ Watermelon                ║ 55    ║ $4.99     ║
╚════╩═══════════════════════════╩═══════╩═══════════╝
```

Esta vez se muestran los productos con su stock disponible y precio de la categoría seleccionada.
Ahora elige qué producto agregar a tu carrito:

```sh
[*] Enter the ID of the product you want or 0 to go back: 1
[*] Enter the number of Apple's you want or 0 to go back: 20
[+] 20 Apple's have been added to your cart.
```

Ingrese `0` para volver y de nuevo otro `0` para volver al menú principal.

Si quieres ver tu información, elige la opción `4` y verás algo así:

```sh
╔════════════════════════════════════════════════════╗
║                 CLIENT INFORMATION                 ║
╠════════════════════╦═══════════════════════════════╣
║   Client ID        ║ 1                             ║
║   Client Name      ║ test                          ║
║   Client Email     ║ test@test.com                 ║
║   Client Password  ║ 1234                          ║
║   Client Address   ║ paraguay                      ║
║   Client Distance  ║ 10.0                          ║
╚════════════════════╩═══════════════════════════════╝
```

Si quieres salir del programa, elige la opción `5`:

```sh
[+] Thank you for visiting us! We hope to see you again soon!
```

Ahora veremos el menú `My Cart` con la opción `2`:

```sh
╔════════════════════════════════════════════════════╗
║                     CART MENU                      ║
╠════════════════════════════════════════════════════╣
║   1. View Cart                                     ║
║   2. Remove Item                                   ║
║   3. Clear Cart                                    ║
╚════════════════════════════════════════════════════╝
```

Si quieres ver los productos en tu carrito, elige la opción `1`:

```sh
╔════════════════════════════════════════════════════╗
║                     Your Cart                      ║
╠══════════════════════╦════════════╦════════════════╣
║ Product Name         ║  Quantity  ║      Price     ║
╠══════════════════════╬════════════╬════════════════╣
║ Apple                ║  20        ║ $ 39.8         ║
╠══════════════════════╩════════════╩════════════════╣
║ Total Price:                        $ 39.80        ║
║ Total Weight:                      Kg 10.00        ║
╚════════════════════════════════════════════════════╝
```

Eliminar un producto específico? Opción `2`. Eliminar todos los productos? Opción `3`.

Por último, veremos el `checkout`, que es la opción `3` del menú principal.
Tendrás tres tipos de pago para elegir:

```sh
╔════════════════════════════════════════════════════╗
║                   CHECKOUT MENU                    ║
╠════════════════════════════════════════════════════╣
║   1. Pay with Cash                                 ║
║   2. Pay with Card (30% discount)                  ║
║   3. Pay with QR (10% discount)                    ║
╚════════════════════════════════════════════════════╝
```

Y tres tipos de envío:

```sh
╔════════════════════════════════════════════════════╗
║                  SHIPPING METHODS                  ║
╠════════════════════════════════════════════════════╣
║   1. Standard Shipping                             ║
║   2. Express Shipping                              ║
║   3. In-Store Pickup                               ║
╚════════════════════════════════════════════════════╝
```

Si todo salió bien, verás algo así:

```sh
[+] Total amount with discount: 39.80$
[+] Shipping cost: 0.00$
[+] Total amount with shipping: 39.80$
[+] Thank you for shopping in our store! Have a nice day.
```

Con esto hemos explorado la mayoría de las funciones disponibles. Espero que te haya gustado! Gracias por llegar hasta aquí.
