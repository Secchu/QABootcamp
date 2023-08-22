namespace EmployeeDemoApp.Models
{
    public interface IRepository
    {
        Task CreateAsync(Employee employee);
        Task<IEnumerable<Employee>> GetAllEmployeesAsync();
        Task UpdateAsync(Employee emp, string ID);
        Task<Employee> GetEmployee(string ID);
        Task DeleteAsync(string ID);
    }
}