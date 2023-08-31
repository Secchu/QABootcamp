Project
=======
This project is a MVC project with views that provides a feedback form to users for sending feedback. When feedback
is recieved it uses Amazon Simple Email Service to send an email notification to the verified identity that feedback
has been recieved.

There is also a Serverless version. Please refer to the Readme.md in AWSDemos\SesMvcFeedbackProjects.

For security reasons you should not have your secrets stored and read locally. You should use Secrets Manager 
or Parameters Store. This code reads the mail configuration from Parameters Store.

For the process of converting Serverless MVC project to onpremises please refer to the Readme.md file in 
AWSDemos\SesMvcFeedbackProjects. The file briefly explains the steps involved in converting onpremises MVC code and
publish it as Serverless AWS lambda function. Once you know how to convert one way then you should be able to
work out going the opposite direction and converting an AWS MVC Serverless code to onpremise MVC project.

Required Nuget Packages
=======================
The following packages need to be installed

Amazon.Extensions.Configuration.SystemsManager
AWSSDK.Extensions.NETCore.Setup
AWSSDK.Core
AWSSDK.SimpleEmail

AWS Profile
===========
You will need to setup an AWS user on the CLI with appropiate permissions so that the application can access the parameters
from Parameter Store and have appropiate permissions to send SES emails. You should have the Visual Studio AWS toolket
installed with a AWS profile setup and linked to an user with sufficient rights. Refer to the AWS documentation for
more information.

Setting up SES
==============
You will need to setup a verified identity under the Amazon SES dashboard in the AWS console. 

You will also need to create SMTP credentials under SMTP settings in the SES dashboard.

You will also need to create some parameters in Parameter Store of your SMTP settings including the SMTP user and 
password.

For all of the above refer to AWSDemos\SesMvcFeedbackProjects\Readme.md

appsettings.json File
=====================
You only need to include your profile and region of the Parameter Store.

Refer to AWSDemos\SesMvcFeedbackProjects\Readme.md for more information.