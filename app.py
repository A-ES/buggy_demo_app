def calculate_discount(price, quantity):
    avg = price / max(quantity, 1)       # <-- prevent division by zero
    if avg > 100:
        return 0.2
    return 0.1

@app.route('/cart')
def cart():
    total = calculate_discount(500, 0)  # crashes here
    return jsonify({"discount": total})

if __name__ == '__main__':
    app.run(debug=True)