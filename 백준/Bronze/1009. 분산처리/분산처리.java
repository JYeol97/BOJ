import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine().trim());

        Map<Integer, int[]> cycles = new HashMap<>();
        cycles.put(2, new int[]{2, 4, 8, 6});
        cycles.put(3, new int[]{3, 9, 7, 1});
        cycles.put(4, new int[]{4, 6});
        cycles.put(7, new int[]{7, 9, 3, 1});
        cycles.put(8, new int[]{8, 4, 2, 6});
        cycles.put(9, new int[]{9, 1});

        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            long a = Long.parseLong(st.nextToken());
            long b = Long.parseLong(st.nextToken());

            int last = (int)(a % 10);

            int ans;
            if (b == 0) {
                ans = 1;
            } else if (last == 0) {
                ans = 10; 
            } else if (last == 1 || last == 5 || last == 6) {
                ans = last; 
            } else {
                int[] cyc = cycles.get(last);
                int len = cyc.length;
                int idx = (int)((b - 1) % len); 
                ans = cyc[idx];
            }

            sb.append(ans).append('\n');
        }

        System.out.print(sb);
    }
}
