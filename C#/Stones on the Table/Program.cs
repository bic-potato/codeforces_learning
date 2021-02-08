using System;

namespace Stones_on_the_Table
{
    class Program
    {
        static void Main(string[] args)
        {
            int count = 0;
            int n = Convert.ToInt32(Console.ReadLine());
            string input = Console.ReadLine();
            for (int i = 0; i < n - 1; i++)
            {
                if(input[i] == input[i+1])
                {
                    count++;
                }
            }
            Console.WriteLine(count);
        }
    }
}
