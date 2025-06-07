package practice.elastic.log.processing;

public record Log(long timestamp, Log.Level logLevel, String message) {

    public enum Level {
        TRACE, DEBUG, INFO, WARN, ERROR
    }

    @Override
    public String toString() {
        return this.timestamp + ":" + this.logLevel + ":" + this.message;
    }
}
