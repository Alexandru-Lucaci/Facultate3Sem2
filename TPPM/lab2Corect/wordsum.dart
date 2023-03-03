import 'dart:io';
import 'dart:convert';

// wordsum.dart A 5 B 3 C 9 ABBCC
void main(List<String> args) {
  if (args.length < 3) {
    print('Please enter at least 3 arguments');
    var argss = stdin.readLineSync();
    print(argss);
    args = argss.toString().split(' ');
  }
  print(args);
  var myMap = {};
  for (var i = 0; i < args.length - 1; i += 2) {
    if (i % 2 == 0) {
      myMap[args[i]] = int.parse(args[i + 1]);
    }
  }
  var word = args[args.length - 1];
  num sum = 0;
  for (var i = 0; i < word.length; i++) {
    sum += myMap[word[i]];
  }
  print(myMap);
  print(sum);
}
