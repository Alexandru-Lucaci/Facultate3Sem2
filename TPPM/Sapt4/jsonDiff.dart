// 
import 'dart:convert';
import 'dart:io';
Map<String, dynamic> jsonSubJson(String jsonPath1, String jsonPath2) {
  // Read the JSON files
  File file1 = new File(jsonPath1);
  File file2 = new File(jsonPath2);
  String jsonString1 = file1.readAsStringSync();
  String jsonString2 = file2.readAsStringSync();
  
  // Parse the JSON strings
  Map<String, dynamic> json1 = json.decode(jsonString1);
  Map<String, dynamic> json2 = json.decode(jsonString2);
  
  // Compute the difference
  Map<String, dynamic> diff = {};
  json1.forEach((key, value) {
    if (!json2.containsKey(key)) {
      diff[key] = value;
    } else if (value is Map<String, dynamic> && json2[key] is Map<String, dynamic>) {
      Map<String, dynamic> subdiff = jsonSubJsonMap(value, json2[key]);
      if (subdiff.isNotEmpty) {
        diff[key] = subdiff;
      }
    } else if (value != json2[key]) {
      diff[key] = value;
    }
  });
  
  return diff;
}

Map<String, dynamic> jsonSubJsonMap(Map<String, dynamic> map1, Map<String, dynamic> map2) {
  // Compute the difference between two maps
  Map<String, dynamic> diff = {};
  map1.forEach((key, value) {
    if (!map2.containsKey(key)) {
      diff[key] = value;
    } else if (value is Map<String, dynamic> && map2[key] is Map<String, dynamic>) {
      Map<String, dynamic> subdiff = jsonSubJsonMap(value, map2[key]);
      if (subdiff.isNotEmpty) {
        diff[key] = subdiff;
      }
    } else if (value != map2[key]) {
      diff[key] = value;
    }
  });
  return diff;
}