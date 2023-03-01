
// list constractor
// var l = List<int>.from([1, 2, 3, 4]);
// var l = [1, 2, 3, 4];
// var l = List<int>.filled(10, 0);
// var l = List<int>.generate(10, (index) => index * 2);
// var l = List<int>.generate(10, (index) => index * 2);
// Add elements
// l.add(5);
// l.addAll([6, 7, 8, 9, 10]);
// l.insert(0, 0);
// l.insertAll(0, [-1, -2, -3, -4, -5]);
// l.remove(5);
// l.removeAt(0);
// l.removeLast();
// l.removeRange(0, 5);
// l.removeWhere((element) => element % 2 == 0);
// l.clear();
// l.fillRange(0, 5, 0);
// l.replaceRange(0, 5, [0, 0, 0, 0, 0]);
// l.setAll(0, [0, 0, 0, 0, 0]);
//  l.retainWhere((element) => element % 2 == 0); - oferim o funcție callback
// Check the existanxe of an element in a list use the following apis
// l.contains(5);
// l.indexOf(5);
// l.indexAt(5);
// l.lastIndexOf(5);
// l.indexWhere((element) => element % 2 == 0);
// process a list
// l.getrange(0, 5);
// l.sublist(0, 5);
// l.map((e) => e * 2).toList();
// l.where((element) => element % 2 == 0).toList();
// l.forEach((element) => print(element));
// l.sublist(0, 5).forEach((element) => print(element)); - it is the same as the previous line
// l.take(int count) - return the first count elements



void main() {
  print("hello");
  var l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  print(l);
  var k = <int>[]; // empty list
  var kl = List<int>.from([1, 2, 3, 4]);

  var m = ["hello", "world", "how", "are", "you"];
  print(l.first);
  print(l.last);
  print(l.length);
  print(l.isEmpty);
  print(l.isNotEmpty);
  print(l.reversed);  // este un iterabil (Iterable)
  print(l.reversed.toList());
}
//