namespace ContactsApiGW.Models
{
    public interface IContactRepository
    {
        Task<IEnumerable<Contact>> GetAllContactsAsync();
        Task<string> CreateContactAsync(Contact contact);
        Task<Contact> GetContactAsync(string id);
        Task DeleteContactAsync(string id);
    }
}
