package practice.elastic.bulk.consumer;

import java.util.concurrent.BlockingQueue;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.TimeUnit;

public class Consumer {

    private final BlockingQueue<Document> documentQueue;

    public Consumer(BlockingQueue<Document> documentQueue) {
        this.documentQueue = documentQueue;
    }

    public CompletableFuture<Void> read() {
        return CompletableFuture.runAsync( () -> {
            while(ApplicationState.doWork) {
                Document doc = null;
                try {
                    doc = this.documentQueue.poll(1L, TimeUnit.SECONDS);
                } catch (InterruptedException e) {
                    System.out.println("Consumer Timeout");
                }
                System.out.println("Polled " + doc.content + " " + doc.timestamp);
            }
        });
    }
}
