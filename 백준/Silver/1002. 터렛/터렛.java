import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt(); 

        while (T-- > 0) {
            int x1 = sc.nextInt();
            int y1 = sc.nextInt();
            int r1 = sc.nextInt();

            int x2 = sc.nextInt();
            int y2 = sc.nextInt();
            int r2 = sc.nextInt();

            System.out.println(getIntersectionCount(x1, y1, r1, x2, y2, r2));
        }
    }

    private static int getIntersectionCount(int x1, int y1, int r1, int x2, int y2, int r2) {
        double distance = Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));

        if (x1 == x2 && y1 == y2 && r1 == r2) {
            return -1;
        }

        if (distance == r1 + r2 || distance == Math.abs(r1 - r2)) {
            return 1;
        }

        if (Math.abs(r1 - r2) < distance && distance < r1 + r2) {
            return 2;
        }

        return 0;
    }
}
