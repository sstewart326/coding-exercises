package practice;

import java.util.concurrent.atomic.AtomicInteger;

public class ThreadPractice {

    static int vulnerableInt = 0;
    static AtomicInteger atomicInt = new AtomicInteger(0);

    static synchronized void safeIncrement() {
        vulnerableInt++;
        atomicInt.addAndGet(1);
    }

    static void unsafeIncrement() {
        vulnerableInt++;
    }

    static Runnable synchronizedTask = () -> {
        for (int i=0; i<100000; i++) {
            safeIncrement();
        }
    };

    static Runnable unsynchronizedTask = () -> {
        for (int i=0; i<100000; i++) {
            unsafeIncrement();
        }
    };

    static Thread thread1 = new Thread(synchronizedTask);
    static Thread thread2 = new Thread(synchronizedTask);

    static Thread thread3 = new Thread(unsynchronizedTask);
    static Thread thread4 = new Thread(unsynchronizedTask);

    public static void main() throws InterruptedException {
        thread1.start();
        thread2.start();
        thread1.join();
        thread2.join();
        System.out.println("Synchronized val: " + vulnerableInt);
        System.out.println("Atomic val: " + atomicInt);

        vulnerableInt = 0;
        thread3.start();
        thread4.start();
        thread3.join();
        thread4.join();
        System.out.println("Unsynchronized val: " + vulnerableInt);
    }

}
