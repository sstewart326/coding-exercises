package practice.elastic.bulk.consumer;

public class Document {

    final String content;
    final long timestamp;

    public Document(String content, long timestamp) {
        this.content = content;
        this.timestamp = timestamp;
    }

    @Override
    public String toString() {
        return "Document{" +
                ", content='" + content + '\'' +
                ", timestamp=" + timestamp +
                '}';
    }
}
