import aws_cdk as core
import aws_cdk.assertions as assertions

from rest_api_cdk.rest_api_stack import RestApiStack

# example tests. To run these tests, uncomment this file along with the example
# resource in rest_api_cdk/rest_api_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = RestApiStack(app, "rest-api-stack")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
