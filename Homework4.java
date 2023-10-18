import java.util.Scanner;

public class Homework4 {

    public static int gcd(int m, int n) {
        if (n == 0) {
            return m;
        } else {
            return gcd(n, m % n);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("두 정수를 입력하세요: ");
        int m = scanner.nextInt();
        int n = scanner.nextInt();

        int result = gcd(m, n);
        System.out.println("최대공약수는 " + result + "입니다.");
    }
}
