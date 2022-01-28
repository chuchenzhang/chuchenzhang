public class Array{
	public static void main(String[] args){
		
		int[] myList = {1,2,3};
		//打印数组
		for(int i = 0; i < myList.length; i ++){
			System.out.println(myList[i]);
		}
		//for-each循环
		System.out.println(">>>>>>>>");
		double[] arr = {1.2, 3.14, 2.68};
		for(double elem: arr){
			System.out.println(elem);
		}

		//调用函数
		System.out.println(">>>>>>>>");
		printArray(new int[]{4,5,6});

		System.out.println(">>>>>>>>");

		int[] re =reverse(myList);
		printArray(re);

		//define an two-dimensional array定义二维数组
		//2行3列
		String[][] s = new String[2][];
		s[0] = new String[3];
		s[1] = new String[3];
		s[0][0] = new String("My");
		s[0][1] = new String("Name");
		s[0][2] = new String("is");
		s[1][0] = new String("Zhang");
		s[1][1] = new String("Chuchen");
		s[1][2] = new String("Chen");

		print2Array(s);

	}

	/**
	 * print array 数组作为函数形参
	 * @param array [description]
	 */
	public static void printArray(int[] array){
		for(int i = 0; i < array.length; i ++){
			System.out.println(array[i]);
		}
	}

	/**
	 * print two-dimensional array
	 * @param array two-dimensional array
	 */
	public static void print2Array(String[][] array){
		for(int i = 0; i < array.length; i ++){
			for(int j = 0; j < array[i].length; j ++){
				System.out.println(array[i][j]);
			}
		}
	}

	/**
	 * [reverse description]
	 * @param  list dataType array
	 * @return      dataType array
	 */
	public static int[] reverse(int[] list){
		//define an array
		int[] result = new int[list.length];

		for(int i = 0, j = result.length - 1; i < list.length; i ++, j--){
			result[j] = list[i];
		}
		return result;
	}
}