
//泛型类
class Box <T>
{
	private T t;

	public void add(T t)
	{
		this.t = t;
	}

	public T get()
	{
		return t;
	}
}

public class GenericMethod
{
	//泛型方法
	public static < E > void printArray(E[] inputArray)
	{
		//print array
		for (E element: inputArray)
		{
			System.out.println(element);
		}
	}

	public static void main(String[] args)
	{
		//创建不同类型数组
		Integer[] intArray    = {1, 2, 3, 4};
		Double[] doubleArray  = {1.2, 2.3, 4.6, 3.1};
		Character[] charArray = {'H', 'E', 'L', 'L', 'O'};

		System.out.println("int array: ");
		printArray(intArray);

		System.out.println("double array: ");
		printArray(doubleArray);

		System.out.println("char array: ");
		printArray(charArray);

		//创建泛型对象
		Box<Integer> integerBox = new Box<Integer>();
		Box<String> stringBox = new Box<String>();

		integerBox.add(new Integer(10));
		stringBox.add(new String("hello,yihan"));

		System.out.println("整型: " + integerBox.get());
		System.out.println("字符串型: " + stringBox.get());


	}
}