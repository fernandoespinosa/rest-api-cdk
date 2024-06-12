
# Architecture overview

This stack quickly provisions:

- A lambda function named `restapi_lambda` (not connected to any customer-owned VPC)
- A DynamoDB table named `restapi_dynamo_table` with Read/Write grant to the `restapi_lambda`
- An API Gateway named `restapi_lambda_api` with the `restapi_lambda` as handler

This stack uses simple table
Include considerations for scalability, data consistency, and global availability.


