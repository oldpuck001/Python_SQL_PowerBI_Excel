vscode_basic.md

## 并排编辑：

按住 option/Alt 快捷键，同时单击资源管理器的文件。

通过 Command/Ctrl + \ 快捷键把当前编辑器分为两个。

在资源管理器的文件上右键菜单选择Open to the Side（開至側邊）。

单击编辑器右上角的Split Editor按钮。

通过拖拽，把当前文件移至上下左右任意一侧。

使用Ctrl+P / Command+P调出文件列表，选择需要打开的文件，然后按Command+Enter / Ctrl+Enter快捷键


## 配置隐藏的文件和文件夹的 glob 模式

files.exclude: {
    **/.git: true,
    **/.svn: true,
    **/.hg: true,
    **/CVS: true,
    **/.DS_Store: true
}


## 比较已选中的两个文件

在资源管理器中使用Command/Ctrl选中两个文件，右键菜单Compare Selected快速比较两个文件。


## 运行代码片段

选中代码的一行或多行，然后按下 shift+enter 或右键快捷菜单→执行Python→在Python终端机中执行项目/行


## 调试（最简单的做法）

设置断点→执行→执行但不进行侦错（F5）