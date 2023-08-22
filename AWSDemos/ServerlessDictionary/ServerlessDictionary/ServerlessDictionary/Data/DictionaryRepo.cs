using System.Collections.Concurrent;

namespace ServerlessDictionary.Data
{
    public class DictionaryRepo : IDictionaryRepository<string, string>
    {
        private ConcurrentDictionary<string, string> dictionary;

        public DictionaryRepo() 
        {
            dictionary = new ConcurrentDictionary<string, string>();
        }

        public DictionaryRepo(IEnumerable<KeyValuePair<string, string>> keyValuePairs)
        {
            dictionary = new ConcurrentDictionary<string, string>(keyValuePairs);
        }

        public string Find(string key)
        {
            string value;

            dictionary.TryGetValue(key, out value);

            return value;
        }

        public IEnumerable<KeyValuePair<string, string>> GetAll()
        {
            return dictionary.ToArray();
        }

        public bool TryAdd(string key, string value)
        {
            if (key == null || value == null)
                return false;

            return dictionary.TryAdd(key, value);
               
        }

        public bool TryDelete(string key)
        {
            if (key == null)
                return false;

            string value;
            return dictionary.TryRemove(key, out value);
        }

        public bool TryRemove(string key)
        {
            if (key == null)
                return false;
            
            string value;
            return dictionary.TryRemove(key, out value);
        }

        public bool TryUpdate(string key, string value)
        {
            if (key == null || value == null)
                return false;

            string oldValue;
            if (!dictionary.TryGetValue(key, out oldValue))
                return false;

            return dictionary.TryUpdate(key, value, oldValue);    
        }
    }
}
