Project
=======
This is a project is a Lambda Authorizer using the custom authorization scheme The project enables you to add security to your API Lambda Functions. 
You will need to publish your own API Lambda functions and add this project to your solution. When published correctly the API Gatway will validate
the users credentials and issue a valid JWT token for 5 minutes. If authorized it will return the appropiate access policy.

The main code was taken from this website. I suggest you follow the instructions on this website to provide authorization for your lambda functions.

https://codewithmukesh.com/blog/aws-lambda-authorizer-in-dotnet 

The code has been tweaked to provide encrypted passwords. The users are taken from a dynamodb table called users where the users Email field is the
partition key. Refer to Users.cs. I have added encryption so the users password is encrypted.

Required Modifications
======================
Change the two static variables below to your AES private key in Base64 format.

    private const string secretkey = 
    "IR1OxZcrKJcLnqZmBzXHBswdLf9LIscA/UZvQvbDzlY=";
    
    private const string secretIv = "e1+doLZTWo6V+2+Ezpx9eQ==";
	
Change the static variable below so that the string value contains your API Gatway ID and region. The format is 
arn:aws:execute-api:<aws-region>:<aws-account-id>:<amazon-gateway-id>/*/*.

    private const string awsArn = "arn:aws:execute-api:ap-south-1:821175633958:sctmtm1ge8/*/*";
	
Change the static variable below to your API key

    private const string ApiKey = "S0M3RAN0MS3CR3T!1!MAG1C!1!";
	
Generating your own AES private key and Initialization Vector
=============================================================

Open a separate project. It could be a Console application or Test project. It really doesn't matter.
You could then write your key and IV bytes to a file.

var rkg = new RandomKeyGenerator();
File.WriteAllBytes(@"C:\temp\key.txt", rkg.GetBytes(32));
File.WriteAllBytes(@"C:\temp\IV.txt", rkg.GetBytes(16));

The key and IV need to be in Base64 format. You could just do something like this when reading the keys

var aesKey = Convert.ToBase64String(File.ReadAllBytes(@"C:\temp\key.txt"));
var aesIV = Convert.ToBase64String(File.ReadAllBytes(@"C:\temp\IV.txt"));

Console.WriteLine($"aes key: {aesKey}");
Console.WriteLine($"IV: {aesIV}");

Adding Users to users dynamodb table
====================================
The password needs to be encrypted. You could use the snipplet below.

AesEncryptionProvider provider =
new AesEncryptionProvider(key, iv);

string encrypt = provider.Encrypt("YOUR PASSWORD");

Console.WriteLine($"PASSWORD: {encrypt}");


## Here are some steps to follow from Visual Studio:

To deploy your function to AWS Lambda, right click the project in Solution Explorer and select *Publish to AWS Lambda*.

To view your deployed function open its Function View window by double-clicking the function name shown beneath the AWS Lambda node in the AWS Explorer tree.

To perform testing against your deployed function use the Test Invoke tab in the opened Function View window.

To configure event sources for your deployed function, for example to have your function invoked when an object is created in an Amazon S3 bucket, use the Event Sources tab in the opened Function View window.

To update the runtime configuration of your deployed function use the Configuration tab in the opened Function View window.

To view execution logs of invocations of your function use the Logs tab in the opened Function View window.

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
    cd "LambdaAuthorizer/test/LambdaAuthorizer.Tests"
    dotnet test
```

Deploy function to AWS Lambda
```
    cd "LambdaAuthorizer/src/LambdaAuthorizer"
    dotnet lambda deploy-function
```
