using System;

namespace Word_Capitalization
{
    class Program
    {
        protected static string Capitalize (string str1)
        {
            char FirstLetter = Convert.ToChar(str1[0]);
            char UpperedFirstLetter = Char.ToUpper(FirstLetter);
            string str2 = str1.Remove(0, 1);
            string str3 = str2.Insert(0, Convert.ToString(UpperedFirstLetter));
            return str3;
        }
        static void Main(string[] args)
        {
            Console.WriteLine(Capitalize(Console.ReadLine()));
        }
    }
}
