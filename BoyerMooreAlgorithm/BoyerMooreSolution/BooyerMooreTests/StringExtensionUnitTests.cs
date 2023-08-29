using BoyerMooreExtension;
using Microsoft.VisualStudio.TestPlatform.CommunicationUtilities;
using System.ComponentModel.DataAnnotations;

namespace BooyerMooreTests
{

    public class StringExtensionUnitTests
    {
        [TestCase("Have a nice day", "day", ExpectedResult = 12)]
        [TestCase("AWS and Azure are two examples of Clouds", "AWS", ExpectedResult = 0)]
        [TestCase("AWS and Azure are two examples of Clouds", "Azure", ExpectedResult = 8)]
        [TestCase("AWS and Azure are two examples of Clouds", "examples", ExpectedResult = 22)]
        [TestCase("AWS and Azure are two examples of Clouds", "NonExistant", ExpectedResult = -1)]
        public int OneTimeBoyerMooreShouldRtnOffsetOfPatternInString(string str, string pattern)
        {
            return str.OneTimeBoyerMooreSearch(pattern);
        }

        [TestCase("Play,I am Playing, She is Playing", "Play", 0, -1, new int[] { 0, 10, 26 })]
        [TestCase("Play,I am Playing, She is Playing", "Play", 0, 2, new int[] { 0, 10 })]
        [TestCase("Play,I am Playing, She is Playing", "Play", 1, 2, new int[] { 10, 26 })]
        [TestCase("Play,I am Playing, She is Playing", "Play", 1, 1, new int[] { 10 })]
        public void BoyerMooreSearchShouldRtnCorrectOffsetsAsEnumerable(string str, string pattern
        , int startIndex, int maxOccurrence, int[] expected)
        {
            var results = str.BoyerMooreSearch(pattern, maxOccurrence, startIndex);

            Assert.That(expected.SequenceEqual(results));
        }

        [TestCase("You can call me {name}", "{name}", 
        new string[] { "You can call me " })]

        [TestCase("You can call me {name}", "name",
        new string[] { "You can call me {", "}" })]

        [TestCase("You can call me {name}", "{name}.",
        new string[] { "You can call me {name}"})]

        [TestCase("You can call me {name}. You can call my brother {name}.",
        "{name}", new string[] { "You can call me ",
        ". You can call my brother ","."})]

        [TestCase("You can call me {name}. You can call my brother {name}.",
        "name", new string[] { "You can call me {", "}. You can call my brother {", "}." })]

        [TestCase("You can call me {name}. You can call my brother {name}.",
         "{name}.", new string[] { "You can call me ", " You can call my brother " })]

        [TestCase("You can call me {name}. You can call my brother {name}. My sisters friend is also called {name}",
         "{name}", new string[] { "You can call me ", ". You can call my brother ",
         ". My sisters friend is also called "})]

        [TestCase("You can call me {name}. You can call my brother {name}. My sisters friend is also called {name}",
         "name", new string[] { "You can call me {", "}. You can call my brother {",
         "}. My sisters friend is also called {","}"})]

        [TestCase("You can call me {name}. You can call my brother {name}. My sisters friend is also called {name}",
         "{name}.", new string[] { "You can call me ", " You can call my brother ",
         " My sisters friend is also called {name}"})]
        public void BoyerMooreTokenizeShouldRtnCorrectTokens
        (string str, string delimiter, string[] expected)
        {
            var results = str.BoyerMooreTokenize(delimiter);

            Assert.That(expected.SequenceEqual(results));
        }

        /*
         * I want the BooyerMooreTokenize method be a feasible replacement
         * for the Split method of the string class with the StringSplitOptions.RemoveEmptyEntries
         * option. Unit test will compare the results of both methods
         */
        [Test, Combinatorial]
        public void BooyerMoreTokenizeShouldGiveSameResultsAsStringSplit([Values("You can call me {name}", "You can call me {name}. You can call my brother {name}.",
        "You can call me {name}. You can call my brother {name}. My sisters friend is also called {name}")] string str,
        [Values("{name}", "name", "{name}.")] string delimiter)
        {
            string[] expectedTokens = str.Split(delimiter, StringSplitOptions.RemoveEmptyEntries);
            var results = str.BoyerMooreTokenize(delimiter);

            Assert.That(results.GetType(), Is.EqualTo(expectedTokens.GetType()));
            Assert.That(results.Length, Is.EqualTo(expectedTokens.Length));
            Assert.That(results, Is.All.InstanceOf<string>());
            Assert.That(expectedTokens.SequenceEqual(results));
        }


