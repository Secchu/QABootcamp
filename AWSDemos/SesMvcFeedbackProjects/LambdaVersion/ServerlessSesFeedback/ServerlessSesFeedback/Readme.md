The Project
===========
This is an AWS Serverless lambda demo application that uses .Net MVC with views. It provides a feedback form for
users to send feedback and then once feedback is recieved SES is used to send an email notifying the verified identity
setup on the AWS account that feedback has been recieved.

The Mail settings are read from Parameter Store and these configuration settings such as Username, Password and Host
should be SecureString so that their values are encrypted.

There is also an onpremises version of this project please refer to following files for more information

AWSDemos\SesMvcFeedbackProjects\OnPremisesVersion\SesFeedback\Readme.md 
AWSDemos\SesMvcFeedbackProjects\Readme.md

Required Nuget Packages
=======================
The following packages need to be installed

Amazon.Extensions.Configuration.SystemsManager
AWSSDK.Extensions.NETCore.Setup
AWSSDK.Core
AWSSDK.SimpleEmail
Amazon.Lambda.AspNetCoreServer (Installed when you open a new AWS Serverless Web API project)

More Information
================
For more information on how to setup the projects including how to convert from onpremises to serverless and vice versa
please refer to the following Readme.md file.

AWSDemos\SesMvcFeedbackProjects\Readme.md
