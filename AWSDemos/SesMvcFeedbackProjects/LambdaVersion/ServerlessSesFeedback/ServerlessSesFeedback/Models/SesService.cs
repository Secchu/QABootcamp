using Amazon.SimpleEmail;
using Amazon.SimpleEmail.Model;

namespace ServerlessSesFeedback.Models
{
    public class SesService : ISesService
    {
        public SesService(IConfiguration config, IAmazonSimpleEmailService ses)
        {
            _mailConfig = new MailSettings(config);
            _ses = ses;
        }

        public async Task NotifyFeedbackAsync(Feedback feedback)
        {

            var time = DateTime.Now.ToString("HH:mm dd/MM/yy");

            string fbContent = "This is the SES Service. You have recieved feeback\n\n" +
                               $"SMTP Display Name: {_mailConfig.DisplayName}\n" +
                               $"Name: {feedback.Name}\n" +
                               $"Subject: {feedback.Subject}\n" +
                               $"Email: {feedback.Email}\n" +
                               $"Content: {feedback.Content}\n\n" +
                               $"Recieved Time: {time}\n";

            var inbox = new Destination(new List<string> { _mailConfig.Mail! });

            var mailBody = new Body(new Content(fbContent));
            
            var emailMsg = new Message
            (new Content($"Feedback from {feedback.Name} {feedback.Email}"), 
            mailBody);
            
            await _ses.SendEmailAsync(new SendEmailRequest(_mailConfig.Mail, inbox, emailMsg));
        }

        private MailSettings _mailConfig { get; }
        private IAmazonSimpleEmailService _ses { get; }

        public MailSettings MailSettings { get=> _mailConfig; } 

    }
}
