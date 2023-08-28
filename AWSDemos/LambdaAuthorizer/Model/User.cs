using Amazon.DynamoDBv2.DataModel;

namespace LambdaAuthorizer.Model
{
    [DynamoDBTable("users")]
    public class User
    {
        [DynamoDBHashKey("email")]
        public string? Email { get; set; }
        [DynamoDBProperty("username")]
        public string? Username { get; set; }
        [DynamoDBProperty("password")]
        public string? Password { get; set; }
    }
}
