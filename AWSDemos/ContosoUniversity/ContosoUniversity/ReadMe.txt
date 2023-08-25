Project
=======
The point of this project is to be able to modify any ASP.NET web app and make the on premises code serverless so that it can be published on to AWS.

The process of converting a MVC application to AWS Lambda is exactly the same. The Serverless project type is different. That's it.

Modified Code
=============
The code I modified was an online Microsoft Learn tutorial which can be found on this website.

https://learn.microsoft.com/en-us/aspnet/core/data/ef-rp/intro?view=aspnetcore-7.0&tabs=visual-studio

The original github code can be found here
https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/data/ef-rp/intro/samples/cu60

Many thanks to Rick Anderson who wrote the original code.

Modifications
=============
The code is modified so that it works as a Lambda function.

Original code used SQL Server while I have modified this to an in memory database. This is to save on compute costs. This means the size of the database
is subject to Lambda limitations but for demo purposes this is absolutely fine.

Publishing the code on AWS
==========================
You will need an AWS account to publish the Lambda function.

Updates
=======
On later versions of Visual Studio the format of the serverless.template file has changed. Best to readd the source files to a new project. You can just 
publish the code without worrying about this file.

Live demo
=========
https://jjtfbral0a.execute-api.eu-west-2.amazonaws.com/Prod

More Information
================
https://d2n2rgkzriycso.cloudfront.net/Demos/MyDemos.html