namespace BasicCodes
{
  class Program
  {
    static void Main(string[] args)
    {
      Dictionary<string, int> months = new Dictionary<string, int>();
      months.Add("ocak", 30);
      months.Add("subat", 28);
      months.Add("mart", 30);
      Console.WriteLine("Ay giriniz:");
      string month = Console.ReadLine().ToLower().Trim();


      Console.WriteLine("Ortalama m3 tuketim:");
      double m3 = double.Parse(Console.ReadLine()) * months[month];

      Console.WriteLine($"{month} ayın fature tutarı {m3}.");


    }
  }
}


