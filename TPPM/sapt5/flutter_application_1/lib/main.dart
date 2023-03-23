import 'dart:io';

import 'package:flutter/material.dart';


void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Lista de cumpărături',
      home: ShoppingList(),
    );
  }
}

class ShoppingList extends StatefulWidget {
  @override
  _ShoppingListState createState() => _ShoppingListState();
}

class _ShoppingListState extends State<ShoppingList> {
  final List<String> items = <String>[];

  final TextEditingController controller = TextEditingController();
  var appBar = AppBar(title: const Text("Lista de cumpărături"),centerTitle: true,backgroundColor: Colors.yellow,
        foregroundColor: Colors.grey.shade800,);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: appBar,
      
      body: Column(
        children: <Widget>[
          Expanded(
            child: ListView.builder(
              padding: const EdgeInsets.all(8.0),
              itemCount: items.length,
              itemBuilder: (BuildContext context, int index) {
                final item = items[index];
                return Dismissible(
                  key: Key(item),
                  background: Container(color: Colors.red),
                  onDismissed: (direction) {
                    setState(() {
                      items.removeAt(index);
                    });
                  },
                  child: ListTile(
                    title: Text(item),
                  ),
                );
              },
            ),
            
          ),
          
          TextField(
            controller: controller,
            decoration: InputDecoration(
              labelText: 'Adăugați un element',
              labelStyle: TextStyle(color: Colors.blue.shade700),
            ),
            onSubmitted: (text) {
              setState(() {
                items.add(text);
                appBar = AppBar(title: const Text("Lista de cumparaturi"));
                controller.clear();
              });
            },
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              ElevatedButton(
                
                child: Text('Adauga element'),
                onPressed: () {
                  setState(() {
                    items.add(controller.text);
                    controller.clear();
                  });
                },
              ),
              ElevatedButton(
                child: Text('Șterge lista'),
                onPressed: () {
                  setState(() {
                    items.clear();
                  });
                },
              ),
              ElevatedButton(onPressed:(){
                setState(() {
                  try{
                    items.removeLast();
                  }catch(e){
                    // update appBar
                    
                    appBar =AppBar(title:const Text("Nu mai exista elemente de sters"));
                    // sleep(const Duration(seconds: 1));
                    controller.clear();
                    // sleep(const Duration(seconds: 1));
                    //
                    // appBar = AppBar(title: const Text("Lista de cumparaturi"));
                    // controller.clear();
                  }
                  // appBar = AppBar(title: const Text("Lista de cumparaturi"));
                });
              }, child: const Text("Sterge ultimul element"))
            ],
          ),

          
        ],
      ),

      // floatingActionButton: FloatingActionButton(
      //   onPressed: () {
      //     setState(() {
      //       items.add(controller.text);
      //       controller.clear();
      //     });
      //   },
      // )

    );
  }
}
