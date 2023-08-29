using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BoyerMooreExtension
{
    public static class BooleanExtensions
    {
        public static int ParseInt(this bool b)
        {
            if (b) return 1;

            return 0;
        }
    }
}
