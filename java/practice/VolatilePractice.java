package practice;

public class VolatilePractice {

    static volatile boolean shouldWork = true;

    static Runnable doWork = () -> {
        while(shouldWork) {
            // do nothing
        }
        System.out.println("Done working");
    };

    static Thread thread1 = new Thread(doWork);

    public static void main() throws InterruptedException {
        thread1.start();
        Thread.sleep(1000);
        shouldWork = false;
        thread1.join();
        System.out.println("Finished Main");
    }
}
