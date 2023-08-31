The SES Projects
================
The solution consists of two separate projects unrelated and each project can be run separately. Both are MVC Projects
with razor views. 

Both projects provide an interface for the user to send feedback via a post request using a feedback form. When the 
feedback form is recieved SES is used to send an email notifying the verified identity on the AWS account that feedback
has been recieved. Note your SES email notification will likely appear in your junk folder as the identity of the
sender cannot be confirmed.

Another point about these two projects is to learn how to convert onpremises MVC code and publish it as a AWS
Serverless application. I am going to briefly explain the steps.

For security you should not leave your mail settings in appsettings.json. You should read in all your settings from
a Secrets Store such as Secrets Manager. In both projects the mail settings are read from Parameter Store. Now by
all means use Secrets Manager if you want. The only reason I have used Parameter Store because you get a generous amount
of free notifications under the free tier. Yes, it just to do with costs. I recently commited a Lambda Authorizer project
that use JWT to authorize API Gateway requests. It was a project where I modified code from another author. The username
and password were stored in Dynamodb table. I listened to the author and provided modifications to the project where
it uses encryption to store the password in Dynamodb. I realised later that it would have been so much easier if I
had used Parameter Store to store the usernames and passwords as SecureStrings. It provides builtin encryption rather
than providing your own encryption code and storing your own private keys. You should not store any keys in code.

The two projects have the following names:
1. SesFeedback is the on premises MVC version.
2. ServerlessSesFeedback is the Lambda version.

Originally I was only going to commit the Lambda version but since I have done a on premises version there is no harm
including that as well so you can see the process on how to convert on premises code to AWS Serverless Lambda functions.
I did commit a project on a AWS Serverless .Net project which was converted from on premises code. The code was 
online Microsoft Learn tutorial. However that was web pages and these two projects are MVC projects with views so
you can compare the two versions to convert between the two formats. Obviously you should know that both project types
are different. One is MVC project with views and the other is AWS Serverless project.

For more specific information about each project please refer to that projects Readme.md file. Here we are going to
cover the SES AWS requirements and the parameter store requirements to get the projects working. I will also cover brief
steps required of how to convert a MVC project to a AWS Serverless project.

AWS Permissions
===============
I am assuming you have an AWS account. You would also need to set a user with permissions for the CLI. I am not going to
cover that. Please refer to the AWS documentation for more details.

SES verified identity
=====================
As explained earlier you will need a verified identity so that SES emails can be sent. 

