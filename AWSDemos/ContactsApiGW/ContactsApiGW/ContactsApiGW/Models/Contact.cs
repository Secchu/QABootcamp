using Amazon.DynamoDBv2.DataModel;

namespace ContactsApiGW.Models
{
    [DynamoDBTable("Contacts")]
    public class Contact
    {
        [DynamoDBHashKey("Id")]
        public string Id { get; set; }
        public string Name { get; set; }
        public string Surname { get; set; }
        public string Mobile { get; set; }

    }
}
