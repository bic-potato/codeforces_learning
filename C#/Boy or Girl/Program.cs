using System;
using System.Collections;

namespace Boy_or_Girl
{
    class Program
    {
        static void Main(string[] args)
        {
            string input = Console.ReadLine();
            Hashtable dict1 = new Hashtable();
            for(int i = 0; i< input.Length; i++)
            {
                if (dict1.Contains(input[i]) == false)
                {
                    dict1.Add(input[i], 0);
                }
            }
            if(dict1.Count % 2 == 0)
            {
                Console.WriteLine("CHAT WITH HER!");
            }
            else
            {
                Console.WriteLine("IGNORE HIM!");
            }
        }
    }
}
