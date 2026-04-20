function calculate_discount(price: number, quantity: number): number | string {
    if (!quantity) {
        return 'Quantity cannot be zero.';
    }
    const discount = price * (0.1 * quantity);
    return discount;
}
