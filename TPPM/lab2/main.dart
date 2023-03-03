int sumSubList(List<int> l) {
  int sum = 0;
  int currentSum = 0;
  int start = 0;
  int end = 0;
  for (int i = 0; i < l.length; i++) {
    currentSum += l[i];
    if (currentSum > sum) {
      sum = currentSum;
      end = i;
    }
    if (currentSum < 0) {
      currentSum = 0;
      start = i + 1;
    }
  }
  print(l.sublist(start, end + 1));
  return sum;
}

createMap2(List<String> l) {
  var myMap = {};
  for (var i = 0; i < l.length; i++) {
    var word = l[i];
    var currentMap = myMap;
    var lastLetter = word[word.length - 1];
    for (var j = 0; j < word.length; j++) {
      var letter = word[j];
      if (currentMap[letter] == null) {
        currentMap[letter] = {};
      }
      currentMap = currentMap[letter];
    }
    currentMap[lastLetter] =
        currentMap[lastLetter] == null ? 1 : currentMap[lastLetter] + 1;
  }
  return myMap;
}

// Pentru 2 stringuri a si b, sa se verifice daca a este subsecventa a lui b. Se considera subsecventa a unui string, un nou string care este format din caracterele stringului original stergand unele caractere, fara sa schimbe pozitia caracterelor ramase (ex. "ace" este subsecventa a lui "abcde", dar "aec" nu este)
bool isSubsequence(String subString, String theString) {
  var i = 0;
  var j = 0;
  while (i < subString.length && j < theString.length) {
    if (subString[i] == theString[j]) {
      i++;
    }
    j++;
  }
  return i == subString.length;
}

int instantiateMap(Map map, String letter) {
  if (map[letter] == null) {
    return 1;
  } else {
    return map[letter]++;
  }
}

bool isAnagram(String first, String second) {
  if (first.length != second.length) {
    return false;
  }
  var firstMap = {};
  var secondMap = {};
  for (var i = 0; i < first.length; i++) {
    var letter = first[i];
    firstMap[letter] = instantiateMap(firstMap, letter);
  }
  for (var i = 0; i < second.length; i++) {
    var letter = second[i];
    secondMap[letter] = instantiateMap(secondMap, letter);
  }
  // check number of keys in both maps
  if (firstMap.keys.length != secondMap.keys.length) {
    return false;
  }
  // check if all keys in first map are in second map
  for (var key in firstMap.keys) {
    if (!secondMap.containsKey(key)) {
      return false;
    }
  }
  // check if all keys in second map are in first map
  for (var key in secondMap.keys) {
    if (!firstMap.containsKey(key)) {
      return false;
    }
  }
  // check if all values in first map are equal to values in second map
  for (var key in firstMap.keys) {
    if (firstMap[key] != secondMap[key]) {
      return false;
    }
  }

  return true;
}

void main(List<String> args) {
  print(args);
  var l = List<int>.from([-2, 1, -3, 4, -1, 2, 1, -5, 4]);
  print(sumSubList(l));

  var l2 = List<String>.from(["abcd", "adfc", "abcd", "a"]);
  print(createMap2(l2));

  print(isSubsequence("aec", "abcde"));
  print(isAnagram("abc", "cba"));
}
