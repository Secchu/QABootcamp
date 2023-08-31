using Microsoft.AspNetCore.Mvc;
using SesFeedback.Models;
using System.Diagnostics;

namespace SesFeedback.Controllers
{
    public class HomeController : Controller
    {
        private readonly ISesService _mailService;

        public HomeController(ISesService mailService)
        {
            _mailService = mailService;
        }

        public IActionResult Index()
        {
            return View();
        }

        public IActionResult Feedback()
        {
            return View();
        }

        [HttpPost]
        public async Task<IActionResult> FeedbackAsync(Feedback feedback)
        {
            await _mailService.NotifyFeedbackAsync(feedback);
            return View("Confirmation", feedback.Name);
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}