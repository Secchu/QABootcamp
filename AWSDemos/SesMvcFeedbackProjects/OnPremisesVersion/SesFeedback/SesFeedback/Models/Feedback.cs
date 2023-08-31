namespace SesFeedback.Models
{
    public class Feedback
    {
        public Feedback()
        {
                
        }

        public string Name { get; set; } = string.Empty;
        public string Email { get; set; } = string.Empty;
        public string Subject { get; set; } = string.Empty; 
        public string Content { get; set; } = string.Empty;  
    }
}
