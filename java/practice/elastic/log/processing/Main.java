package practice.elastic.log.processing;

import java.util.List;
import java.util.Random;
import java.util.Stack;
import java.util.concurrent.LinkedBlockingQueue;

/**
 * You're building a log processing system that needs to handle multiple log streams concurrently. Implement a LogProcessor class with the following requirements:
 *
 * Method addLog(String logEntry): Adds a log entry to be processed
 * Method processLogs(): Processes all pending logs and returns them sorted by timestamp
 * Method getLogCount(): Returns the current number of unprocessed logs
 * The system must be thread-safe and handle concurrent additions while processing
 *
 * Constraints:
 *
 * Log entries format: "TIMESTAMP:LEVEL:MESSAGE" (e.g., "1623456789:ERROR:Database connection failed")
 * Multiple threads will call addLog simultaneously
 * Processing should not block new log additions
 * Return processed logs sorted by timestamp (ascending)
 */
public class Main {

    private final static LogProcessor logProcessor = new LogProcessor(new LinkedBlockingQueue<>());
    private volatile static boolean doWork = true;

    public static void main(String[] args) throws InterruptedException {

        Runnable insertLogs = () -> {
            for (int i=0; i<10000; i++) {
                logProcessor.addLog(generateRandomLog());
            }
        };

        Runnable getCount = () -> {
            while (doWork) {
                System.out.println("Current log count: " + logProcessor.getLogCount());
                try {
                    Thread.sleep(500L);
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                }
            }
        };

        Runnable processLogs = () -> {
            while (doWork) {
                List<Log> logs = logProcessor.processLogs();
                for (Log log : logs) {
                    System.out.println("Processed log: " + log);
                }
                try {
                    Thread.sleep(500L);
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                }
            }
        };
        

        Stack<Character> stack = new Stack<>();
        stack.is

        Thread thread1 = new Thread(insertLogs);
        Thread thread2 = new Thread(insertLogs);
        Thread thread3 = new Thread(insertLogs);
        Thread thread4 = new Thread(getCount);
        Thread thread5 = new Thread(processLogs);

        thread1.start();
        thread2.start();
        thread3.start();
        thread4.start();
        thread5.start();

        Thread.sleep(10000L);
        doWork = false;
    }

    private static final Random random = new Random();
    private static final String chars = "abcdefghijklmnopqrstuvwxyz0123456789";
    private static Log generateRandomLog() {
        long timestamp = System.currentTimeMillis();
        Log.Level logLevel = Log.Level.values()[random.nextInt(Log.Level.values().length)];
        StringBuilder stringBuilder = new StringBuilder();
        // num of words
        for (int i=0; i<random.nextInt(1,10); i++) {
            //chars per word
            for (int j=0; j<random.nextInt(1,12); j++) {
                stringBuilder.append(chars.charAt(random.nextInt(chars.length())));
            }
            stringBuilder.append(" ");
        }
        return new Log(timestamp, logLevel, stringBuilder.toString());
    }
}
