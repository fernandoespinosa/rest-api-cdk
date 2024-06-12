from aws_cdk import (
    Stack, RemovalPolicy,
    aws_lambda,
    aws_dynamodb,
    aws_apigateway
)
from constructs import Construct

class RestApiStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # example resource
        # queue = sqs.Queue(
        #     self, "ApiTestCdkQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        restapi_lambda = aws_lambda.Function(
            self,
            "restapi_lambda",
            runtime=aws_lambda.Runtime.PYTHON_3_12,
            code=aws_lambda.Code.from_asset("lambda/rest-api"),
            handler="main.handler"
        )

        dynamodb_table = aws_dynamodb.TableV2(
            self,
            "restapi_dynamodb_global_table",
            partition_key=aws_dynamodb.Attribute(name="pk", type=aws_dynamodb.AttributeType.STRING),
            replicas=[
                aws_dynamodb.ReplicaTableProps(region="us-east-2"),
                aws_dynamodb.ReplicaTableProps(region="us-west-2")
            ],
            removal_policy=RemovalPolicy.DESTROY
        )
        
        dynamodb_table.grant_read_write_data(restapi_lambda)
        
        restapi_lambda.add_environment("DYNAMO_TABLE", dynamodb_table.table_name)
        
        api = aws_apigateway.LambdaRestApi(
            self,
            "restapi_lambda_api",
            handler=restapi_lambda
        )
        echo_resource = api.root.add_resource("echo")
        echo_resource.add_method("GET")