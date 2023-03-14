import 'package:tema3/tema3.dart' as tema3;
import 'package:xml_parser/xml_parser.dart' as xml;
import 'package:xml/xml.dart';
import 'dart:convert';
// import 'package:xml/xml.dart' as xml;
// import 'package:xml_parser/xml_parser.dart' as xml;

class Queue2<T> {
  List<T> _list = [];
  void push(T value) {
    _list.add(value);
  }

  T pop() {
    return _list.removeAt(0);
  }

  T back() {
    return _list.last;
  }

  T front() {
    return _list.first;
  }

  bool isEmpty() {
    return _list.isEmpty;
  }

  @override
  String toString() {
    return _list.toString();
  }
}

void defaultQueue() {
  var q = Queue2<int>();
  q.push(10);
  q.push(20);
  q.push(30);
  q.push(40);
  q.push(50);
  print(q);
  print(q.pop());
  print(q);
  print(q.back());
  print(q.front());
  print(q.isEmpty());
}
// Implement a class with a fromXml() constructor + toXml().
// class Example{
//     int varA;
//     int varB;
//     String varC;
//     List <int> varD;
//     double varE;
// }
class Example{
  int varA = 0;
  int varB = 0;
  String varC = '';
  List<int> varD = [];
  double varE = 0.0;
  Example.fromXml(String xml){
    final document = xml.parse(xmlString);
    final element = document.rootElement;
    final varA = int.parse(_getElementText(element, 'varA'));
    final varB = int.parse(_getElementText(element, 'varB'));
    final varC = _getElementText(element, 'varC');
    final varD = _getElementList(element, 'varD', 'item')
        .map((text) => int.parse(text))
        .toList();
    final varE = double.parse(_getElementText(element, 'varE'));
    return Example(varA: varA, varB: varB, varC: varC, varD: varD, varE: varE);

  }

  void toXml(){
    // return the xml
    print('test');
  }
}


void main() {
  defaultQueue();
}
