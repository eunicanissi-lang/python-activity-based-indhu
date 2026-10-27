
TAX_RATES = {
    "Electronics": 18,
    "Clothing": 5,
    "Groceries": 0,
    "Furniture": 12
}
DISCOUNT_THRESHOLD = 5000
THRESHOLD_DISCOUNT = 10
MAX_DISCOUNT = 1000
def calculate_bill(products):
    subtotal = 0
    total_tax = 0
    invoice = []
    for product in products:
        name = product["name"]
        category = product["category"]
        price = product["price"]
        quantity = product["quantity"]
        if price < 0 or quantity <= 0:
            raise ValueError("Price must be non-negative and quantity positive.")
        if category not in TAX_RATES:
            raise ValueError(f"Invalid category: {category}")
        item_total = price * quantity
        tax_rate = TAX_RATES[category]
        item_tax = item_total * tax_rate / 100

        subtotal += item_total
        total_tax += item_tax
        invoice.append({
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity,
            "item_total": item_total,
            "tax_rate": tax_rate,
            "tax": item_tax
        })
    discount = 0
    if subtotal >= DISCOUNT_THRESHOLD:
        discount = subtotal * THRESHOLD_DISCOUNT / 100
    discount = min(discount, MAX_DISCOUNT)
    for item in invoice:
        if subtotal > 0:
            item_discount = discount * item["item_total"] / subtotal
        else:
            item_discount = 0
        item["discount"] = item_discount
        item["final_amount"] = (
            item["item_total"] - item_discount + item["tax"]
        )
    grand_total = subtotal - discount + total_tax
    return invoice, subtotal, discount, total_tax, grand_total
def main():
    products = []
    n = int(input("Enter number of products: "))
    if n <= 0:
        print("Number of products must be positive.")
        return
    print("\nAvailable categories:", ", ".join(TAX_RATES))
    for i in range(n):
        print(f"\nProduct {i + 1}")
        name = input("Enter product name: ")
        category = input("Enter category: ").strip().title()
        try:
            price = float(input("Enter unit price (Rs.): "))
            quantity = int(input("Enter quantity: "))
            products.append({
                "name": name,
                "category": category,
                "price": price,
                "quantity": quantity
            })
        except ValueError:
            print("Invalid price or quantity. Please enter numeric values.")
            return
    try:
        invoice, subtotal, discount, tax, grand_total = calculate_bill(
            products
        )
    except ValueError as error:
        print("Error:", error)
        return
    print("\n" + "=" * 88)
    print("                         RETAIL STORE INVOICE")
    print("=" * 88)
    print(
        f"{'Product':<16}{'Category':<14}{'Qty':>5}"
        f"{'Unit Price':>12}{'Amount':>12}{'Tax':>10}"
        f"{'Discount':>12}"
    )
    print("-" * 88)
    for item in invoice:
        print(
            f"{item['name']:<16}"
            f"{item['category']:<14}"
            f"{item['quantity']:>5}"
            f"{item['price']:>12.2f}"
            f"{item['item_total']:>12.2f}"
            f"{item['tax']:>10.2f}"
            f"{item['discount']:>12.2f}"
        )
    print("-" * 88)
    print(f"{'Subtotal:':>65} Rs. {subtotal:>10.2f}")
    print(f"{'Total Tax:':>65} Rs. {tax:>10.2f}")
    print(f"{'Total Discount:':>65} Rs. {discount:>10.2f}")
    print("=" * 88)
    print(f"{'GRAND TOTAL:':>65} Rs. {grand_total:>10.2f}")
    print("=" * 88)
if __name__ == "__main__":
    main()
