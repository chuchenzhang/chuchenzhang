import java.util.HashMap;
import java.util.Map;

public class MapDemo{

	public static void main(String args[]){
		Map<String,Integer> m1 = new HashMap<String,Integer>();

		m1.put("chuchen", 22);
		m1.put("yihan", 16);
		m1.put("hui", 21);
		System.out.println(m1);
		System.out.println("map size is: " + m1.size());
	}
}