namespace SesFeedback.Models
{
    public interface ISesService
    {
        Task NotifyFeedbackAsync(Feedback feedback);
    }
}
