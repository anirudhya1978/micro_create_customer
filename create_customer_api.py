#this is the api wrapper for create customers to be deployed in a container
from flask import Flask, jsonify, request
from create_customer import create_customer

app= Flask(__name__)

@app.route('/')
def hello():
    return "API for Create Customers !"

@app.route('/create_customer', methods=['POST'])
def create_customers():
    customer_names = request.form.get('customer_name')
    customer_adds = request.form.get('customer_add')
    customer_phones = request.form.get('customer_phone')
    customer_id = create_customer(customer_names,customer_adds, customer_phones)
    return jsonify({'Customer Id':customer_id})

if __name__== '__main__':
    app.run(debug=False,host='0.0.0.0')