On the AWS console navigate to Amazon Simple Mail Service and click on 'Create identity'. You can verify by domain or`
email address but as a quick start select email address. Enter your email details and verify. An email would be sent
to the email provided. You need to logon to the email and click on the email link contained in the email. As soon as
you done this the identity should show up as verified on the AWS Console. You now have an identity to send emails.

SMTP Credentials
================
On the left handside of the SES dashboard click on SMTP settings. Then click on 'Create SMTP credentials'. This brings
you straight to IAM with a user to be created with SMTP permissions to send emails. Just click on create user and thats
it you now have a user with the required SMTP Credentials. You need to take note of several values required for Parameter
Store. A word of warning take note of the username and password because if you navigate away you won't be able to 
retrieve it. Don't bother remembering the username or password and these appear as randomly generated strings.

Parameter Store
===============
You would need to create several parameters to get the demo projects working. You must make sure that the Parameter type
is SecureString so that the parameters are encrypted. A parameter takes on the following format.

/{namespace}/{parameter name}

You can have multiple namespaces so the following parameter name is valid

/mail/settings/Host

Both projects have '/mailSettings' as the name of the namespace. If you use a different namespace then you need to change
the following code snipplet.

        Host.CreateDefaultBuilder(args)
        .ConfigureAppConfiguration((context, builder) =>
         {
               //Put in the namespace prefix of the parameter store
               builder.AddSystemsManager("/mailSettings");
         })
            .ConfigureWebHostDefaults(webBuilder =>
            {
                webBuilder.UseStartup<Startup>();
            });

For on premises code the code snipplet is

builder.Configuration.AddSystemsManager("/mailSettings");

The following parameters need to be created in Parameter Store. The values of the parameters can be gotten from SMTP 
settings in the SES dashboard.
 
Assuming you are using the '/mailSettings' namespace the parameters you need to create are listed below.

/mailSettings/Host - Host of the SMTP Server
/mailSettings/DisplayName - What you want to appear on the email. (Anything that you think should appear on the email)
/mailSettings/Mail - Email address of the verified identity
/mailSettings/Password - Password of the SMTP user - (You should have taken note of this when creating the SMTP Credentials.)
/mailSettings/Username - Username of the SMTP user - (You should have taken note of this when creating the SMTP Credentials.)

Required Nuget Packages
=======================
Refer to the specific projects readMe.md file. You can also check the projects proj file.

Converting Onpremise MVC code to Lambda functions
=================================================
Note the namespaces of the onpremises code is SesFeedback and for the Lambda Serverless code is ServerlessSesFeedback.
When I copied over code over to the Serverless project I just used the file->replace for entire solution and replace the
keywords SesFeedback with ServerlessSesFeedback. There is nothing stoping you from using the same namespace name or
moving code such as those contained in the Models folder into a Class library so that it can be imported into any project.
I just the old copy and paste and replace keyword method because its nice and quick and I don't have to make a class 
library. This is however bad practice because we're duplicating code and not sticking to the 'Don't Repeat yourself'
rule.

Another thing to note on the on premises code is .net 7 while the Lambda Serverless version is .net 6. You don't have
a choice on VS 2022. Don't try to modify the proj file on the Serverless version so that it uses .net 7. You will run
into errors and I had to find out the hard way. I suspect Serverless projects for .net 7 is still work in progress 
on some Serverless project types at the time of writing. So, just accept any version the project gives you.

By the way at the time of writing, there is no AWS Serverless project type for MVC projects with views. I had to use the
AWS Serverless project type for Controller Web API's. This does mean that there are a few extra steps required.

1. Copy the Views folder, Models folder and wwwroot folder over to your AWS Serverless project. Important to keep the
file structure exactly the same as the MVC onpremise project.

2. As explained earlier there are other ways to do this but this way is quick and convienient. Replace the keyword 
SesFeedback with ServerlessSesFeedback. Remove any unrequired using statements in code. This will appear in grey.

3. This step is only required because we are using Systems Manager extension. In the Init replace the method with the
following code.

    protected override void Init(IWebHostBuilder builder)
    {
        builder
         .ConfigureAppConfiguration((context, builder) =>
         {
             builder.AddSystemsManager("/mailSettings");
         }
        )
            .UseStartup<Startup>();
    }

Note there are two init methods but it is the top one with IWebHostBuilder as the parameter. Also I am not sure that
LocalEntryPoint.cs is required. I have never really used this file. Theres no harm in including the snipplet in this
file as well.

4. Now for the code modifications on the startup.cs file. Note we are using MVC Web API template so there are a few 
modifications. Perhaps you can just replace the startup.cs file on ServerlessSesFeedback with the startup.cs file 
on SesFeedback. Make the required namespace changes if required. However I will include the broken down steps so you
understand whats going on and can do it manually.

Register your services. Refer to the onpremises code.

        services.AddDefaultAWSOptions(Configuration.GetAWSOptions());
        services.AddAWSService<IAmazonSimpleEmailService>();
        services.AddTransient<ISesService, SesService>();

We don't need Web API's so replace this line of code

            services.AddControllers();

Replace the above code with 

        //services.AddControllers();
        services.AddControllersWithViews();
		
Now that enables us to uses Views. We want to be able to use the static files in wwwroot. Include the following line of
code.

        app.UseStaticFiles();

We are not using Web API routes so replace the following line of code 

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllers();
            });
			
with 

        app.UseEndpoints(endpoints =>
        {
            endpoints.MapControllerRoute(
                name: "default",
                pattern: "{controller=Home}/{action=Index}/{id?}");
        });
		
Note you can also go the other way converting serverless code to onpremises. Once you know one way you know them both.


The appsettings.json file
=========================
We are using Systems Manager configuration extension so the following needs to be included in appsettings.json

  "AWS": {
    "Profile": "default",
    "Region": "eu-west-2"
  }
  
I know you have the AWS toolkit installed and the AWS user profile however you would want to include the above json
in the file. Make sure you put in the profile name and the region of the Parameter Store.

Publishing Serverless version to AWS
====================================
Publish with the AWS toolkit and refer to the AWS documentation for more details. You would want to include the necessary
IAM permissions. You need to modify the serverless.template file. I know you need the following permissions for
accessing Parameter Store and SES permissions to send emails.

        "Policies": [
          "AWSLambda_FullAccess",
          "AmazonSSMReadOnlyAccess",
          "AmazonSESFullAccess"
        ]
		
However I ran into problems because I was getting blank screens and when I checked the cloudwatch logs it was a
permissions problem. No messing around I quickly changed the permissions to the one below. I included the PowerUsers
permissions. Now this is way too much permissions and this is now a security risk. I suspect just including 
PowerUsers policy would have been enough.

        "Policies": [
          "AWSLambda_FullAccess",
          "AmazonSSMReadOnlyAccess",
          "AmazonSESFullAccess",
          "PowerUserAccess"
        ]

PowerUsersAccess is similar to an AWS admins user with Administrators rights. Refer to the AWS documentation and only
provide the necessary minimal permissions.

I don't know permissions for the onpremises version either because I use the same CLI admin user for all my AWS 
apps. Again in production you would want to be more precise and strict with your permissions.

Screenshots
===========
Provided screenshots while running the serverless version. However the output of both versions are the same because they
are using the same views. Refer to the screenshots folder.

