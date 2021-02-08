using System;

namespace BerOS_file_system
{
    class Program
    {
        public static int CountChar(string str, char chara)
        {
            int coun = 0;
            for(int i = 0; i < str.Length; i++)
            {
                if (str[i] == chara)
                {
                    coun++;
                }
            }
            return coun;
        }
        static void Main(string[] args)
        {
            string input = Console.ReadLine();
            for (int i = 0; i < input.Length - 1; i++)
            {
                if(input[i] =='/' && input[i+1] == '/')
                {
                    continue;
                }
                else
                {
                    Console.Write(input[i]);
                }
            }
            if (input[input.Length - 1] != '/' || CountChar(input, '/') == input.Length)
            {
                Console.WriteLine(input[input.Length - 1]);
            }
        }
    }
}
