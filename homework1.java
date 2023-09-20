import java.util.Scanner;
public class homework1 {
    public static void main(String[] args) {
        int sum = 0;
        for(int i=0; i<5; i++){
            Scanner sc = new Scanner(System.in);
            System.out.println("정수를 입력하세요");
            int s = sc.nextInt();
            sum+=s;
            System.out.printf("현재까지 입력된 정수의 합은 %d 입니다.\n",sum);
        }
    }
}
