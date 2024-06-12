# Architecture Summary

This stack quickly provisions:

- A lambda function named `restapi_lambda` (not connected to any customer-owned VPC)
- A DynamoDB global table named `restapi_dynamodb_global_table` with Read/Write grant to the `restapi_lambda` in the primary region `us-east-1` with 2 replicas in regions `us-east-2` and `us-west-2`
- An API Gateway named `restapi_lambda_api` with the `restapi_lambda` as handler

By choosing DynamoDB global table, we enhance availability by leveraging localized read and write performance accross multiple regions in an active-active configuration.

It's important to note that, as per the [documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html#GlobalTablesReplicate), cross-region replication with global tables
entails the following consistency-vs-availability considerations:

> Transactional operations provide ACID guarantees only within the region where the write is made originally. Transactions are not supported across regions in global tables

# Infrastructure Code

AWS CDK code is contained in the `rest_api_cdk/` directory. The code run by the lambda function is very simple and for demo purposes and is containe in the `lambda/rest-api/` directory.

# CI/CD Pipeline:

Along with the AWS CDK stack, 3 GitHub actions have been provided under the `.github/` directory that perform the following CI/CD tasks if the repository is hosted on GitHub:

1. `aws-cdk-diff`: is run during Pull-Requests and simply checks for changes via `cdk diff`
1. `aws-cdk-deploy`: is run during only on merge actions to the `master` branch and deploys infrastructure via `cdk deploy --require-approval=never`
1. `aws-cdk-destroy`: is run during only manually and destroys infrastructure via `cdk destroy --force`

All workflows set up the build environment by deploying Python 3.12 and Node 18 on a basic environment based on `ubuntu-latest`, and then installing the `aws-cdk` along with the project `pip` dependencies.