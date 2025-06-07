package practice.elastic.log.processing;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;

public class LogProcessor {

    // Blocks consumers if queue is empty, producers if queue is full
    // Thread safe and allows simultaneous reads and writes
    BlockingQueue<Log> queue;
    // Thread safe counter
    AtomicInteger count = new AtomicInteger(0);

    public LogProcessor(BlockingQueue<Log> queue) {
        this.queue = queue;
    }

    public boolean addLog(Log logEntry) {
        try {
            boolean inserted = this.queue.offer(logEntry, 1L, TimeUnit.SECONDS);
            if (inserted) {
                count.incrementAndGet();
            }
            return inserted;
        } catch (InterruptedException e) {
            System.out.println("Unable to add log " + logEntry);
            return false;
        }
    }

    public List<Log> processLogs() {
        List<Log> logs = new ArrayList<>();
        for (int i=0; i<count.get(); i++) {
            logs.add(this.queue.poll());
            count.decrementAndGet();
        }
        logs.sort(Comparator.comparingLong(Log::timestamp));
        return logs;
    }

    public int getLogCount() {
        return count.get();
    }

}
