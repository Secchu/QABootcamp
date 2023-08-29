Solution
========
This solution contains two projects. The first project is a class library that uses Boyermoore Algorithm for searching, tokenizing strings and replacing
strings. They are all string extension methods. All languages have functions to search, tokenize and replace strings. In .Net we have functions like IndexOf, 
Split and Replace.

Most of the time these functions just use a brute force approach for searching the string. They just search and compare each character from start to 
finish. Boyermoore algorithm can be more efficient if we are searching for long words because it uses a bad match table to compute the character jumps
so that it does not have to compare every single character. So single character searches such as using String.Split in .Net with the newline character
then it is better to use String.Split. You won't gain any speedup any Boyermoore. 

Note the class library does not deal with regular expressions. For that you are better using the .Net builtin functions or other libraries.

The second project is just Nunit tests that test the Boyermoore class library.

Using the Class Library
========================
Just add the project to your solution and add a project reference to the project so that you can access the class libraries.

The extension methods are listed below

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
		
        /// <summary>
        /// String extension method that returns a string array that contains the substrings in this instance that are delimited 
        /// by elements of a specified string.
        /// </summary>
        /// <param name="me">Extension method so this is the instance.</param>
        /// <param name="delimiter">The string to seek</param>
        /// <returns> An array whose elements contain the substrings from this instance that are delimited 
        /// by delimiter</returns>
        
		public static string[] BoyerMooreTokenize(this string me, string delimiter)
		

Because the BoyerMooreSearch returns IEnumerable it uses deferred execution meaning it would only perform the search when needed. For example when it 
requires to perform the iteration to search for the pattern in string. Take a look at the Nunit code snipplet below. 

            Assert.That(() => "".BoyerMooreSearch(null),
            Throws.ArgumentNullException);

The code above fails the test even though the code throws exception when null is passed in the parameter. This is because when returning IEnumerable
the codes uses deferred execution and it doesn't perform any search until the very last minute. This is found in libraries such as System.Linq. If
we wanted to force the iteration search we just need to call a function that will ask it to perform the iteration such as

            Assert.That(() => "".BoyerMooreSearch(null).Count(),
            Throws.ArgumentNullException);

BoyerMooreReplace and String.Replace
====================================
The BoyerMooreReplace extension method produces the sames results as String.Replace method. I have replaced old code that used the String.Replace with the
BoyerMooreReplace and never had any problems. There are differences to note. With String.Replace you can specify multiple delimiters and even character 
arrays. You cannot do that with BoyerMooreReplace. There is a Nunit test where both approaches are used and results are compared. Both results gave the same 
replaced string.

Also BoyerMooreReplace returns an object with replacement string in Replace and the number of replaced strings in nReplaced. String.Split simply returns
the replaced string.

 BoyerMooreTokenize and String.Split
 ===================================
The string array tokens returned by BoyerMooreTokenize is the same as String.Split when used with the StringSplitOptions.RemoveEmptyEntries.  
There is a Nunit test where both approaches are used and results are compared. Both results gave the same string array tokens. 
 
You can specify multiple charater array delimiters or string delimiters with String.Split but you cannot do that with BoyerMooreTokenize. The
extension method is suitable for searching long strings with a long delimiter. For single character delimiter your better off using String.Split.

Benchmarking
============
If you need to benchmark and test the execution speeds of any of these methods don't forget to select the release project type for optimal performance. 