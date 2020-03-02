#this is the microservice for creating customers
import requests
import mysql.connector 
import json
import random
import logging

def create_customer(customer_name, customer_add, customer_ph):
    customer_name= customer_name
    customer_add = customer_add
    customer_ph = customer_ph
    max_cust_id = 0
    
    cnx2=mysql.connector.connect(user='admin', password='Welcome1',
                              host='customerdb.ceklihwabawd.us-east-1.rds.amazonaws.com',
                              database='cust_order_db')
    
    cursor2=cnx2.cursor()
    query = ("Select max(cust_id) from customer_details")
    cursor2.execute(query)
    for(cust_id) in cursor2:
        max_cust_id = max(cust_id) +1 
        #print ("Max Customer Id" + str(max_cust_id))
        #print ("Max Customer {}".format(cust_id))
    
    add_customer= ("insert into customer_details"
                   "(cust_id, customer_name, cusotmer_address,customer_phone)"
                   "VALUES(%(cust_id)s, %(customer_name)s, %(cusotmer_address)s, %(customer_phone)s)")
    
    customer_data = {
        'cust_id': max_cust_id,
        'customer_name': customer_name,
        'cusotmer_address': customer_add,
        'customer_phone': customer_ph
        }
    
    cursor2.execute(add_customer,customer_data)
    cnx2.commit()
    cursor2.close()
    cnx2.close()
    return max_cust_id 
