using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.DataModel;

namespace ContactsApiGW.Models
{
    public class ContactRepository : IContactRepository
    {
        private AmazonDynamoDBClient client;
        private DynamoDBContext dbContext;
        
        public ContactRepository()
        {
            client = new AmazonDynamoDBClient();
            dbContext = new DynamoDBContext(client);
        }

        public async Task<string> CreateContactAsync(Contact contact)
        {
            await dbContext.SaveAsync(contact);
            return contact.Id;
        }

        public async Task<IEnumerable<Contact>> GetAllContactsAsync()
        {
            var contacts = new List<Contact>();
            contacts.AddRange(await dbContext.ScanAsync<Contact>(default).GetRemainingAsync());

            return contacts;
        }

        public async Task<Contact> GetContactAsync(string Id) => await dbContext.LoadAsync<Contact>(Id);

        public async Task DeleteContactAsync(string Id)
        {
            var contact = await GetContactAsync(Id);
            await dbContext.DeleteAsync(contact);
        }
    }
}
