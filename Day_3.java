import java.io.IOException;
import java.io.RandomAccessFile;

public class Main {
    public static void main(String[] args) {
        //calling first method
        new Main().First();
    }
    public void First() {
        try (RandomAccessFile file = new RandomAccessFile("C:/Users/elian/Documents/javacourse/exercise/Advent/src/Data.txt", "r")) {
            String words;

            int Total = 0;

            while ((words = file.readLine()) != null) {
                final char[] left = words.substring(0, words.length() / 2).toCharArray();
                final char[] right = words.substring(words.length() / 2).toCharArray();

                boolean Found = false;

                for (char lwords : left) {
                    if (Found) {
                        break;
                    }
                    for (char rwords : right) {
                        if (lwords == rwords) { // ascii references
                            Total += (lwords <= 90) ? (lwords - 65) + 27 : (lwords - 97) + 1;
                            Found = true;
                            break;
                        }
                    }
                }
            }
            System.out.println(Total);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

}
