import java.io.*;
import employee.Employee;

public class EmployeeTest
{
	public static void main(String[] args)
	{
		Employee emp1 = new Employee("chuchen");
		Employee emp2 = new Employee("yihan");

		emp1.empAge(22);
		emp1.empDesignation("高级程序员");
		emp1.empSalary(10000);
		emp1.printEmployee();
	}
}