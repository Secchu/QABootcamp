using System.Text;

namespace BoyerMooreExtension
{
    public static class StringExtensions
    {
        public const int NoLimitMatches = -1;

        /// <summary>
        /// String extension method to search a the starting index of the occurrence of 
        /// pattern
        /// </summary>
        /// <param name="toSearch">Extension method so this is the instance.</param>
        /// <param name="pattern">The string to seek</param>
        /// <param name="startIndex">The index on the instance to begin the search</param> 
        /// <returns>The zero-based index position of value from the start of the current instance if that string is found, 
        /// or -1 if it is not.</returns>
        public static int OneTimeBoyerMooreSearch(this string toSearch, string pattern,
        int startIndex = 0)
        {
            var matched = toSearch.BoyerMooreSearch(pattern, 1, startIndex);

            if (matched.Count() == 0)
                return -1;

            return matched.Single();
        }

        /// <summary>
        /// String extension method that reports all indexes of which pattern occurs in string
        /// </summary>
        /// <param name="toSearch">Extension method so this is the instance.</param>
        /// <param name="pattern">The string to seek</param>
        /// <param name="startIndex">The index on the instance to begin the search</param> 
        /// <returns> Returns IEnumerable of all indexes in which pattern occurs in the instance string. Returns empty IEnumerable if 
        /// pattern does not occur in string.</returns>
        public static IEnumerable<int> BoyerMooreSearch(this string toSearch, string pattern, 
        int maxMatch = NoLimitMatches, int startIndex = 0)
        {
            if (pattern == null)
            {
                throw new ArgumentNullException
                ("pattern","Argument cannot be null");
            }

            int nFound = 0;
            int currentStartIndex = startIndex;
            if (pattern.Length > 0 && toSearch.Length > 0)
            {
                BadmatchTable badMatchTable = new BadmatchTable(pattern);


                while ((currentStartIndex <= toSearch.Length - pattern.Length) &&
                       nFound != maxMatch)
                {
                    int charactersLeftToMatch = pattern.Length - 1;

                    while (charactersLeftToMatch >= 0 && pattern[charactersLeftToMatch].
                        CompareTo(toSearch[currentStartIndex + charactersLeftToMatch]) == 0)
                        charactersLeftToMatch--;


                    if (charactersLeftToMatch < 0)
                    {
                        nFound++;
                        yield return currentStartIndex;
                        currentStartIndex += pattern.Length;
                    }
                    else
                    {
                        currentStartIndex += badMatchTable[toSearch[currentStartIndex + pattern.Length - 1]];
                    }
                }
            }
        }

        /// <summary>
        /// String extension method returns a new string in which all occurrences of a specified string is replaced by a specified string.
        /// </summary>
        /// <param name="toSearch">Extension method so this is the instance.</param>
        /// <param name="pattern">The string to seek</param>
        /// <param name="toReplace">The replacement string</param> 
        /// <returns> Returns an object with two properties nReplaced and Replaced. nReplaced with the number of
        /// occurrences that has been replaced. nReplaced is the number of replacements. If no characters has been replaced
        /// then nReplaced is 0 and Replaced would be the same as the instance string.</returns>
        public static (int nReplaced, string Replaced) BoyerMooreReplace(this string me, string pattern, string toReplace)
        {
            (int nReplaced, string Replaced) replacedString = (0, me);

            var tokens = me.BoyerMooreTokenize(pattern);

            var sb = new StringBuilder();

            var nLoops = tokens.Length - 1;
            for (int x = 0; x < nLoops; x++)
            {
                sb.Append(tokens[x]);

                if (toReplace != null)
                    sb.Append(toReplace);
            }

            sb.Append(tokens[tokens.Length - 1]);

            bool endsWith = false;

            if (pattern != null)
                endsWith = me.EndsWith(pattern);

            if (endsWith)
                sb.Append(toReplace);


            replacedString.nReplaced = nLoops + endsWith.ParseInt();
            replacedString.Replaced = sb.ToString();

            return replacedString;
        }

        /// <summary>
        /// String extension method that returns a string array that contains the substrings in this instance that are delimited 
        /// by elements of a specified string.
        /// </summary>
        /// <param name="me">Extension method so this is the instance.</param>
        /// <param name="delimiter">The string to seek</param>
        /// <returns> An array whose elements contain the substrings from this instance that are delimited 
        /// by delimiter</returns>
        public static string[] BoyerMooreTokenize(this string me, string delimiter)
        {
            if (delimiter == null)
                return new string[] { me };

            var offsets = me.BoyerMooreSearch(delimiter).ToList();

            if (offsets.Count == 0)
                return new string[] { me };

            var offsetJump = delimiter.Length;
            var index = 0;

            var ranges = new List<(int, int)>();

            foreach (var offset in offsets)
            {
                (int lower, int upper) range = (index, offset);
                index = offset + offsetJump;

                ranges.Add(range);
            }

            if (ranges.Count > 0)
            {
                bool leftover =
                (ranges[ranges.Count - 1].Item2 + offsetJump) < me.Length;

                if (leftover)
                {
                    (int, int) range =
                   (ranges[ranges.Count - 1].Item2 + offsetJump, me.Length);

                    ranges.Add(range);
                }
            }

            var tokens = new string[ranges.Count];

            int x = 0;

            foreach (var range in ranges)
            {
                int length = range.Item2 - range.Item1;
                tokens[x++] = me.Substring(range.Item1, length);
            }

            return tokens;
        }


    }
}