class Solution {
    
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        // Since all words are of same length.
		int L = beginWord.length();

		// Dictionary to hold combination of words that can be formed,
		// from any given word. By changing one letter at a time.
		Map<String, List<String>> allComboDict = new HashMap<>();

		wordList.forEach(word -> {
			for (int i = 0; i < L; i++) {
				// Key is the generic word
				// Value is a list of words which have the same intermediate generic word.
				String newWord = word.substring(0, i) + '*' + word.substring(i + 1, L);
				List<String> transformations = allComboDict.getOrDefault(newWord, new ArrayList<>());
				transformations.add(word);
				allComboDict.put(newWord, transformations);
			}
		});

		// Queue for BFS
		Queue<Pair<String, List<String>>> Q = new LinkedList<>();
		Q.add(new Pair(beginWord, new ArrayList<>(Arrays.asList(beginWord))));

		// Visited keep the this levels and their parent nodes.
		Map<Integer, HashSet<String>> visitedHash = new HashMap<Integer, HashSet<String>>();
		HashSet<String> visited_begin = new HashSet<String>();
		visited_begin.add(beginWord);
		visitedHash.put(1, visited_begin);


		// result
		List<List<String>> result = new ArrayList<List<String>>();

		int miniLevel = -1;

		while (!Q.isEmpty()) {
			Pair<String, List<String>> node = Q.remove();
			String word = node.getKey();
			List<String> parentlist = node.getValue();
			int level = parentlist.size();
			HashSet<String> visited_current = new HashSet<String>();
			HashSet<String> visited_next = new HashSet<String>();
			visited_current = visitedHash.get(level);
			if(visitedHash.containsKey(level+1)) {
				visited_next = visitedHash.get(level+1);
			}else {
				visited_next = new HashSet<String>();
				visited_next.addAll(visitedHash.get(level));
			}

			if (miniLevel > 0) {
				// already find the best level
				if (level + 1 != miniLevel) {
					continue;
				}
			}
			for (int i = 0; i < L; i++) {

				// Intermediate words for current word
				String newWord = word.substring(0, i) + '*' + word.substring(i + 1, L);

				// Next states are all the words which share the same intermediate state.
				for (String adjacentWord : allComboDict.getOrDefault(newWord, new ArrayList<>())) {

					if(word.equals(adjacentWord)) {
						continue;
					}
					// If at any point if we find what we are looking for
					// i.e. the end word - we can return with the answer.
					List<String> childlist = new ArrayList<String>();
					childlist.addAll(parentlist);
					childlist.add(adjacentWord);

					if (adjacentWord.equals(endWord)) {
						if (miniLevel < 0) {
							miniLevel = level + 1;
						}
						result.add(childlist);
					} else {
						// Otherwise, add it to the BFS Queue. Also mark it visited
						if (!visited_current.contains(adjacentWord)) {
							visited_next.add(adjacentWord);

							Q.add(new Pair(adjacentWord, childlist));
							visitedHash.put(level+1, visited_next);
						}
					}

				}
			}
		}

		return result;
    }
}
