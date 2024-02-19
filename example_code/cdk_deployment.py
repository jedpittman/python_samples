"""CDK code for AWS stack to deploy the Lambda function and API Gateway."""
from aws_cdk import core
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_apigateway as apigw

# Define the stack
class CdkDeploymentStack(core.Stack):
    
        def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
            super().__init__(scope, id, **kwargs)
    
            # Create a Lambda function
            lambda_function = _lambda.Function(
                self, "HelloHandler",
                runtime=_lambda.Runtime.PYTHON_3_8,
                code=_lambda.Code.asset("lambda"),
                handler="hello.handler"
            )
    
            # Create an API Gateway
            apigw.LambdaRestApi(
                self, "Endpoint",
                handler=lambda_function
            )

# Create the app
app = core.App()

# Create the stack
CdkDeploymentStack(app, "CdkDeploymentStack")

# Synthesize the stack
app.synth()
```
