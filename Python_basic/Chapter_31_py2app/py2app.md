py2app.md

在服務器上安裝Python程式時，是否需要安裝打包後的版本，主要取決於您的具體需求和部署環境。以下是一些考慮因素：

1.開發與測試階段：在開發和測試階段，您可能不需要打包您的Python程式。直接在服務器上運行源代碼可能更方便，因為這樣可以輕鬆修改代碼並即時看到結果。

2.部署到生產環境：當您準備將程式部署到生產環境時，打包您的應用程序可能是一個好主意。打包可以提供多個好處，如：
依賴性管理：打包您的應用程序（例如使用PyInstaller、PyOxidizer、Docker等）可以幫助您管理依賴性，確保在您的開發環境和生產環境中有相同的依賴版本。
易於部署：打包的應用程序通常更易於部署，因為您只需要處理一個檔案或一個容器映像，而不是多個源代碼文件和依賴。
性能優化：某些打包工具允許您對Python代碼進行編譯或優化，這可能提高運行時的性能。
環境隔離：使用容器化技術（如Docker）打包您的應用程序可以提供環境隔離，保證應用程序在任何地方都能以相同的方式運行。

3.簡化安裝過程：對於需要分發給終端用戶的應用程序，打包可以簡化安裝過程，使用戶不需要手動安裝Python和各種依賴項。

總之，是否需要打包您的Python程式取決於您的特定需求。如果您希望簡化部署過程、管理依賴性、提高性能或改善用戶體驗，那麼打包可能是一個好選擇。如果您正在開發階段或者部署過程中對即時更新有高要求，可能直接運行源代碼會更合適。


py2app是一個Python模塊，用於將Python應用程序打包為Mac OS X平台上的獨立應用程序。

安裝Setuptools：

pip install setuptools

安裝py2app：

pip install py2app

創建帶GUI的可執行文件在不想給用戶增加單獨安裝Python解釋器的負擔時很有用。

下面是一個簡單的示例：

首先，創建一個空目錄，再將這個文件放到這個目錄中，然後創建一個類似於下面的setup.py文件：

from setuptools import setup
import py2app

APP = ['your_script.py']
OPTIONS = {
    'argv_emulation': True,
		'packages': ['tkinter'],
}

setup(
    app = APP,
    options = {'py2app': OPTIONS},
    setup_requires = ['py2app'],
)

这段代码是使用py2app打包Python脚本为macOS应用的配置脚本setup.py的基本形式。这里是每一部分的详解：

1.from setuptools import setup：这行代码导入了setuptools模块中的setup函数。setuptools是Python的一个库，用于帮助开发者更容易地构建和分发Python包。
2.APP = ['your_script.py']：定义了一个变量APP，这个变量是一个包含你要打包的Python脚本文件名的列表。
3.OPTIONS = {'argv_emulation': True,}：定义了一个变量OPTIONS，这个变量是一个字典，包含了传递给py2app的选项。在这个例子中，选项 'argv_emulation': True 表示启用命令行参数模拟。这会让你的应用更好地在macOS环境下运行，因为macOS的应用通常不使用命令行参数。OPTIONS字典中的'packages'键，值是一个包含'tkinter'的列表，這樣，就可以像使用其他Python模块一样在你的程序中使用tkinter。当你运行py2app时，它应该会自动找到并包含tkinter，这样你的应用就可以在没有Python环境的其他macOS电脑上运行了。注意：如果你的tkinter程序包含图像或其他资源文件，你可能需要在setup.py文件中指定这些文件的位置，以便py2app可以正确地包含它们。你可能需要使用data_files选项来完成这个操作。
4.setup(...)：这行代码调用了setup函数，进行实际的打包操作。
app = APP：这个参数指定了你要打包的应用。这里传入的是前面定义的APP变量。
options={'py2app': OPTIONS}：这个参数传递了选项给py2app。这里传入的是前面定义的OPTIONS变量。
setup_requires = ['py2app']：这个参数告诉setuptools，py2app是setup.py脚本运行所必需的包。setuptools会在运行setup.py脚本之前确保py2app已经被安装。

通过修改APP和OPTIONS中的内容，你可以更改打包的Python脚本以及py2app的选项，来满足你的具体需求。例如，你可以将'your_script.py'替换为你实际要打包的Python脚本的文件名。你也可以在OPTIONS中添加更多的选项，例如'iconfile': 'myicon.icns'，用来设置应用的图标。

'packages'與'includes'的區別：

在py2app和类似的打包工具中，'packages'和'includes'选项经常被用来确保特定的Python模块和包被包含在生成的应用中。它们之间的主要区别是它们的用途和包含内容的粒度。

如果您要包含一个整个包及其所有子模块和子包，您应该使用'packages'。因為：

'packages'用于指定整个Python包应该被包含。一个包通常是包含__init__.py文件的目录，它可能包含其他模块和子包。
当您在'packages'列表中包含一个包时，这个包以及它包含的所有模块和子包都会被包含在生成的应用中。

如果您只需要包含某个特定模块，您应该使用'includes'。因為：

'includes' 用于指定单个Python模块应该被包含。
当您在'includes'列表中包含一个模块时，只有这个特定的模块会被包含在生成的应用中。

通常，开始时在'packages'中列出所有的外部依赖包，然后运行打包过程，测试生成的应用，查看是否缺失任何模块或功能，如果缺失，可以考虑在'includes'中添加单个模块，以确保它们被包含在最终的应用中。

可像下面這樣運行這個腳本：

% python3 setup.py py2app

打包完成后，你的应用程序会被生成在 dist 目录中。你可以直接运行这个 .app 文件，就像其他macOS应用程序一样。

有關py2app的更多信息，可參閱http://pythonhosted.org/py2app。

py2exe是Setuptools的一個擴展（可通過pip來安裝它），讓你能夠創建可執行的Windows程序（.exe文件）。有關py2exe的工作原理和高級用法的詳細信息，可參閱py2exe官網（http://www.py2exe.org）。