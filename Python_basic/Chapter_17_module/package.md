package.md

在 Python 的多級文件夾結構中，加入__init__.py文件的作用是將該文件夾標記為Python包(Package)。這使得Python可以將該文件夾中的模塊視為一個包的一部分，從而可以進行包內部的模塊導入和使用。具體來說，__init__.py文件的作用包括以下幾點：

1.標識包：__init__.py文件的存在標識了包含該文件的目錄是Python包。沒有這個文件，Python不會將該目錄視為包，即便該目錄中有其他Python文件。

2.初始化代碼：__init__.py文件可以包含包初始化時需要運行的代碼。例如，可以在這個文件中初始化包的模塊或變量，設置包的路徑，或者從包內部的其他模塊導入必要的項目。

3.隱式相對導入：當一個包內的模塊需要導入同一包中的其他模塊時，__init__.py文件的存在可以使隱式相對導入生效。例如，from . import module

4.控制包的導出行為：可以在__init__.py文件中使用__all__列表來顯式指定從包中導入 * 時應該導出的模塊或變量。

例如，假設你的多級文件夾結構如下：

my_package/
    __init__.py
    module_a.py
    sub_package/
        __init__.py
        module_b.py

在my_package/__init__.py中，你可以編寫初始化代碼或者導入包內的模塊：

# my_package/__init__.py
from .module_a import some_function
from .sub_package import module_b

在my_package/sub_package/__init__.py中，你可以編寫子包的初始化代碼：

# my_package/sub_package/__init__.py
from .module_b import another_function

這樣一來，你就可以在使用這個包時進行相對導入和包的初始化操作了。