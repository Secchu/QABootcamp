using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.EntityFrameworkCore;

namespace ContosoUniversity.Pages.Department
{
    public class IndexModel : PageModel
    {
        private readonly Data.SchoolContext _context;

        public IndexModel(Data.SchoolContext context)
        {
            _context = context;
        }

        public IList<Models.Department> Department { get;set; } = default!;

        public async Task OnGetAsync()
        {
            if (_context.Departments != null)
            {
                Department = await _context.Departments
                .Include(d => d.Administrator).ToListAsync();
            }
        }
    }
}
