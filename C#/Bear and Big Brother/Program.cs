using System;

namespace Bear_and_Big_Brother
{
    class Program
    {
        static void Main(string[] args)
        {
            int i = 0;
            string [] input = Console.ReadLine().Split();
            int a = Convert.ToInt32(input[0]);
            int b = Convert.ToInt32(input[1]);
            do
            {
                i++;
                a *= 3;
                b *= 2;
            }
            while (a <= b);
            Console.WriteLine(i);
        }
    }
}
