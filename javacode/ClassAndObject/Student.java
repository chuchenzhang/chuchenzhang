// package students;

import java.io.*;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class Student
{
	private int id;
	// private String college;
	// private String major;
	// private String stu_class;
	private String name;

	public Student(int id, String name)
	{
		this.id   = id;
		this.name = name;
	}

	public String getName()
	{
		return name;
	}

	public void printStu()
	{
		System.out.println(id);
		// System.out.println(college);
		// System.out.println(major);
		// System.out.println(stu_class);
		System.out.println(name);

	}

	public static void main(String[] args)
	{
		//创建hashmap集合对象
		HashMap<String, Student> stu = new HashMap<String, Student>();

		//创建学生对象
		Student s1 = new Student(1810513215, "chuchen");
		Student s2 = new Student(1810513229, "yihan");


		//添加到学生集合
		stu.put("001", s1);
		stu.put("002", s2);

		System.out.println(stu);

		System.out.println(stu.keySet());

		for(String key: stu.keySet())
		{
			Student value = stu.get(key);
			System.out.println(key + ',' + value.getName());
		}

	}
}