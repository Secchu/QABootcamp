using Microsoft.Extensions.DependencyInjection.Extensions;
using ServerlessDictionary.Data;

namespace ServerlessDictionary;

public class Startup
{
    public Startup(IConfiguration configuration)
    {
        Configuration = configuration;
    }

    public IConfiguration Configuration { get; }

    // This method gets called by the runtime. Use this method to add services to the container
    public void ConfigureServices(IServiceCollection services)
    {
        services.AddControllers();

        KeyValuePair<string, string>[] pairs = {
                new KeyValuePair<string, string>("Sam","Sports"),
                new KeyValuePair<string, string>("Password","$ecxr@t" ),
                new KeyValuePair<string, string>("Age","Queen of hearts"),
                new KeyValuePair<string, string>("Number","10"),
                new KeyValuePair<string, string>("Currency","Pound"),
                new KeyValuePair<string, string>("Disaster","Earthquake"),
                new KeyValuePair<string, string>("Name","Bill"),
                new KeyValuePair<string, string>("Cloud","AWS")
            };

        IDictionaryRepository<string, string> dictionary = new DictionaryRepo(pairs);

        services.AddSingleton(typeof(IDictionaryRepository<string, string>), dictionary);  
    }

    // This method gets called by the runtime. Use this method to configure the HTTP request pipeline
    public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
    {
        if (env.IsDevelopment())
        {
            app.UseDeveloperExceptionPage();
        }

        app.UseHttpsRedirection();

        app.UseRouting();

        app.UseAuthorization();

        app.UseEndpoints(endpoints =>
        {
            endpoints.MapControllers();
            endpoints.MapGet("/", async context =>
            {
                await context.Response.WriteAsync("Welcome to running ASP.NET Core on AWS Lambda");
            });
        });
    }
}