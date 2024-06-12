# Infrastructure Engineer Task: Design and Deploy a Global REST API
## Objective
Your task is to design a scalable and resilient architecture for a global REST API with a database component. The solution should leverage AWS services to ensure high availability and global reach. You will use the AWS Cloud Development Kit (CDK) in Python to define the infrastructure as code (IaC) and outline a continuous integration and continuous deployment (CI/CD) process for automated deployment.

# Requirements

1. Architecture Design:

Create a simple Markdown-formatted document describing the architecture of the global REST API. The architecture should include a database component to store and retrieve data.
Include considerations for scalability, data consistency, and global availability.

2. Infrastructure as Code (IaC):

Using Python AWS CDK, write the code necessary to deploy the architecture you’ve designed. Your CDK code should define the necessary AWS resources such as API Gateway, Lambda functions (for the REST API logic), and DynamoDB or RDS (for the database component).
Ensure your CDK code includes configurations for scaling and high availability across multiple regions, if applicable.

3. CI/CD Pipeline:

Outline a CI/CD pipeline that automates the deployment of your REST API and database component. Include steps for code build, tests, and deployment.i
Mention any specific AWS services or third-party tools you would use to implement the CI/CD pipeline (e.g., AWS CodePipeline, AWS CodeBuild, GitHub Actions).

## Deliverables
A Markdown document containing:
A detailed description of the REST API architecture.
Considerations for scalability, availability, and data consistency.
Python AWS CDK code files that define the infrastructure required to deploy your architecture.
A brief outline of the CI/CD pipeline process for deploying the REST API and database component.
Please insert an your Markdown description and associated Python CDK files inside Coderpad. Additionally, include any instructions or assumptions made during the design process.