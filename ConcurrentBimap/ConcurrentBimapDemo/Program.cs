using ConcurrentBimap;
using ConcurrentBimapDemo;

RgbComparer comparer = new RgbComparer();
RwBidictionary<RGB, string> colours = new RwBidictionary<RGB, string>(comparer);

RGB Red = new RGB { Blue = 0, Green = 0, Red = 255 };
RGB Blue = new RGB { Blue = 255, Red = 0, Green = 0 };
RGB Green = new RGB { Red = 0, Blue = 0, Green = 255 };

RGB Yellow = new RGB { Red = 214, Blue = 16, Green = 245 };
RGB Purple = new RGB { Red = 235, Green = 66, Blue = 212 };

RGB[] rgb = { new RGB { Blue = 0, Green = 0, Red = 255 }, new RGB { Blue = 255, Red = 0, Green = 0 }, new RGB { Red = 0, Blue = 0, Green = 255 }
                        , new RGB { Red = 214, Blue = 16, Green = 245 }, new RGB { Red = 235, Green = 66, Blue = 212 }};

string[] colors = { "Red", "Blue", "Green", "Yellow", "Purple" };



Task t1 = Task.Run(() => {

    Console.WriteLine("Hello I am thread with ID {0}. I am READER THREAD", Task.CurrentId);
   
    Random r = new Random();

    for (int i = 0; i < 100; i++)
    {


        int rnd = r.Next(0, rgb.Length - 1);

        Console.WriteLine("Checking for RGB value: " + rgb[rnd] + " should have color: " + colors[rnd]);
        bool willSucceed;

        if (colours.ContainsRightKey(rgb[rnd]))
        {
            Console.WriteLine("The Dictionary contains " + rgb[rnd] + " so tryget method should succeed");
            willSucceed = true;
        }
        else
        {
            Console.WriteLine("The Dictionary does not contain " + rgb[rnd] + " so tryget method should fail");
            willSucceed = false;
        }

        string colourKey;
        bool success = colours.TryGetRightValue(rgb[rnd], out colourKey);

        if (willSucceed == success)
            Console.WriteLine("CORRECTLY PREDICTED READING FROM READER THREAD. TASK ID: {0}", Task.CurrentId);
        else
            Console.WriteLine("SOMETHING WENT WRONG READING FROM READER THREAD THREADID {0}", Task.CurrentId);

        Console.WriteLine("Now Simulating work by sleeping reader thread");
        Thread.Sleep(r.Next(500, 1000));
    }
});

Task t2 = Task.Run(() =>
{
    Console.WriteLine("Hello I am thread with ID {0}. I am the adder thread", Task.CurrentId);

    Random r = new Random();

    for (int i = 0; i < 100; i++)
    {
        int rnd = r.Next(0, rgb.Length - 1);
        Console.WriteLine("Checking for RGB value: " + rgb[rnd]);
        bool willSucceed;

        if (colours.ContainsRightKey(rgb[rnd]))
        {
            Console.WriteLine("The Dictionary contains " + rgb[rnd] + " so addding method should fail");
            willSucceed = false;
        }
        else
        {
            Console.WriteLine("The Dictionary does not contain " + rgb[rnd] + " so adding method should succeed");
            willSucceed = true;
        }

        bool success = colours.TryAdd(rgb[rnd], colors[rnd]);

        if (willSucceed == success)
            Console.WriteLine("CORRECTLY PREDICTED ADDING. SO FAR SO GOOD FROM THE ADDER THREAD TASK{0}", Task.CurrentId);
        else
            Console.WriteLine("SOMETHING WENT WRONG ADDING TASK {0}", Task.CurrentId);

        Console.WriteLine("Now Simulating work by sleeping adder thread");
        Thread.Sleep(r.Next(500, 1000));
    }
});

Task t3 = Task.Run(() =>
{
    Console.WriteLine("Hello I am the deleter task with ID {0}", Task.CurrentId);

    Random r = new Random();

    for (int i = 0; i < 100; i++)
    {
        int rnd = r.Next(0, rgb.Length - 1);
        bool willSucceed;
        if (colours.Contains(colors[rnd]))
        {
            Console.WriteLine("Dictionary contains {0} therefore deletion should succeed", colors[rnd]);
            willSucceed = true;

        }
        else
        {
            Console.WriteLine("Dictionary contains {0} therefore deletion should succeed", rgb[rnd]);
            willSucceed = false;
        }

        bool succeed = colours.TryRemoveByLeftKey(colors[rnd]);

        if (succeed == willSucceed)
            Console.WriteLine("CORRECTLY PREDICTED DELETION. SO FAR SO GOOD FROM DELETER");
        else
            Console.WriteLine("SOMETHING WENT WRONG FOR DELETION");

        Console.WriteLine("Deleter thread simulating work");
        Thread.Sleep(r.Next(500, 1000));
    }
});

Task.WaitAll(t1, t2, t3);

Console.WriteLine("items left in dictionary {0}", colours.Count);
if (colours.Count > 0)
{
    string[] keys = colours.LeftKeys();

    Console.WriteLine("Here are all the key strings");
    foreach (string k in keys)
        Console.WriteLine(k);

    RGB[] Rgb = colours.RightKeys();

    Console.WriteLine("Here are all the RGB values left");

    foreach (RGB col in Rgb)
        Console.WriteLine(col);

    if (keys.Length != Rgb.Length)
        Console.WriteLine("Something definitely wrong");

    var enumer = colours.getLeftDictionaryEnumerator();

    while (enumer.MoveNext())
    {
        Console.WriteLine("Key: {0}", enumer.Current.Key);
        Console.WriteLine("Value: {0}", enumer.Current.Value);
    }
}
else
    Console.WriteLine("Dictionary is completely empty");

