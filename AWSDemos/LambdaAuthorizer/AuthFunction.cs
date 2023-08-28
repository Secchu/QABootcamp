using Amazon.DynamoDBv2.DataModel;
using Amazon.DynamoDBv2;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using LambdaAuthorizer.CrytographyUtils;
using LambdaAuthorizer.Model;
using Microsoft.IdentityModel.Tokens;
using Newtonsoft.Json;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace LambdaAuthorizer;

public class AuthFunction
{

    private const string secretkey = 
    "IR1OxZcrKJcLnqZmBzXHBswdLf9LIscA/UZvQvbDzlY=";
    
    private const string secretIv = "e1+doLZTWo6V+2+Ezpx9eQ==";
    private const string awsArn = "arn:aws:execute-api:ap-south-1:821175633958:sctmtm1ge8/*/*";
    private const string action = "execute-api:Invoke";

    private static AesEncryptionProvider aes = new 
    AesEncryptionProvider(secretkey, secretIv);

    private const string ApiKey = "S0M3RAN0MS3CR3T!1!MAG1C!1!";

    public APIGatewayCustomAuthorizerResponse ValidateToken
    (APIGatewayCustomAuthorizerRequest request, ILambdaContext context)
    {
        var authToken = request.Headers["authorization"];

        var claimsPrincipal = GetClaims(authToken);
        var effect = claimsPrincipal == null ? "Deny" : "Allow";
        var principalId = claimsPrincipal == null ? "401" : claimsPrincipal?.FindFirst(ClaimTypes.Name)?.Value;
        return new APIGatewayCustomAuthorizerResponse()
        {
            PrincipalID = principalId,
            PolicyDocument = new APIGatewayCustomAuthorizerPolicy()
            {
                Statement = new List<APIGatewayCustomAuthorizerPolicy.IAMPolicyStatement>
            {
                new APIGatewayCustomAuthorizerPolicy.IAMPolicyStatement()
                {
                    Effect = effect,
                    Resource = new HashSet<string> { awsArn },
                    Action = new HashSet<string> { action }
                }
            }
            }
        };
    }

    private ClaimsPrincipal GetClaims(string token)
    {
        var tokenHandler = new JwtSecurityTokenHandler();
        var validationParams = new TokenValidationParameters()
        {
            ValidateLifetime = true,
            ValidateAudience = false,
            ValidateIssuer = false,
            IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(ApiKey)),
        };
        try
        {
            return tokenHandler.ValidateToken(token, validationParams, out SecurityToken securityToken);
        }
        catch (Exception)
        {
            return null;
        }
    }

    public async Task<string> GenerateTokenAsync(APIGatewayHttpApiV2ProxyRequest request, ILambdaContext context)
    {
        var tokenRequest = JsonConvert.DeserializeObject<User>(request.Body);
        AmazonDynamoDBClient client = new AmazonDynamoDBClient();
        DynamoDBContext dbContext = new DynamoDBContext(client);

        //check if user exists in ddb
        var user = await dbContext.LoadAsync<User>(tokenRequest?.Email);

        var pwd = String.Empty;

        if (tokenRequest != null)
            if (tokenRequest.Password != null)
                pwd = decrypt(tokenRequest.Password);

        if (user == null) throw new Exception("User Not Found!");

        if (user.Password != pwd) throw new Exception("Invalid Credentials!");

        var token = GenerateJWT(user);
        return token;
    }

    public string GenerateJWT(User user)
    {
        var claims = new List<Claim> { new(ClaimTypes.Email, user.Email), new(ClaimTypes.Name, user.Username) };
        
        byte[] secret = Encoding.UTF8.GetBytes(ApiKey);
        
        var signingCredentials = new 
        SigningCredentials(new SymmetricSecurityKey(secret), SecurityAlgorithms.HmacSha256);
        
        var token = new 
        JwtSecurityToken(claims: claims, expires: DateTime.UtcNow.AddMinutes(5), signingCredentials: signingCredentials);
        
        var tokenHandler = new JwtSecurityTokenHandler();
        return tokenHandler.WriteToken(token);
    }

    public string decrypt(string pwd) => aes.Decrypt(pwd);
}
