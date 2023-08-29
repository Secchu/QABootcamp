namespace BoyerMooreExtension
{
    public class BadmatchTable
    {
        private readonly int _defaultValue;
        private readonly Dictionary<int, int> _distances;

        public BadmatchTable(string pattern)
        {
            _defaultValue = pattern.Length;
            _distances = new Dictionary<int, int>();

            for (int i = 0; i < pattern.Length - 1; i++)
            {
                _distances[pattern[i]] = pattern.Length - i - 1;
            }
        }

        /// <summary>
        /// Getters and Setters for the Badmatch table class
        /// </summary>
        public int this[int index]
        {
            get
            {
                int value;
                if (!_distances.TryGetValue(index, out value))
                {
                    value = _defaultValue;
                }

                return value;
            }
            set
            {
                _distances[index] = value;
            }
        }
    }
}
