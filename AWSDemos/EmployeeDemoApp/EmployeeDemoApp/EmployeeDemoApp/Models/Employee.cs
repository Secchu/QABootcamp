using Amazon.DynamoDBv2.DataModel;

namespace EmployeeDemoApp.Models
{
    [DynamoDBTable("Employees")]
    public class Employee
    {
        public string ID { get; set; }
        public string Name { get; set; }
        public string Surname { get; set; }
        public int Age { get; set; }
        public decimal Salary { get; set; }
        public string Department { get; set; }
        public char Sex { get; set; }
    }
}
