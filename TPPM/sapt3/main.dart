import 'dart:convert';
import 'package:xml/xml.dart' as xml;
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

class Example {
  int varA = 0;
  int varB = 0;
  String varC = '';
  List<int> varD = [];
  double varE = 0.0;
  Example.fromXml(String xmll) {
    final newDoc = xml.XmlDocument.parse(xmll);
    var document = newDoc;
    varA = int.parse(document.findAllElements('varA').first.text);
    varB = int.parse(document.findAllElements('varB').first.text);
    varC = document.findAllElements('varC').first.text;
    varD = document
        .findAllElements('varD')
        .first
        .text
        .split(',')
        .map((e) => int.parse(e))
        .toList();
    varE = double.parse(document.findAllElements('varE').first.text);
  }

  xml.XmlElement toXml() {
    final builder = xml.XmlBuilder();
    builder.processing('xml', 'version="1.0"');
    builder.element('Example', nest: () {
      builder.attribute('varA', '$varA');
      builder.attribute('varB', '$varB');
      builder.attribute('varC', '$varC');
      builder.element('varD', nest: () {
        for (final value in varD) {
          builder.element('value', nest: '$value');
        }
      });
      builder.attribute('varE', '$varE');
    });
    // builder.buildDocument().rootElement;
    return builder.buildDocument().rootElement;
  }

  // implement toString()
  @override
  String toString() {
    return '''
    varA: $varA
    varB: $varB
    varC: $varC
    varD: $varD
    varE: $varE
    ''';
  }
}

class Client {
  final String name;
  double purchasesAmount = 0.0;
  Client(this.name, this.purchasesAmount);
  double get() {
    return purchasesAmount;
  }

  void add(double value) {
    purchasesAmount += value;
  }
}

class LoyalClient extends Client {
  double purchasesAmount = 0.0;
  LoyalClient(String name, double value) : super(name, value);

  @override
  double get() {
    return purchasesAmount;
  }

  void setSupper(double value) {
    super.purchasesAmount = value;
  }

  void discount() {
    print('super.purchasesAmount: ');
    print(super.purchasesAmount);
    print('this.purchasesAmount: ');
    print(this.purchasesAmount);
    this.purchasesAmount = super.purchasesAmount * 0.9;
  }
}

void main() {
  var client = Client('Alex', 0);
  client.add(100);
  print(client.get());                         
  var loyalClient = LoyalClient('Gigel', 100);
  loyalClient.add(100);
  // loyalClient.setSupper(100);
  print(loyalClient.get());
  loyalClient.discount();
  print(loyalClient.get());
}

// void main() {
//   defaultQueue();
//   var xml = '''
//   <?xml version="1.0"?>
//   <Example>
//     <varA>10</varA>
//     <varB>20</varB>
//     <varC>abc</varC>
//     <varD>1,2,3,4,5</varD>
//     <varE>3.14</varE>
//   </Example>
//   ''';
//   var e = Example.fromXml(xml);
//   print(e);
//   print(e.toXml());
// }
