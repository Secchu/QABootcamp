namespace ServerlessSesFeedback;

public class LambdaEntryPoint :

    Amazon.Lambda.AspNetCoreServer.APIGatewayProxyFunction
{

    protected override void Init(IWebHostBuilder builder)
    {
        builder
         .ConfigureAppConfiguration((context, builder) =>
         {
             builder.AddSystemsManager("/mailSettings");
         }
        )
            .UseStartup<Startup>();
    }

    protected override void Init(IHostBuilder builder)
    {
    }
}