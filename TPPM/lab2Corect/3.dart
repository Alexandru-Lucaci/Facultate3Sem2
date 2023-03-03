int numarPerechiBune(List<int> lst) {
  Set<Set<int>> perechiBune = {};
  for (int i = 0; i < lst.length; i++) {
    for (int j = i + 1; j < lst.length; j++) {
      if (lst[i] == lst[j]) {
        perechiBune.add({i, j});
      }
    }
  }
  print(perechiBune);
  return perechiBune.length;
}

void main() {
  print(numarPerechiBune([1, 2, 3, 3, 5, 6, 2, 8, 9, 8]));
}
