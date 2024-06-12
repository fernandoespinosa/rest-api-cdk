from aws_cdk import (
    Stack,
    aws_lambda,
    aws_dynamodb,
    aws_apigateway
)
from constructs import Construct

class ApiTestCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

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

        dynamo_table = aws_dynamodb.Table(
            self,
            "restapi_dynamo_table",
            partition_key=aws_dynamodb.Attribute(name="id", type=aws_dynamodb.AttributeType.STRING)
        )
        
        dynamo_table.grant_read_write_data(restapi_lambda)
        
        restapi_lambda.add_environment("DYNAMO_TABLE", dynamo_table.table_name)
        
        api = aws_apigateway.LambdaRestApi(
            self,
            "restapi_lambda_api",
            handler=restapi_lambda
        )
        echo_resource = api.root.add_resource("echo")
        echo_resource.add_method("GET")