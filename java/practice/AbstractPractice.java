package practice;

public class AbstractPractice {

    interface Message {
        void processMessage(String message);
    }

    static abstract class MessageProcessor implements Message {

        @Override
        public void processMessage(String message) {
            if (validateMessage(message)) {
                System.out.println("Message processed successfully");
            } else {
                System.out.println("Message failed to process");
            }
        }

        protected abstract boolean validateMessage(String message);
    }

    static class EmailMessage extends MessageProcessor {

        @Override
        protected boolean validateMessage(String message) {
            return message.contains("@");
        }
    }

    static class SMSMessage extends MessageProcessor {

        @Override
        protected boolean validateMessage(String message) {
            return message.length() < 160;
        }
    }

    public static void main(String[] args) {
        Message email = new EmailMessage();
        email.processMessage("valid@email.com");
        email.processMessage("invalidemail.com");

        Message sms = new SMSMessage();
        sms.processMessage("Valid text");
        sms.processMessage("This message is way too long like omg please make it stop right now ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh");
    }

}
