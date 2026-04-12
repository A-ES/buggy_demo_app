def calculate_discount(price, quantity):
    if quantity == 0:
        return 'Quantity cannot be zero'
    return (1 - (quantity / 100)) * price