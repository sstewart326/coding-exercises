package practice.elastic.bulk.consumer;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;
import java.util.concurrent.*;

public class AsyncDocumentProducer {

    final UUID ID = UUID.randomUUID();
    private final int batchSize;
    private final List<Document> batchedList;
    private final BlockingQueue<Document> documentQueue;
    private final long flushInterval;
    private final Object lock = new Object();

    private long lastFlushTime = System.currentTimeMillis();
    private ScheduledExecutorService schedulerService;

    public AsyncDocumentProducer(int batchSize, ScheduledExecutorService schedulerService, long flushInterval, BlockingQueue documentQueue) {
        this.batchSize = batchSize;
        this.batchedList = new ArrayList<>(batchSize);
        this.flushInterval = flushInterval;
        this.documentQueue = documentQueue;
        this.schedulerService = schedulerService;
        this.schedulerService.scheduleAtFixedRate(this::flush, flushInterval, flushInterval, TimeUnit.MILLISECONDS);
    }

    private CompletableFuture<Void> flush() {
        return CompletableFuture.runAsync( () -> {
            if (System.currentTimeMillis() < lastFlushTime + this.flushInterval) {
                synchronized (lock) {
                    System.out.println("Flushing " + batchedList.size() + " documents");
                    this.batchedList.forEach(d -> {
                        try {
                            this.documentQueue.put(d);
                        } catch (InterruptedException e) {
                            System.out.println("Unable to put document for producer" + ID);
                        }
                    });
                    this.lastFlushTime = System.currentTimeMillis();
                }
            } else {
                System.out.println("Ignoring scheduled flush. Already flushed within flush interval");
            }
        });
    }

    public CompletableFuture<Void> startProducing(int numOfDocs, ExecutorService executorService) {
        return CompletableFuture.runAsync(() -> {
                    for (int i = 0; i < numOfDocs; i++) {
                        Document doc = new Document("doc produced by producer " + ID, System.currentTimeMillis());
                        synchronized (lock) {
                            batchedList.add(doc);
                            if (batchedList.size() == this.batchSize) {
                                batchedList.forEach(d -> {
                                    try {
                                        this.documentQueue.put(d);
                                    } catch (InterruptedException e) {
                                        System.out.println("Unable to put document for producer" + ID);
                                    }
                                });
                                batchedList.clear();
                                lastFlushTime = System.currentTimeMillis();
                            }
                        }
                    }
                    System.out.println("Producer " + ID + " produced " + numOfDocs + " documents");
                }, executorService
        );
    }

}
