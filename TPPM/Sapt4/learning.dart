// template / generics
class class_name<T1, T2> {
  // described the class and use T1 and T2 as type
}

class MyTempalte<T, G> {
  T obj1;
  G obj2;
  MyTempalte(this.obj1, this.obj2);
  void Print() {
    print("MyClass(obj1=${obj1.toString()}, obj2=${obj2.toString()})");
  }
}

class Mytemplate2<T extends num> {
  T Sum(T a, T b) {
    return (a + b) as T;
  }
}

abstract class PrintInterface {void Print();}
class MyInt extends PrintInterface {
  int i;
  MyInt(this.i);
  void Print() {print(i);}
}

void main() {
  var m = MyTempalte<int, String>(1, "Hello");
  m.Print();
  var m2 = Mytemplate2<int>();
  print(m2.Sum(1, 2));
}
