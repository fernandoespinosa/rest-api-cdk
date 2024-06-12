import aws_cdk as core
import aws_cdk.assertions as assertions

from rest_api_cdk.rest_api_stack import ApiTestCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in api_test_cdk/api_test_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ApiTestCdkStack(app, "api-test-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
