using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.DataModel;
using Amazon.DynamoDBv2.DocumentModel;

namespace EmployeeDemoApp.Models
{
    public class Repository : IRepository
    {
        private Random rand = new Random();

        /*
        //Local Dynamodb Start
        private AmazonDynamoDBConfig config = new AmazonDynamoDBConfig
        {
            RegionEndpoint = Amazon.RegionEndpoint.EUWest2,
            ServiceURL = "http://localhost:8000/"
        };
        //Local Dynamodb End*/

        
        //Actual DB Start
        private AmazonDynamoDBConfig config = new AmazonDynamoDBConfig
        {
            RegionEndpoint = Amazon.RegionEndpoint.USEast1
        };
        //Actual DB End

        private AmazonDynamoDBClient client;
        private DynamoDBContext context;

        public Repository()
        {
            //Local DB
            //client = new AmazonDynamoDBClient("1", "1", config);

            //Actual DB
            client = new AmazonDynamoDBClient(config);

            // Create a DynamoDB Context Object
            context = new DynamoDBContext(client);

        }

        public async Task<IEnumerable<Employee>> GetAllEmployeesAsync()
        {
            var table = context.GetTargetTable<Employee>();
            var scanOps = new ScanOperationConfig();
            var employeeResults = new List<Employee>();

            bool done = false;

            do
            {
                Search results = table.Scan(scanOps);

                List<Document> data = await results.GetNextSetAsync();
                IEnumerable<Employee> employees = context.FromDocuments<Employee>(data);
                employeeResults.AddRange(employees);

                //Empty JSON will be returned if we're done. Dynamodb like relational db isn't designed
                //for retrieving large datasets. More so for Dynamodb. Whole Table Scan is expensive
                //and involves checking all partitions. Avoid if possible.
                done = results.PaginationToken.Equals("{}");

            } while (!done);
            
            return employeeResults;
        }

        public async Task UpdateAsync(Employee emp, string ID)
        {
            var employee = await GetEmployee(ID);
            employee.Surname = emp.Surname;
            employee.Name = emp.Name;
            employee.Salary = emp.Salary;
            employee.Sex = emp.Sex;
            employee.Age = emp.Age;
            employee.Department = emp.Department;

            await context.SaveAsync(employee);
        }

        public async Task<Employee> GetEmployee(string ID) => await context.LoadAsync<Employee>(ID);

        public async Task DeleteAsync(string ID)
        {
            var employee = await GetEmployee(ID);
            await context.DeleteAsync(employee);
        }

        public async Task CreateAsync(Employee employee)
        {
            employee.ID = $"{employee.Name}{employee.Surname}{rand.Next(1,1000)}";
            await context.SaveAsync(employee);
        }

    }
}
