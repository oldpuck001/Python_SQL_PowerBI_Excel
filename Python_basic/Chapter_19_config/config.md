config.md

在Python中，使用配置文件是一種管理和組織設定參數的好方法，特別是在你有許多需要調整的參數時。這可以讓你的代碼更加乾淨，並且容易維護。常見的配置文件格式包括INI、JSON和YAML。

使用配置文件有利有弊。一方面，配置很有用；但另一方面，使用針對整個項目的中央共享變量庫可能降低項目的模塊化程度（即增大耦合程度）。因此，使用配置文件時，務必不要破壞抽象（如封裝）。

JSON是一種輕量級的數據交換格式。Python內建的json模塊允許你輕鬆地讀取和寫入JSON格式的配置文件。

JSON（JavaScript Object Notation）是一種輕量級的數據交換格式，其結構簡單明了，通常由鍵值對組成。JSON文件可以表示對象、陣列、數字、字符串、布爾值（true/false）以及 null。

數據類型：
字符串（String）：使用雙引號包圍的文本數據，如 "Hello"。
數字（Number）：可以是整數或浮點數，如42或3.14。
布爾值（Boolean）：表示true或false。
null：表示空值，如null。
對象：如{"key": "value"}。
陣列：如[1, 2, 3]。

這些元素可以嵌套，從而構成更複雜的數據結構。

JSON文件中的字符串必須使用雙引號（"），而不能使用單引號（'）。

以下是 JSON 的基本結構和示例：

對象：對象由 {} 包圍，並由一組鍵值對組成。鍵是字符串，必須用雙引號包裹，值可以是各種JSON支持的數據類型。
{
  "name": "John",
  "age": 30,
  "isStudent": false
}


陣列：陣列由[]包圍，包含一組有序的值。值可以是各種JSON支持的數據類型，包括對象。
{
  "students": [
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 25}
  ]
}


嵌套結構：對象和陣列可以相互嵌套，從而構成更複雜的結構。
{
  "school": {
    "name": "XYZ High School",
    "location": "New York",
    "students": [
      {"name": "John", "age": 30},
      {"name": "Alice", "age": 25}
    ]
  }
}