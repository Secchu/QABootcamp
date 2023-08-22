namespace ServerlessDictionary.Data
{
    public interface IDictionaryRepository<K,V>
    {
        bool TryAdd(K key, V value);
        bool TryRemove(K key);
        IEnumerable<KeyValuePair<K,V>> GetAll();
        bool TryUpdate(K key, V value);
        bool TryDelete(K key);
        string Find(K key);
    }
}
