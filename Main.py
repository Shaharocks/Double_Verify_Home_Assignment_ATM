from flask import Flask, request, jsonify
import os

# Create Flask application
app = Flask(__name__)

# In-memory storage for accounts
# Format: {account_number: {"balance": amount}}
accounts = {
    "12345": {"balance": 1000.0},
    "67890": {"balance": 500.0},
    "11111": {"balance": 250.75}
}


# Basic route to test if server is running
@app.route('/')
def home():
    return jsonify({
        "message": "ATM Server is running!",
        "endpoints": [
            "GET /accounts/{account_number}/balance",
            "POST /accounts/{account_number}/withdraw",
            "POST /accounts/{account_number}/deposit"
        ]
    })


# GET /accounts/{account_number}/balance
@app.route('/accounts/<account_number>/balance', methods=['GET'])
def get_balance(account_number):
    # Check if account exists
    if account_number not in accounts:
        return jsonify({
            "error": "Account not found",
            "account_number": account_number
        }), 404

    # Return the balance
    return jsonify({
        "account_number": account_number,
        "balance": accounts[account_number]["balance"]
    }), 200


# POST /accounts/{account_number}/withdraw
@app.route('/accounts/<account_number>/withdraw', methods=['POST'])
def withdraw_money(account_number):
    # Check if account exists
    if account_number not in accounts:
        return jsonify({
            "error": "Account not found",
            "account_number": account_number
        }), 404

    # Get the amount from the request body
    data = request.get_json()
    if not data or 'amount' not in data:
        return jsonify({
            "error": "Amount is required",
            "example": {"amount": 100.50}
        }), 400

    amount = data['amount']

    # Validate amount
    if not isinstance(amount, (int, float)) or amount <= 0:
        return jsonify({
            "error": "Amount must be a positive number"
        }), 400

    current_balance = accounts[account_number]["balance"]

    # Check if sufficient funds
    if amount > current_balance:
        return jsonify({
            "error": "Insufficient funds",
            "current_balance": current_balance,
            "requested_amount": amount
        }), 400

    # Perform withdrawal
    accounts[account_number]["balance"] -= amount
    new_balance = accounts[account_number]["balance"]

    return jsonify({
        "message": "Withdrawal successful",
        "account_number": account_number,
        "amount_withdrawn": amount,
        "new_balance": new_balance
    }), 200


# POST /accounts/{account_number}/deposit
@app.route('/accounts/<account_number>/deposit', methods=['POST'])
def deposit_money(account_number):
    # Check if account exists
    if account_number not in accounts:
        return jsonify({
            "error": "Account not found",
            "account_number": account_number
        }), 404

    # Get the amount from the request body
    data = request.get_json()
    if not data or 'amount' not in data:
        return jsonify({
            "error": "Amount is required",
            "example": {"amount": 100.50}
        }), 400

    amount = data['amount']

    # Validate amount
    if not isinstance(amount, (int, float)) or amount <= 0:
        return jsonify({
            "error": "Amount must be a positive number"
        }), 400

    # Perform deposit
    accounts[account_number]["balance"] += amount
    new_balance = accounts[account_number]["balance"]

    return jsonify({
        "message": "Deposit successful",
        "account_number": account_number,
        "amount_deposited": amount,
        "new_balance": new_balance
    }), 200


if __name__ == '__main__':
    # Get port from environment variable or use 5000 as default
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)