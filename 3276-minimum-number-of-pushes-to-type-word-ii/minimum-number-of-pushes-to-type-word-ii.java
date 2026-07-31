class Solution {
    public int minimumPushes(String word) {
        int[] freqency = new int[26];
        for (char c : word.toCharArray()) {
            freqency[c - 'a']++;
        }

        Arrays.sort(freqency);

        int totalPushes = 0;
        for (int i = 25; i >= 0; i --) {
            if (freqency[i] == 0) {
                break;
            }
            totalPushes += ((25 - i) / 8 + 1) * freqency[i];
        }

        return totalPushes;
    }
}