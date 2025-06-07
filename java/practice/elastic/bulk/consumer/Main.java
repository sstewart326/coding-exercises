package practice.elastic.bulk.consumer;

import java.util.concurrent.*;

/**
 * Problem: Build a document indexing system similar to Elasticsearch where:
 *
 * Multiple producers submit documents for indexing
 * Documents are processed in batches for efficiency (like Elasticsearch bulk API)
 * Each document submission returns a CompletableFuture<ProcessingResult>
 * Batches are processed when they reach a target size OR after a timeout
 * Processing is asynchronous and can handle failures gracefully
 */
public class Main {

    // this can grow dynamically
    private static final BlockingQueue<Document> documentQueue = new LinkedBlockingQueue<>();
    private static final ExecutorService executor = Executors.newFixedThreadPool(5);
    private static final ScheduledExecutorService scheduledExecutor = Executors.newScheduledThreadPool(2);
    private static final AsyncDocumentProducer producer = new AsyncDocumentProducer(50, scheduledExecutor, 500L, documentQueue);
    private static final Consumer consumer = new Consumer(documentQueue);

    private static final Runnable consumerWork = () -> {
        while(ApplicationState.doWork) {
            consumer.read();
        }
    };


    public static void main(String[] args) throws InterruptedException {
        for (int i=0; i<100; i++) {
            producer.startProducing(10000, executor);
        }
        Thread consumerThread = new Thread(consumerWork);
        consumerThread.start();

        Thread.sleep(10000L);
        ApplicationState.doWork = false;
        executor.shutdown();
        scheduledExecutor.shutdown();
    }


}
