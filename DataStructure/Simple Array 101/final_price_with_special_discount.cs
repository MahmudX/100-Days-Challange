using System;

class MainClass {
	public static void Main(string[] args) {
		//https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
		int[] arr = new int[] {8, 4, 6, 2, 3};
		foreach(var item in FinalPrices(arr)) {
			Console.WriteLine(item);
		}
	}
	public static int[] FinalPrices(int[] prices) {
		for (int i = 0; i < prices.Length - 1; i++) {
			for (int j = i + 1; j < prices.Length - 1; j++) {
				if (prices[i] > prices[j]) {
					prices[i] = prices[i] - prices[j];
					break;
				}
			}
		}
		return prices;
	}
}