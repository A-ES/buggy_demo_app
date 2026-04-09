from flask import Flask, request, jsonify

app = Flask(__name__)

def validate_order(data):
    errors = []
    if 'item_id' not in data:
        errors.append("item_id required")
    if 'quantity' not in data or data['quantity'] <= 0:
        errors.append("quantity must be > 0")
    return errors

# BUG #3: returns 200 even on validation failure
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    errors = validate_order(data)
    if errors:
        return jsonify({"errors": errors})  # <-- missing status=422!
    order = process_order(data)
    return jsonify({"order_id": order.id})
#3 · wrong status code 200 vs 422 · line 18