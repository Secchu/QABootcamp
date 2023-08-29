using BoyerMooreExtension;

namespace BooyerMooreTests
{
    [TestFixture]
    public class BoolExtensionUnitTests
    {
        [Test]
        public void TestBoolExtension() 
        {
            Assert.That(false.ParseInt() == 0);
            Assert.True(true.ParseInt() == 1);
        }
    }
}
