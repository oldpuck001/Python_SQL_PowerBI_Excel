git_basic.md


指令目錄：
git --version
git init
git config
git add
git status
git commit
git log
git show
git diff
git checkout
git rm
git mv
git clone


(0)查看版本號: git --version

檢查安裝是否成功：在終端中執行 git --version 指令，執行結果如果出現Git的版本編號，則表示安裝成功。


(1)初始化指令: git init

git init 命令會創建一個隱藏目錄 .git ，Git將所有的修改信息都放在這個目錄中。

建立不需要的被追蹤的文件清單：在項目文件夾中新建 .gitignore 文件，將不需要追蹤的文件名寫入其中。
.gitignore 文件格式見 gitignore_format.md
常用文件清单见示例。


(2)配置提交作者: git config

設置用戶名的指令: git config --global user.name 'your_name'
設置Email的指令: git config --global user.email 'your_name@gmail.com'


(3)將文件添加到庫中: git add

添加單個文件的指令: git add your_file.md
添加所有文件的指令: git add --all

使用 git add --all 的優點：不仅会将新增和修改的文件添加到暂存区，还会处理已删除的文件。


(4)檢查當前目錄中每個文件的狀態: git status

Git中文件的四種狀態：Untracked、Tracked、Staged、Committed。


(5)建立還原點的指令: git commit -m '說明信息'

-m 是 --message 的縮寫，後面跟著的是一個簡短的提交信息。


(6)查看提交日誌的指令: git log 或者 git log --oneline


(7)查看特定提交的詳細信息: git show 提交碼

提供當前開發分支簡潔的單行摘要: git show -branch --more=10


(8)比較還原點的指令: git diff 還原點的ID --要對比的文件的文件名


(9)還原指令: git checkout 還原點的ID --要對比的文件的文件名


(10)刪除文件指令: git rm


(11)重命名文件指令: git mv


(12)複製儲存庫的指令: git clone