
using EmployeeDemoApp.Models;
using Microsoft.AspNetCore.Mvc;

namespace EmployeeDemo.Controllers
{
    public class EmployeeController : Controller
    {
        private readonly IRepository repository;

        public EmployeeController(IRepository repository)
        {
            this.repository = repository;
        }

        public async Task<IActionResult> IndexAsync()
        {
            var employees = await repository.GetAllEmployeesAsync();
            return View(employees);
        }
        // HTTP GET VERSION
        public IActionResult Create()
        {
            return View();
        }

        // HTTP POST VERSION
        [HttpPost]
        public async Task<IActionResult> CreateAsync(Employee employee)
        {
           await repository.CreateAsync(employee);
           return View("Thanks", employee);
        }

        public async Task<IActionResult> UpdateAsync(string ID)
        {
            var employee = await repository.GetEmployee(ID);
            return View(employee);
        }

        [HttpPost]
        public async Task<IActionResult> UpdateAsync(Employee employee, string ID)
        {
           await repository.UpdateAsync(employee, ID);
           return RedirectToAction("Index");
        }

        [HttpPost]
        public async Task<IActionResult> Delete(string ID)
        {
          await repository.DeleteAsync(ID);
          return RedirectToAction("Index");
        }
    }
}

