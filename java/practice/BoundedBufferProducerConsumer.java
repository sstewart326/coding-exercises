package practice;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.UUID;
import java.util.concurrent.*;

/**
 * Simple Producer/Consumer implementation with a bounded buffer
 * Supports multiple producers and consumers with thread safety
 */
public class BoundedBufferProducerConsumer {

    private static class QueueItem {

        String value;

        public QueueItem(String value) {
            this.value = value;
        }
    }

    private static final BlockingQueue<QueueItem> queue = new ArrayBlockingQueue<>(1000);
    private static volatile boolean shutdown = false;

    public enum BackPressureStrategy {
        DROP, BLOCK, THROTTLE
    }

    static class Producer implements Runnable {

        private final UUID id = UUID.randomUUID();
        private BackPressureStrategy strategy;

        public Producer(BackPressureStrategy strategy) {
            this.strategy = strategy;
        }

        private void insertWithBlock(QueueItem item) throws InterruptedException {
            boolean submitted = false;
            while (!shutdown) {
                queue.offer(item, 1, TimeUnit.SECONDS);
            }
            if (!submitted && shutdown) {
                System.out.println("Item was not submitted before shutdown");
            }
        }

        private void insertWithDrop(QueueItem item) throws InterruptedException {
            boolean submitted = queue.offer(item, 1, TimeUnit.MICROSECONDS);
            if (!submitted) {
                System.out.println("Dropping item " + item.value);
            }
        }

        /**
         *  after .8, throttle. Only allow 20 insets over 2 seconds.
         */
        private void insertWithThrottle(QueueItem item) throws InterruptedException {
            BigDecimal remainingCapacity = BigDecimal.valueOf(queue.remainingCapacity());
            BigDecimal totalAvailable = BigDecimal.valueOf(queue.remainingCapacity() + queue.size());
            BigDecimal totalUsedPercent = BigDecimal.valueOf(.01);
            if (totalAvailable.doubleValue() != remainingCapacity.doubleValue()) {
                totalUsedPercent = totalAvailable.subtract(remainingCapacity).divide(totalAvailable, 2, RoundingMode.CEILING);
            }

            if (totalUsedPercent.doubleValue() > .8) {
                boolean saved = false;
                while (!shutdown && !saved) {
                    System.out.println("Reached " + totalUsedPercent.doubleValue() + " capacity. throttling...");
                    Thread.sleep((long) (1000 * Math.pow(totalAvailable.doubleValue(), 3)));
                    saved = queue.offer(item, 1, TimeUnit.MICROSECONDS);
                }
                if (shutdown && !saved) {
                    System.out.println("Was not able to insert the item before the shutdown " + item.value);
                }
            } else {
                queue.offer(item, 1, TimeUnit.MICROSECONDS);
            }
        }

        @Override
        public void run() {
            for (int i=0; i<1000; i++) {
                try {
                    if (shutdown) {
                        break;
                    }
                    QueueItem item = new QueueItem("item num " + i + " producer" + id);
                    switch (strategy) {
                        case DROP -> insertWithDrop(item);
                        case THROTTLE -> insertWithThrottle(item);
                        case BLOCK -> insertWithBlock(item);
                    }
                } catch (InterruptedException e) {
                    System.out.println("Error in producer " + id + ": " + e.getMessage());
                    throw new RuntimeException(e);
                }
            }
        }
    }

    static class Consumer implements Runnable {
        UUID id = UUID.randomUUID();

        @Override
        public void run() {
            while (!shutdown) {
                try {
                    QueueItem item = queue.poll(5L, TimeUnit.SECONDS);
                    Thread.sleep(5L);
                    System.out.printf("Consumer [%s] has received message [%s] %n", id, item.value );
                } catch (InterruptedException e) {
                    System.out.println("Error in consumer " + id + ": " + e.getMessage());
                    throw new RuntimeException(e);
                }
            }
        }
    }

    static class StatsCollector implements Runnable {

        @Override
        public void run() {
            try {
                while(!shutdown) {
                    System.out.println("Queue size: " + queue.size());
                    Thread.sleep(10);
                }
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }

        }
    }

    public static void main(String[] args) throws InterruptedException {
        ExecutorService executor = Executors.newFixedThreadPool(6);
        executor.submit(new Producer(BackPressureStrategy.THROTTLE));
        executor.submit(new Producer(BackPressureStrategy.THROTTLE));
        executor.submit(new Producer(BackPressureStrategy.THROTTLE));
        executor.submit(new StatsCollector());
        executor.submit(new Consumer());

        Thread.sleep(5000L);
        shutdown = true;
        Thread.sleep(2000L);
        executor.shutdown();
    }
}
