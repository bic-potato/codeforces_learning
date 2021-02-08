using System;

namespace Helpful_Maths
{
    class Program
    {
        static void Main(string[] args)
        {
            string [] input = Console.ReadLine().Split("+");
            Array.Sort(input);
            for(int i = 0; i < input.Length; i++)
            {
                if (i != input.Length - 1)
                {
                    Console.Write(input[i] + "+");
                }
                else
                {
                    Console.WriteLine(input[i]);
                }
            }
        }
    }
}
