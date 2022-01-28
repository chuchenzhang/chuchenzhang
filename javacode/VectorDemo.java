import java.util.ArrayList;
import java.util.Vector;		//向量
import java.util.Enumeration;	//枚举

public class VectorDemo {

    public static void main(String[] args) {

    	Vector<Integer> v = new Vector<Integer>(3);

    	v.add(2);
    	v.add(3);
    	v.add(4);
    	//get first element in vector
    	System.out.println(v.firstElement());

    	//enumerate the elements in vector
    	Enumeration<Integer> vEnum = v.elements();
    	System.out.println("\nElements in vector");
    	//hasMoreElements 测试此枚举中是否包含更多的元素 >= 1
    	while(vEnum.hasMoreElements()){
    		System.out.println(vEnum.nextElement());
    	}


    }
}