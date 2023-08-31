namespace SesFeedback
{
    public class MailSettings
    {
        public MailSettings(IConfiguration configuration)
        {
            Host = configuration["Host"];
            DisplayName = configuration["DisplayName"];
            Mail = configuration["Mail"];
            Username = configuration["Username"];
            Password = configuration["Password"];
            Port = 587;
        }

        public string? Host { get; }
        public int Port { get; }
        public string? DisplayName { get; }
        public string? Mail { get; }
        public string? Username { get; }
        public string? Password { get; }
    }
}
