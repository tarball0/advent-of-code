import java.io.FileReader;
import java.io.BufferedReader;

public class Main {
	public static boolean isAscending(int[] level){
		boolean result = true;
		int first, second;
		for(int i = 0; i < level.length-1; i++){
			first = level[i];
			second = level[i+1];
			if ((first >= second) || (second - first > 3)) {
				result = false;
				break;
			}
		}
		return result;
	}

	public static boolean isDescending(int[] level){
		boolean result = true;
		int first, second;
		for(int i = 0; i < level.length-1; i++){
			first = level[i];
			second = level[i+1];
			if ((first <= second) || (first - second > 3)) {
				result = false;
				break;
			}
		}
		return result;
	}

	public static boolean isSafe(int[] level){
		boolean safe = true;;
		if (!(isAscending(level)) && !(isDescending(level))) {
			safe = false;
		}
		return safe;
	}
	
	public static int count(String str, char q){
		int count = 0;
		for(int i = 0; i < str.length(); i++){
			if (str.charAt(i) == q) {
				count++;
			}
		}
		return count;
	}
	

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new FileReader("input.txt"));
		String s = br.readLine();
		int result = 0;

		while (s != null) {
			int count = 0;
			int size = count(s, ' ');
			System.out.print("size of line: " + (size+1) + ": ");
			int[] level = new int[size+1];
			String[] levelStr = new String[size+1];

			levelStr = s.split(" ");

			for(String sh : levelStr){
				System.out.print(sh + " ");
			}
			System.out.println();

			for (String data : levelStr) {
				level[count] = Integer.valueOf(data);
				count++;
			}
			if (isSafe(level)) {
				System.out.println("safe");
				result++;
			} else {
				System.out.println("unsafe");
			}
			s = br.readLine();
		}

		System.out.println("result: " + result);
		br.close();
	}
}
