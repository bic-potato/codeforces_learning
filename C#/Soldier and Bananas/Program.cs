using System;

namespace Soldier_and_Bananas
{
    class Program
    {
        static void Main(string[] args)
        {
            int count = 0;
            string [] input = Console.ReadLine().Split();
            int k = Convert.ToInt32(input[0]);
            int n = Convert.ToInt32(input[1]);
            int w = Convert.ToInt32(input[2]);
            for(int i = 1; i <= w; i++)
            {
                count += i * k;
            }
            if(count < w)
            {
                Console.WriteLine(0);
            }
            else
            {
                Console.WriteLine(count - w);
            }
        }
    }
}
