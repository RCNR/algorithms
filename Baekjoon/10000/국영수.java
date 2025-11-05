import java.io.*;
import java.util.*;

class Student {
    String name;
    int kor; int eng; int math;

    Student(String name, int kor, int eng, int math) {
        this.name = name;
        this.kor = kor;
        this.eng = eng;
        this.math = math;
    }
}

public class Main{

    static int n;
    static Student[] board;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        board = new Student[n];

        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            int kor = Integer.parseInt(st.nextToken());
            int eng = Integer.parseInt(st.nextToken());
            int math = Integer.parseInt(st.nextToken());

            board[i] = new Student(name, kor, eng, math);
            }

        Arrays.sort(board, (s1, s2) -> {
            if (s1.kor != s2.kor) return s2.kor - s1.kor;
            if (s1.eng != s2.eng) return s1.eng - s2.eng;
            if (s1.math != s2.math) return s2.math - s1.math;
            else return s1.name.compareTo(s2.name);
        });

        for (Student s : board) {
            bw.write(s.name + "\n");
        }

        bw.flush();

    }

}