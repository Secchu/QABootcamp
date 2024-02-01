Author: Sec Chu

QABootcamp Repository Project List
===================================
Repository contains Python coding tasks done during my study at QA Bootcamp. It also includes my own personal project for my portfolio. 

The Repository also contains .Net Projects and AWS Demos coded in C# .Net. These projects are not part of my work during my study at QA but are 
coding projects that I do in my spare time. Please refer to the specific Readme.md file for more information. Below is a brief summary.

tictactoe_task
==============
A basic Tic Tac Toe console application coded in Python.

MoviesSQLTask
=============
Python code that uses MySQL Connector to create a Movies schema. The task involves creating the schema with Python, inserting movie records wirh Python
as well as querying the tables and joining relationships between tables to answer queries. The relational database used was MySQL.

The first part of the task was to design the tables and relationships using SQL statements.

MoviesFlaskApp
==============
This was my personal project. It is also an extension of the previous task. My project was to design a fully functional flask application with a web
interface that provides CRUD capabilities for a relational movies database with multiple relationships.

CRUD stands for CREATE READ UPDATE DELETE. These are the four features necessary to implement an database application that provides persistent storage. In 
any basic database application it is necessary that users should be able to create, read, update and delete records.

The application uses Flask as the web framework and Flask SQLAlchemy as the object mapper for connecting to the database. While database Administrators
work with SQL, columns, rows, records, relationships etc Developers work with objects. Having a Object Mapper that convert database records to objects
allows the Developer to concentrate on the design of the application and coding style without having to worry about too much on the internal structure
of the database as well as linking of multiple table relationships.

----------------------------------------------------------------------------------------------------------------------------------------------------------
AWSDemos Folder
===============
The following are .Net projects I have done in my spare time.

ConcurrentBimap
===============
A Class library that provides a thread safe Bidirectional Dictionary.

BoyerMooreAlgorithm
===================
A class library that uses the Boyer Moore algorithm to search, replace and tokenize strings.

ContactsApiGW
=============
A serverless AWS API Gateway application for storing contact information in a Dynamodb table. The project contains a series of Lambda functions 
that can be published to API Gateway. The API's provide CRUD operations for manipulating contact data in a Dynamodb table.

ContosoUniversity
=================
This project modified a .Net CRUD web page application and made it serverless and published the code as a Lambda function. The application was a 
Microsoft Learn tutorial on Web Pages and Entity Framework.

EmployeeDemoApp
===============
A .Net MVC application with views for storing employee records. The persistent store used was Dynamodb.

LambdaAuthorizer
================
This project is a Lambda Authorizer that uses the custom authorization scheme to authorizing API Gateway requests and authorizes users stored in a dynamodb 
table. Passwords in the dynamodb table are encrypted. The project enables you to add security to your API Lambda Functions.  

ServerlessDictionary
====================
A Serverless API lambda application for retrieving dictionary values

SesMvcFeedbackProjects
======================
The solution consists of two separate projects unrelated and each project can be run separately. Both are MVC Projects with razor views. 

Both projects provide an interface for the user to send feedback via a post request using a feedback form. When the  feedback form is recieved Simple Email 
Service is used to send an email notifying the verified identity on the AWS account that feedback has been recieved.

One project is the MVC on premises version. The other project is the serverless lambda version. Both projects are useful for learning how to convert any
ASP.Net application into a serverless lambda function.
