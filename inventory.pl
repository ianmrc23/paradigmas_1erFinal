% Categories
category(fruits).
category(vegetables).
category(dairy).
category(bakery).
category(beverages).

% Products
product(fruits, apple).
product(fruits, banana).
product(fruits, orange).
product(fruits, grape).
product(fruits, mango).
product(fruits, pineapple).
product(fruits, strawberry).
product(fruits, kiwi).
product(fruits, pear).
product(fruits, watermelon).
product(vegetables, carrot).
product(vegetables, lettuce).
product(vegetables, tomato).
product(vegetables, potato).
product(vegetables, onion).
product(vegetables, cucumber).
product(vegetables, broccoli).
product(vegetables, bellpepper).
product(vegetables, spinach).
product(vegetables, garlic).
product(dairy, milk).
product(dairy, cheese).
product(dairy, yogurt).
product(dairy, butter).
product(dairy, cream).
product(dairy, icecream).
product(dairy, cottagecheese).
product(dairy, sourcream).
product(dairy, creamcheese).
product(dairy, evaporatedmilk).
product(bakery, bread).
product(bakery, cake).
product(bakery, cookies).
product(bakery, croissant).
product(bakery, muffin).
product(bakery, pastry).
product(bakery, donut).
product(bakery, baguette).
product(bakery, scone).
product(bakery, brownie).
product(beverages, water).
product(beverages, coffee).
product(beverages, tea).
product(beverages, soda).
product(beverages, juice).
product(beverages, energydrink).
product(beverages, smoothie).
product(beverages, beer).
product(beverages, wine).
product(beverages, cocktail).

% Stock
stock(apple, 3).
stock(banana, 5).
stock(orange, 6).
stock(grape, 6).
stock(mango, 7).
stock(pineapple, 40).
stock(strawberry, 90).
stock(kiwi, 85).
stock(pear, 75).
stock(watermelon, 55).
stock(carrot, 120).
stock(lettuce, 110).
stock(tomato, 105).
stock(potato, 95).
stock(onion, 100).
stock(cucumber, 95).
stock(broccoli, 85).
stock(bellpepper, 80).
stock(spinach, 9).
stock(garlic, 5).
stock(milk, 65).
stock(cheese, 70).
stock(yogurt, 80).
stock(butter, 75).
stock(cream, 8).
stock(icecream, 60).
stock(cottagecheese, 70).
stock(sourcream, 90).
stock(creamcheese, 0).
stock(evaporatedmilk, 95).
stock(bread, 0).
stock(cake, 0).
stock(cookies, 0).
stock(croissant, 90).
stock(muffin, 85).
stock(pastry, 70).
stock(donut, 100).
stock(baguette, 95).
stock(scone, 80).
stock(brownie, 65).
stock(water, 150).
stock(coffee, 70).
stock(tea, 85).
stock(soda, 95).
stock(juice, 60).
stock(energydrink, 75).
stock(smoothie, 50).
stock(beer, 40).
stock(wine, 25).
stock(cocktail, 35).

% Prices
price(apple, 1.99).
price(banana, 0.59).
price(orange, 0.79).
price(grape, 2.49).
price(mango, 1.99).
price(pineapple, 2.99).
price(strawberry, 3.49).
price(kiwi, 1.29).
price(pear, 1.79).
price(watermelon, 4.99).

price(carrot, 0.99).
price(lettuce, 1.49).
price(tomato, 0.79).
price(potato, 0.89).
price(onion, 0.69).
price(cucumber, 1.29).
price(broccoli, 1.99).
price(bellpepper, 1.39).
price(spinach, 1.59).
price(garlic, 0.49).

price(milk, 2.99).
price(cheese, 3.49).
price(yogurt, 1.99).
price(butter, 2.29).
price(cream, 1.79).
price(icecream, 4.99).
price(cottagecheese, 2.49).
price(sourcream, 1.69).
price(creamcheese, 2.99).
price(evaporatedmilk, 1.89).

price(bread, 1.29).
price(cake, 19.99).
price(cookies, 2.49).
price(croissant, 1.79).
price(muffin, 1.49).
price(pastry, 2.29).
price(donut, 0.99).
price(baguette, 1.99).
price(scone, 1.29).
price(brownie, 2.99).

price(water, 0.79).
price(coffee, 2.49).
price(tea, 1.99).
price(soda, 1.29).
price(juice, 3.49).
price(energydrink, 2.99).
price(smoothie, 4.29).
price(beer, 5.99).
price(wine, 12.99).
price(cocktail, 7.49).



% Reglas para manejo de inventario

% Regla 1: Productos con baja disponibilidad (menos de 10 unidades)
low_stock(Product) :-
    stock(Product, Quantity),
    Quantity < 10.

% Regla 2: Productos de una categoría específica
products_in_category(Category, Product) :-
    product(Category, Product).

% Regla 3: Disponibilidad de un producto específico
available(Product) :-
    stock(Product, Quantity),
    Quantity > 0.

% Regla 4: Categorías con productos de baja disponibilidad
category_with_low_stock(Category) :-
    product(Category, Product),
    low_stock(Product).

% Regla 5: Productos con más de 100 unidades en stock
high_stock(Product) :-
    stock(Product, Quantity),
    Quantity > 100.

% Regla 6: Consulta de stock específico de un producto
specific_stock(Product, Quantity) :-
    stock(Product, Quantity).

% Regla 7: Productos agotados (stock igual a 0)
out_of_stock(Product) :-
    stock(Product, 0).

% Regla 8: Disponibilidad de un producto (disponible o no disponible)
availability(Product, Status) :-
    (   stock(Product, Quantity),
        Quantity > 0 ->
        Status = available
    ;   Status = not_available
    ).

% Regla 9: Productos con stock bajo y en riesgo de agotarse (menos de 5 unidades)
low_stock_and_at_risk(Product) :-
    stock(Product, Quantity),
    Quantity > 0,
    Quantity < 5.

% Regla 10: Mostrar productos con un determinado stock
products_with_stock(Quantity, Product) :-
    stock(Product, Quantity).


% Regla 1: Calcular el costo total de comprar una cantidad específica de un producto
total_cost(Product, Quantity, TotalCost) :-
    price(Product, Price),
    TotalCost is Price * Quantity.

% Regla 2: Encontrar el producto más barato dentro de una categoría
cheapest_in_category(Category, Product, Price) :-
    product(Category, Product),
    price(Product, Price),
    \+ (product(Category, Other), price(Other, OtherPrice), OtherPrice < Price).

% Regla 3: Encontrar el producto más caro dentro de una categoría
most_expensive_in_category(Category, Product, Price) :-
    product(Category, Product),
    price(Product, Price),
    \+ (product(Category, Other), price(Other, OtherPrice), OtherPrice > Price).

% Regla 4: Calcular el promedio de precios de una categoría de productos
average_price_in_category(Category, AveragePrice) :-
    findall(Price, (product(Category, Product), price(Product, Price)), Prices),
    length(Prices, Count),
    sum_list(Prices, Total),
    AveragePrice is Total / Count.

% Regla 5: Encontrar productos con precios superiores a un valor dado
products_above_price(PriceLimit, ProductList) :-
    findall(Product-Price, (price(Product, Price), Price > PriceLimit), ProductList).

