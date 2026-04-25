def find_top_seller(products: dict, sales: dict) -> str:
    max_revenue = 0
    top_seller = ""
    
    for product, price in products.items():
        revenue = price * sales.get(product, 0)
        if revenue > max_revenue:
            max_revenue = revenue
            top_seller = product
            
    return top_seller


print(find_top_seller(
    {"Olma": 5000, "Banan": 8000, "Uzum": 7000},
    {"Olma": 10,   "Banan": 5,    "Uzum": 8}
))
# Kutilgan natija: "Uzum"