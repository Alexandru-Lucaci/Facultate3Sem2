
import 'dart:io';
import 'dart:typed_data';
import 'jsonDiff.dart' as  jsonDiff;
Map<String, List<dynamic>> match(String s, List<RegExp> l) {
  List<String> result = [];
  List<dynamic> matches = [];
  for (RegExp r in l) {
    if (r.hasMatch(s)) {
      result.add(s);
      // add only the part
      //  type of r.stringMath(s) 
      matches.add(r.stringMatch(s));

    }
  }
  // make a tuple of the two lists
  var dict = {
    "result": result,
    "matches": matches
  };

  return dict;
}


class MyStack {
  final String _filePath;
  final int _maxSize;
  int _top;

  MyStack({required String filePath, int maxSize = 100})
      : _filePath = filePath,
        _maxSize = maxSize,
        _top = -1 {
    // create the file if not existed
    File(_filePath).createSync(recursive: true);

    // Read the first line of the file to get the position of the last element in the stack
    String? positionString = null;
    try{ 
      String? positionString = File(_filePath).readAsLinesSync().first;
    }catch(e){
      print('Clean file');
    }
    if (positionString != null && positionString.isNotEmpty) {
      _top = int.parse(positionString);
    }
  }

  void push(int value) {
    if (_top == _maxSize - 1) {
      print('Stack is full');
      return;
    }

    // Write the new value to the file
    File(_filePath).writeAsStringSync('${value.toString()}\n', mode: FileMode.append);

    _top++;
  }

  int pop() {
    if (_top == -1) {
      print('Stack is empty');
      return -1;
    }

    // Read the value of the top element from the file
    List<String> lines = File(_filePath).readAsLinesSync();
    int value = int.parse(lines[_top]);
    //print(value);

    // remove the last element 
    lines.removeLast();
    File(_filePath).writeAsStringSync('', mode: FileMode.write);
    int lenghtValue = value.toString().length;
    //print(lenghtValue);
    for(var element in lines)
      File(_filePath).writeAsStringSync('${element.toString()}\n', mode: FileMode.append);
    _top--;
    return value;
  }

  int peek() {
    if (_top == -1) {
      print('Stack is empty');
      return -1;
    }

    // Read the value of the top element from the file
    List<String> lines = File(_filePath).readAsLinesSync();
    int value = int.parse(lines[_top]);
    
    return value;
  }

  bool isEmpty() {
    return _top == -1;
  }
}

class MathOps<T, G> {
  
  int sub(T obj1, G obj2) {
    if (obj1 is int && obj2 is int) {
      return obj1 - obj2;
    } else if (obj1 is double && obj2 is double) {
      return (obj1 - obj2).toInt();
    } else if (obj1 is String && obj2 is String) {
      dynamic val1 = int.tryParse(obj1);
      dynamic val2 = int.tryParse(obj2);
      if (val1 != null && val2 != null) {
        return val1 - val2;
      } else {
        throw new ArgumentError("Both Strings must represent integers.");
      }
    } else {
      throw new ArgumentError("The types of the arguments are not supported.");
    }
  }
  
  int prod(T obj1, G obj2) {
    if (obj1 is int && obj2 is int) {
      return obj1 * obj2;
    } else if (obj1 is double && obj2 is double) {
      return (obj1 * obj2).toInt();
    } else if (obj1 is String && obj2 is String) {
    
      dynamic val1 = int.tryParse(obj1);
      dynamic val2 = int.tryParse(obj2);


      if (val1 != null && val2 != null) {
        return val1 * val2;
      } else {
        throw new ArgumentError("Both Strings must represent integers.");
      }
    } else {
      throw new ArgumentError("The types of the arguments are not supported.");
    }
  }
  
  int mod(T obj1, G obj2) {
    if (obj1 is int && obj2 is int) {
      return obj1 % obj2;
    } else if (obj1 is double && obj2 is double) {
      return (obj1 % obj2).toInt();
    } else {
      if (obj1 is String && obj2 is String) {
        dynamic val1 = int.tryParse(obj1);
        dynamic val2 = int.tryParse(obj2);
        if (val1 != null && val2 != null) {
          return val1 % val2;
        } else {
          throw new ArgumentError("Both Strings must represent integers.");
        }
      } else {
        throw new ArgumentError("The types of the arguments are not supported.");
      }
    }
  }
  
}
void main(){
  // regex for matching a word
  RegExp r = RegExp(r"\w+");
  // regex for matching a number
  RegExp r2 = RegExp(r"\d+");
  print(match("Hello 22 World", [RegExp(r"Hello"), RegExp(r"World"),r,r2])); // [Hello]

  // 2. Implementati o Stiva folosind fisiere ca storage.
  MyStack fs = MyStack(filePath: "stack.txt");
  fs.push(1);
  fs.push(2);
  fs.push(3);
  print(fs.peek()); // 3 
  print(fs.pop()); // 3
  print(fs.pop()); // 2
  print(fs.pop()); // 1
  print(fs.pop()); // -1
  print(fs.pop()); // -1
  print(fs.peek()); // -1
  print(fs.isEmpty()); // true

  MathOps<int, int> m = MathOps();
  print(m.sub(1, 2)); // -1
  print(m.sub(1, 4)); // -1

  MathOps<double, double> m2 = MathOps();
  print(m2.sub(1.0, 2.0)); // -1
  print(m2.sub(1.0, 4.0)); // -1
  print(m2.prod(1.0, 2.0)); // 2
  print(m2.prod(1.0, 4.0)); // 4
  print(m2.mod(1.0, 2.0)); // 1
  print(m2.mod(1.0, 4.0)); // 1

  MathOps<String, String> m3 = MathOps();
  print(m3.sub("1", "2")); // -1
  print(m3.sub("1", "4")); // -1
  print(m3.prod("1", "2")); // 2
  print(m3.prod("1", "4")); // 4
  print(m3.mod("1", "2")); // 1
  print(m3.mod("1", "4")); // 1

  print(jsonDiff.jsonSubJson("C:\\Stuff\\Repo\\Facultate3Sem2\\TPPM\\json1.json", "C:\\Stuff\\Repo\\Facultate3Sem2\\TPPM\\json2.json"));


}