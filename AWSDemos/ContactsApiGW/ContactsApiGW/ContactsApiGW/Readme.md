Project
=======
A basic AWS API Gateway application for storing contact information. 

Quick Start
===========
You will need to create the dynamodb table called Contacts in your AWS account. Its probably easier just to create this table using the AWS console.
For the structure of the table refer to Contacts.cs. The main requirement is the Id field needs to be the hashkey. Note the hashkey is of type string.
This is the partition key. You can manually create the records in the AWS console if you want. Refer to Contacts.cs for the attribute fields.

You will also need to create the API Gateway routes in API Gateway -> API -> Create API -> HTTP API Build -> Add Integration.

You will need to create a route for each function in ContactsApiLambda.cs.

You will also need to publish the code function by function. Use the AWSToolkit. You will need to create an IAM role with the following permissions
1. LambdaExecutionRole
2. Also you need to add permissions to access the Lambda table. You need to add a policy. 
3. I am also assuming you have a CLI user setup with sufficient rights or you won't be able to publish the code.

You will need to specify this role for each published function. You can use the specify the LambdaExecutionRole when publishing and uploading the code
to AWS. However you will need to edit this role and add policies to enable permissions to access the dynamodb table.

Routes
======
The following routes need to be published.

Method		Resource Path			Integration Target				Function Name
======      =============		    ================== 				=============
GET         /Contacts/{Id}   		ContactById						GetContactByIdAsync
DELETE 		/Contacts/{Id}			DeleteContact					DeleteContactAsync
GET			/Contacts				Contacts						GetAllContactsAsync
POST		/Contacts				CreateContact					CreateContactAsync

Testing
=======
Use POSTMAN

Getting Sample Data in the Contacts dynamodb table
==================================================

> cd dynamodb

(The following is windows command. If your using Linux refer to the AWS documentation. I don't think its much different although I haven't had time
to check)

> aws dynamodb batch-execute-statement --statements file://partiqlbatch.json

You should then recieve JSON response indicating that the records have been added.

You notice the telephone numbers are less than 10 digits. This is done so that I don't accidently publish someone telephone number. All numbers are just 
random.

Cleaning up
===========
Delete your resources when finished so you don't get charged.

Updates
=======
A good addition to the code is to add searching capabilities. Please don't use Scan. It is expensive operation. Set up the Sort key and use Indexes such as
global and local index if you need even more complicated search capabilities. Please refer to the AWS documentation.

## Here are some steps to follow to get started from the command line:

Once you have edited your template and code you can deploy your application using the [Amazon.Lambda.Tools Global Tool](https://github.com/aws/aws-extensions-for-dotnet-cli#aws-lambda-amazonlambdatools) from the command line.

Install Amazon.Lambda.Tools Global Tools if not already installed.
```
    dotnet tool install -g Amazon.Lambda.Tools
```

If already installed check if new version is available.
```
    dotnet tool update -g Amazon.Lambda.Tools
```

Execute unit tests
```
    cd "ContactsApiGW/test/ContactsApiGW.Tests"
    dotnet test
```

Deploy function to AWS Lambda
```
    cd "ContactsApiGW/src/ContactsApiGW"
    dotnet lambda deploy-function
```
