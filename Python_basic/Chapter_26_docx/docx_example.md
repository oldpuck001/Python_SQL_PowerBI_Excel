docx_example.md

可以使用python-docx這個第三方庫來創建和修改Word文檔。

這個庫提供了許多功能，例如添加標題、段落、圖片和設置格式等。

安裝python-docx的命令來安裝

pip3 install python-docx


在 python-docx 中，直接通过 run.font.name 只能设置拉丁字符的字体（ascii），不能正确影响中文字符的字体。因此，为了设置中文字体，需要操作 XML 结构的 rFonts 的 w:eastAsia 属性。

代码拆解
header_run._element.rPr.rFonts.set(qn('w:eastAsia'), 'SimSun')

header_run：
表示页眉段落中一个文本运行（Run）对象。
一个Run对象代表段落中一段连续的、具有相同格式的文本。

header_run._element：
_element是底层的XML元素，表示Run的内部结构。
在Word文档的XML中，每个Run对应<w:r>标签。

header_run._element.rPr：
rPr是表示Run属性的XML元素，对应<w:rPr>标签。
它包含了与文本格式相关的所有设置，如字体、字号、颜色等。

.rFonts：
rFonts是<w:rFonts>标签，用于指定字体。
这个标签可以定义不同语言文本的字体，包括：
w:ascii：拉丁字符（英文等）的字体。
w:eastAsia：东亚字符（中文、日文、韩文等）的字体。
w:hAnsi：高 ANSI 字符的字体。
w:cs：复杂脚本（如阿拉伯语）的字体。

.set(qn('w:eastAsia'), 'SimSun')：
set方法用于修改XML属性。
qn('w:eastAsia')生成了w:eastAsia的命名空间，表示修改东亚字符字体。
'SimSun'是具体的字体名称（宋体）。