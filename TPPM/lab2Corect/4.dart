int sumaCifre(int n) {
  int sum = 0;
  while (n > 0) {
    sum += n % 10;
    n = n ~/ 10;
  }
  return sum;
}

void generareGrupuri(int n) {
  var myMap = {};
  for (var i = 1; i <= n; i++) {
    var sum = sumaCifre(i);
    if (myMap.containsKey(sum)) {
      myMap[sum].add(i);
    } else {
      myMap[sum] = [i];
    }
  }
  print(myMap);
  var max = 0;
  for (var i in myMap.values) {
    if (i.length > max) {
      max = i.length;
    }
  }
  print(max);
  var count = 0;
  for (var i in myMap.values) {
    if (i.length == max) {
      count++;
    }
  }
  print(count);
}

void main() {
  generareGrupuri(30);
}
