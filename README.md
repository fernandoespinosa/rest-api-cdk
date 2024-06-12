
# Architecture overview

This stack quickly provisions:

- A lambda function named `restapi_lambda` (not connected to any customer-owned VPC)
- A DynamoDB global table named `restapi_dynamodb_global_table` with Read/Write grant to the `restapi_lambda` in the primary region `us-east-1` with 2 replicas in regions `us-east-2` and `us-west-2`
- An API Gateway named `restapi_lambda_api` with the `restapi_lambda` as handler

By choosing DynamoDB global table, we enhance availability by leveraging localized read and write performance accross multiple regions in an active-active configuration.

It's important to note that, as per the [documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html#GlobalTablesReplicate), cross-region replication with global tables
entails the following consistency-vs-availability considerations:

> Transactional operations provide ACID guarantees only within the region where the write is made originally. Transactions are not supported across regions in global tables

