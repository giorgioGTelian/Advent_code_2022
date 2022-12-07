import java.io.RandomAccessFile;
import java.util.Random;
import java.util.Scanner;

public class Main {
    public void main(String[] args) {


        class Day4 extends Day {
               
      

            public Day4(){
                RandomAccessFile file = new RandomAccessFile("/home/giorgio/Java_prj/Binary_converter/src/file.txt", "r");

            }
        };
      
            public void part1() {
                String input = this.getInput();
                int total = 0;
                for (String line : input.split("\n")) {
                    int first = Integer.parseInt(line.substring(0,line.indexOf("-")));
                    int second = Integer.parseInt(line.substring(line.indexOf("-")+1,line.indexOf(",")));
                    int third = Integer.parseInt(line.substring(line.indexOf(",")+1,line.lastIndexOf("-")));
                    int fourth = Integer.parseInt(line.substring(line.lastIndexOf("-")+1));
                    //System.out.println(first + " " + second + " " + third + " " + fourth);
                    if (first <= third && fourth <= second || third <= first && second <= fourth){
                        total++;
                    }

                }
                System.out.println("Total: "+ total);

            }

            public void part2() {
                String input = this.getInput();
                int total = 0;
                for (String line : input.split("\n")) {
                    int first = Integer.parseInt(line.substring(0,line.indexOf("-")));
                    int second = Integer.parseInt(line.substring(line.indexOf("-")+1,line.indexOf(",")));
                    int third = Integer.parseInt(line.substring(line.indexOf(",")+1,line.lastIndexOf("-")));
                    int fourth = Integer.parseInt(line.substring(line.lastIndexOf("-")+1));
                    //System.out.println(first + " " + second + " " + third + " " + fourth);
                    if (first <= third && third <= second || first <= fourth && fourth <= second || third <= first && first <= fourth || third <= second && second <= fourth){
                        total++;
                    }

                }
                System.out.println("Total: "+ total);
            }

            private String getInput() {
                
            }
        }
    }
}
