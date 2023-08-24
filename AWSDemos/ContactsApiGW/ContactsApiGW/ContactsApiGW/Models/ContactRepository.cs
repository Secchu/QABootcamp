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

        public async Task<Contact> GetContactAsync(string id) => await dbContext.LoadAsync<Contact>(id);

        public async Task DeleteContactAsync(string id)
        {
            var contact = await GetContactAsync(id);
            await dbContext.DeleteAsync(contact);
        }
    }
}
