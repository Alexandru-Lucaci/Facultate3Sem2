int sumSubList(List<int> l) {
  int maxSum = 0;
  int currentSum = 0;
  int start = 0;
  int end = 0;
  for (int i = 0; i < l.length; i++) {
    currentSum += l[i];
    if (currentSum > maxSum) {
      maxSum = currentSum;
      end = i;
    }
    if (currentSum < 0) {
      currentSum = 0;
      start = i + 1;
    }
  }
  print(l.sublist(start, end + 1));
  return maxSum;
}

void main() {
  var l = List<int>.from([-2, 1, -3, 4, -1, 2, 1, -5, 4]);
  print(sumSubList(l));
}
