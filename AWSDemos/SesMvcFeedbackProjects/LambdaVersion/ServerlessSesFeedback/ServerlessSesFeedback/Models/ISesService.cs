namespace ServerlessSesFeedback.Models
{
    public interface ISesService
    {
        Task NotifyFeedbackAsync(Feedback feedback);
    }
}
