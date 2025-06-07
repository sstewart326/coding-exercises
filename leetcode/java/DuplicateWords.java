import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class DuplicateWords {

    private static Set<String> findDuplicateWords(String text) {
        Map<String, Integer> wordCounts = new HashMap<>();
        Set<String> uniqueWords = new HashSet<>();

        for (String word : text.split(" ")) {
            Integer count = wordCounts.getOrDefault(word, 0);
            wordCounts.put(word, ++count);
        }

        for (Map.Entry<String, Integer> entry : wordCounts.entrySet()) {
            if (entry.getValue() > 1) {
                uniqueWords.add(entry.getKey());
            }
        }
        return uniqueWords;
    }

    public static void main() {
        System.out.println(findDuplicateWords("This is this rhythm of night this night"));
    }

}
