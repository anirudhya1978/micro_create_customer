# Create Customer
This has the micro service code for creating customers

The following files have been included 
1. Dockerfile - Use this to build your docker image for create_order micro service

2. Create_customer.html - This is to check if the database your code is working. You have to change the post end point to make it work. You can use this to build a load generator for the application using JMeter or some other tool 

3. creare_customer.py - This has the code and logic for the creating customers. You have to change the database host, dbname and crednetials

4. create_customer_api.py - Flask code to convert the create_order into a service 

5. deployment_create_customer.yaml - Configuration files for creating the cluster on AWS using EKS. You will have to replace the name of the image with docker image that you create

6. newrelic.ini - You will have to change the key to include your own New Relic license key. 

7. requirements.txt - has all the python libraries that are required for the code to run


