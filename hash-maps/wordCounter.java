import java.util.HashMap;

public static HashMap<String, Integer> wordCounter(String document) {
    HashMap<String, Integer> counts = new HashMap<String, Integer>();
    for (String word : document.split(" ")) {
        String key = word.toLowerCase().replaceAll("[^a-zA-Z]", "");
        if (counts.containsKey(key)) {
            counts.put(key, counts.get(key) + 1);
        } else {
            counts.put(key, 1);
        }
    }
    return counts;
}