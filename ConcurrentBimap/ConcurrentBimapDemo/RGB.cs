

namespace ConcurrentBimapDemo
{
    public class RGB
    {
        public byte Red { get; set; }
        public byte Green { get; set; }
        public byte Blue { get; set; }

        public override string ToString()
        {
            return "Red: " + Red + " Green: " + Green + " Blue: " + Blue;
        }

        public override int GetHashCode()
        {
            return base.GetHashCode();
        }

        public override bool Equals(object obj)
        {
            if (obj == null)
                return false;
            
            if(obj is RGB)
            {
                RGB rgb = (RGB)obj;

                if (Red == rgb.Red && 
                Green == rgb.Green && Blue == rgb.Blue)
                    
                    return true;
            }

            return false;
        }
    }

    public class RgbComparer : IEqualityComparer<RGB>
    {
        public bool Equals(RGB x, RGB y)
        {
            return x.Equals(y);
        }

        public int GetHashCode(RGB obj)
        {
            return obj.GetHashCode();
        }
    }

}
