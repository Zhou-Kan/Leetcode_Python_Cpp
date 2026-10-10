// Input: s = "PAYPALISHIRING", numRows = 3
// Output: "PAHNAPLSIIGYIR"
import java.util.*;

public class Main{
    private String Convert(String s, int numRows) {
        if (numRows <= 1) {
            return s;
        }
        
        List<StringBuilder> rows = new ArrayList<>();

        for (int i = 0; i < numRows; i++) {
            rows.add(new StringBuilder());
        }

        int move = 1;
        int cur = 0;
        for (int i = 0; i < s.length(); i++) {
            if (i != 0 && i % (numRows - 1) == 0) {
                move *= -1;
            }
            rows.get(cur).append(s.charAt(i));
            cur += move;
        }

        StringBuilder resultSb = new StringBuilder();
        for (StringBuilder sb : rows) {
            resultSb.append(sb);
        } 
        return resultSb.toString();
    }

    public static void main(String[] args) {
        Main main = new Main();
        System.out.println(main.Convert("PAYPALISHIRING", 3));
    }
}