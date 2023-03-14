class Test {
  var x;
  var y = 10;

  // empty class
}

class Test2 {
  final int x = 30;
  // x cannot be changed. Nu se mai creează setterul pentru x
  int? y;
  // y can be null
  int z = 10;
  // z cannot be null
  static int a = 10;
  // a is a static variable, the getter and setter are not generated


}
// var  t = Test2(); // cannot be instantiated
// print(Test2.a); // 10
void main() {
  var t = Test();
  print(t);
  print(t.runtimeType);
  print(t.hashCode);
  print(t.toString());
}