        [TestCase("AWS is cloud. Azure is also cloud. its cloud",
         "cloud","nice", "AWS is nice. Azure is also nice. its nice", 3)]

        [TestCase("I love to eat","to eat","to go eating",
         "I love to go eating", 1)]

        [TestCase("I hate this", " this","","I hate", 1)]

        [TestCase("Erase","E","e","erase",1)]

        [TestCase("Its not there", "and it isn't", "", 
        "Its not there", 0)]
        public void BoyerMooreReplaceShouldRtnCorrectReplacement
        (string str, string pattern, string toReplace, string expected, 
         int nReplaced)
        {
            var result = str.BoyerMooreReplace(pattern, toReplace);

            Assert.That(result.Replaced == expected);
            Assert.That(result.nReplaced == nReplaced);
        }

        /*
            I want the BoyerMooreReplace method to be able replace the
            String.Replace method.

            This unit tests compares the results of both methods.

            The BoyerMooreReplace methods differs in that it returns
            the replaced string and the number of replacements as 
            (Replaced, nReplaced)
         */

        [Test, Combinatorial]
        public void BoyerMooreReplaceShouldGiveSameResultsAsStringReplace
        ([Values("You can call me {name}", "You can call me {name}. You can call my brother {name}.",
        "You can call me {name}. You can call my brother {name}. My sisters friend is also called {name}")]string testString,
        [Values("{name}", "name", "{name}.")] string pattern,
        
        //"string".replace(pattern,null) is perfectly valid
        [Values("Collins", "Jones", "Johnson", "", null)] string replacement)
        {
            var expectedNReplace = testString.BoyerMooreSearch(pattern).ToList().Count;
            
            var expected = testString.Replace(pattern, replacement);
            var results = testString.BoyerMooreReplace(pattern, replacement);

            Assert.That(results.Replaced, Is.InstanceOf<string>());
            Assert.That(results.Replaced, Is.EqualTo(expected));
            Assert.That(results.nReplaced, Is.EqualTo(expectedNReplace));
        }

        [Test]
        public void AssertBadmatchIndexerValues()
        {
            var table = 
            new BadmatchTable("Creative");

            var expectedDict = new Dictionary<int, int>()
            {
                {'C', 7}, {'r', 6}, {'e', 5}, {'a', 4},
                {'t', 3}, {'i', 2},{'v', 1}
            };


            foreach (var expected in expectedDict)
                 Assert.That(table[expected.Key] == expected.Value);
            
            table = new BadmatchTable("play play play");

            expectedDict = new Dictionary<int, int>()
            {
                {'p', 3}, {'l', 2}, {'a', 1}, {'y', 5},
                {' ', 4}
            };

            foreach (var expected in expectedDict)
                Assert.That(table[expected.Key] == expected.Value);
        }

        /*
         * I am being lazy and just copy and pasted code from the previous
         * test. When working in production you would want to minimise on
         * duplicate code and put repeated code in methods.
         */

        [Test]
        public void AssertBadmatchIndexerUpdateValues()
        {
            var table =
            new BadmatchTable("Creative");

            table['C'] = 5;
            table['l'] = 9;
            table['y'] = 10;

            var expectedDict = new Dictionary<int, int>()
            {
                {'C', 5}, {'r', 6}, {'e', 5}, {'a', 4},
                {'t', 3}, {'i', 2},{'v', 1}, {'l',9},
                {'y', 10}
            };


            foreach (var expected in expectedDict)
                Assert.That(table[expected.Key] == expected.Value);

            table = new BadmatchTable("play play play");

            table['p'] = 5;
            table['e'] = 6;
            table['d'] = 7;

            expectedDict = new Dictionary<int, int>()
            {
                {'p', 5}, {'l', 2}, {'a', 1}, {'y', 5},
                {' ', 4}, {'e', 6}, {'d', 7}
            };

            foreach (var expected in expectedDict)
                Assert.That(table[expected.Key] == expected.Value);
        }

        [Test]
        public void AssertThrowsBoyerMooreSearchThrowsExWhenPattenIsNull()
        {
            //Deffered Execution so using Count() to get function to
            //immediately execute
            Assert.That(() => "".BoyerMooreSearch(null).Count(),
            Throws.ArgumentNullException);

            //Deferred execution again but it is deferred in the
            //OneTimeBoyerMooreSearch method because it calls
            //the Single method.
            Assert.That(() => "".OneTimeBoyerMooreSearch(null),
            Throws.ArgumentNullException);
        }

    }
}