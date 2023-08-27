using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using ContactsApiGW.Models;
using Newtonsoft.Json;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace ContactsApiGW;

public class ContactsApiLambda
{

    private IContactRepository ContactRepo = new ContactRepository();

    public async Task<IEnumerable<Contact>> GetAllContactsAsync(APIGatewayHttpApiV2ProxyRequest request, 
    ILambdaContext context)
    {
        LambdaLogger.Log("Getting all contacts in the DynamoDB table");
        var contacts = await ContactRepo.GetAllContactsAsync();
        var contactsJson = JsonConvert.SerializeObject(contacts);
        LambdaLogger.Log($"Retrieved the following Contacts in JSON: {contactsJson}");
        
        return contacts;
    }

    public async Task<APIGatewayHttpApiV2ProxyResponse> CreateContactAsync(APIGatewayHttpApiV2ProxyRequest request, 
    ILambdaContext context)
    {
        var contact = JsonConvert.DeserializeObject<Contact>(request.Body);

        await ContactRepo.CreateContactAsync(contact);

        var message = $"Contact with Id {contact.Id} Created";
        LambdaLogger.Log(message);
        
        return new APIGatewayHttpApiV2ProxyResponse
        {
            Body = message,
            StatusCode = 201
        };
    }



    public async Task<APIGatewayHttpApiV2ProxyResponse> DeleteContactAsync(APIGatewayHttpApiV2ProxyRequest request,
    ILambdaContext context)
    {
        try
        {
            string Id = request.PathParameters["Id"];
            LambdaLogger.Log($"Deleting contact with {Id}");

            await ContactRepo.DeleteContactAsync(Id);

            return new APIGatewayHttpApiV2ProxyResponse
            {
                StatusCode = 204,
                Body = "Contact with ID deleted"
            };
        }
        catch (Exception) { return new APIGatewayHttpApiV2ProxyResponse { StatusCode = 404, Body = "Not Found" }; }
    }

    public async Task<Contact> GetContactByIdAsync(APIGatewayHttpApiV2ProxyRequest request, 
    ILambdaContext context)
    {
        string Id = request.PathParameters["Id"];
        LambdaLogger.Log($"Retrieving contact with {Id}");
        return await ContactRepo.GetContactAsync(Id);
    }
}
