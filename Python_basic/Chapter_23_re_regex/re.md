re.md

標準庫：re

在Python中，通常使用re模塊來處理正表達式。

完整的正則表達式運算符清單請參閱Python庫中的Regular Expression Syntax部分。

模塊re包含多個使用正則表達式的函數，下面是模塊re中一些重要的函數：
以下函數中有些接受一個名為flags的可選參數。這個參數可用於修改正則表達式的解讀方案。有關這方面的詳細信息，請參閱“Python參考庫手冊”中討論模塊re的部分。


compile：將用字符串表示的正則表達式轉換為模式對象
compile(pattern[,flags])          將用字符串表示的正則表達式轉換為模式對象
調用search、match等函數時，如果提供的是用字符串表示的正則表達式，都必須在內部將它們轉換為模式對象。
使用函數compile對正則表達式進行轉換後，每次使用它時都無須再進行轉換。
模式對象也有搜索/匹配方法，因此re.search(pat,string)（其中pat是一個使用字符串表示的正則表達式）等價於pat.search(string)（其中pat是使用compile創建的模式對象）。
編譯後的正則表達式對象也可用於模塊re中的普通函數中。


search：在給定字符串中查找第一個與指定正則表達式匹配的子串
search(pattern,string[,flags])          在給定字符串中查找第一個與指定正則表達式匹配的子串
如果找到這樣的子串，將返回Matchobject（結果為真），否則返回None（結果為假）。
鑑於返回值的這種特徵，可在條件語句中使用這個函數，如下所示：
if re.search(pat,string):
    print('Found it!')
然而，如果你需要獲悉有關匹配的子串的詳細信息，可查看返回的MatchObject。
在Python中，MatchObject是由re.match()或re.search()方法返回的一個對象，用於描述在搜索期間找到的匹配的詳細信息。它包含有關匹配的各種信息，例如匹配的字符串、匹配的位置以及匹配的子字符串。您可以使用MatchObject的方法和屬性來訪問這些信息。
以下是 MatchObject 的一些常用方法和屬性：
group()：返回匹配的子字符串。
start()：返回匹配的子字符串開始的位置。
end()：返回匹配的子字符串結束的位置。
span()：返回匹配的子字符串的開始和結束位置。
您可以使用這些方法和屬性來進一步處理匹配的字符串或提取有用的信息。


match：在給定字符串開頭查找與正則表達式匹配的子串
match(pattern,string[,flags])          在給定字符串開頭查找與正則表達式匹配的子串
函數match在模式與字符串的開頭匹配時，就返回True，而不要求模式與整個字符串匹配。
例如：re.match(’p’,’python’)返回真，而re.match(’p’,’www.python.org’)返回假（None）。
如果要求與整個字符串匹配，需要在模式末尾加上一個美元符號。美元符號要求與字符串末尾匹配，從而將匹配檢查延伸到整個字符串。
在Python中，MatchObject是由re.match()或re.search()方法返回的一個對象，用於描述在搜索期間找到的匹配的詳細信息。它包含有關匹配的各種信息，例如匹配的字符串、匹配的位置以及匹配的子字符串。您可以使用MatchObject的方法和屬性來訪問這些信息。
以下是 MatchObject 的一些常用方法和屬性：
group()：返回匹配的子字符串。
start()：返回匹配的子字符串開始的位置。
end()：返回匹配的子字符串結束的位置。
span()：返回匹配的子字符串的開始和結束位置。
您可以使用這些方法和屬性來進一步處理匹配的字符串或提取有用的信息。


findall：返回一個包含所有與給定模式匹配的子串的列表
findall(pattern, string)          返回一個包含所有與給定模式匹配的子串的列表
返回一個列表，其中包含所有與給定模式匹配的子串。例如，要找出字符串包含的所有單詞，可像下面這樣做：
>>>pat='[a-zA-Z]+'
>>>text='"Hm... Err -- are you sure?"he said,sounding insecure.'
>>>re.findall(pat, text)
['Hm', 'Err', 'are', 'you', 'sure', 'he', 'said', 'sounding', 'insecure']
要查找所有的標點符號，可像下面這樣做：
>>>pat=r'[.?\-",]+'
>>>re.findall(pat, text)
['"', '...', '--', '?"', ',', '.']
請注意，這裡對連字符（-）進行了轉義，因此Python不會認為它是用來指定字符範圍的（如a-z）。


split：根據與模式匹配的子串來分割字符串
split(pattern,string[,maxsplit=0])          根據與模式匹配的子串來分割字符串
類似於字符串方法split，但使用正則表達式來指定分隔符，而不是指定固定的分隔符。例如，使用字符串方法split時，可以字符串‘, ‘為分隔符來分割字符串，但使用re.split時，可以空格和逗號為分隔符來分割字符串。
>>>some_text='alpha, beta,,,,gamma    delta'
>>>re.split('[, ]+',some_text)
['alpha', 'beta', 'gamma', 'delta']
如果模式包含圓括號，將在分割得到的字串之間插入括號中的內容。例如，`re.split(’o(o)’, ’foobar’)`的結果為`[’f’, ’o’, ’bar’]`。
從這個示例可知，返回值為子串列表。參數maxsplit指定最多分割多少次。
>>>re.split('[, ]+', some_text, maxsplit=2)
['alpha', 'beta', 'gamma    delta']
>>>re.split('[, ]+', some_text, maxsplit=1)
['alpha', 'beta,,,,gamma    delta']


sub：從左往右將與模式匹配的子串替換為指定內容
sub(pat, repl, string [,count=0])          從左往右將與模式匹配的子串替換為指定內容
示例：
>>>pat='{name}'
>>>text='Dear {name}...'
>>>re.sub(pat,'Mr.Gumby',text)
'Dear Mr.Gumby...'
替換中的組號和函數（替換字符串時使用組號）：
為了利用re.sub的強大功能，最簡單的方式是在替換字符串中使用組號。
在替換字符串中，任何類似於'\\n'的轉義序列都將被替換為與模式中編組n匹配的字符串。
例如，假設要將'*something*'替換為'<em>somethong</em>'，其中前者是在純文本文檔（如電子郵件）中表示突出的普通方式，而後者是相應的HTML代碼（用於網頁中）。
下面先來創建一個正則表達式。
>>>emphasis_pattern = r'\*([^\*]+)\*'
請注意，正則表達式容易變得難以理解，因此為方便其他人（也包括你自己）以後閱讀代碼，使用有意義的變量名很重要。
創建模式後，就可使用re.sub來完成所需的替換了。
>>>re.sub(emphasis_pattern, r'<em>\1</em>', 'Hello, *world*!')
'Hello, <em>world</em>!'
如你所見，成功地將純文本轉換成了HTML代碼。
然而，通過將函數用作替換內容，可執行更複雜的替換。這個函數將MatchObject作為唯一的參數，它返回的字符串將用作替換內容。換而言之，你可以對匹配的字符串做任何處理，並通過細致的處理來生成替換內容。


匹配對象和編組（group、start、end、span）
在re中，查找與模式匹配的子串的函數都在找到時返回MatchObject對象。這種對象包含與模式匹配的子串的信息，還包含模式的哪部分與子串的哪部分匹配的信息。這些子串部分稱為編組（group）。
編組就是放在圓括號內的子模式，它們是根據左邊的括號數編號的，其中編組0指的是整個模式。因此，在下面的模式中：
'There (was a (wee) (cocper)) who (lived in Fyfe)'
包含如下編組：
0 There was a wee cocper who lived in Fyfe
1 was a wee cocper
2 wee
3 cooper
4 lived in Fyfe
通常，編組包含諸如通配符和重複運算符等特殊字符，因此你可能想知道與給定編組匹配的內容。例如，在下面的模式中：
r’www\.(.+)\.com$’
編組0包含整個字符串，而編組1包含‘www.’和’.com’之間的內容。通過創建類似於這樣的模式，可提取字符串中你感興趣的部分。
下表描述了re匹配對象的一些重要方法。
group([group1,…])       獲取與給定子模式（編組）匹配的子串
start([group])          返回與給定編組匹配的子串的起始位置
end([group])            返回與給定編組匹配的子串的終止位置（與切片一樣，不包含終止位置）
span([group])           返回與給定編組匹配的子串的起始和終止位置
方法group返回與模式中給定編組匹配的子串。如果沒有指定編組號，則默認為0。如果只指定了一個編組號（或使用默認值0），將只返回一個字符串；否則返回一個元組，其中包含與給定編組匹配的子串。
除整個編組（編組0）外，最多還可以有99個編組，編號為1～99。
方法start返回與給定編組（默認為0，即整個模式）匹配的子串的起始索引。
方法end類似於start，但返回終止索引加1
方法span返回一個元組，其中包含與給定編組（默認為0，即整個模式）匹配的子串的起始索引和終止索引。
下面的示例說明了這些方法的工作原理：
>>>m=re.match(r'www\.(.*)\..{3}','www.python.org')
>>>m.group(1)
'python'
>>>m.start(1)
4
>>>m.end(1)
10
>>>m.span(1)
(4, 10)


escape：用於對字符串所有可能被視為正則表達式運算符進行轉義
escape(string) 用於對字符串所有可能被視為正則表達式運算符進行轉義
re.escape是一個工具函數，用於對字符串所有可能被視為正則表達式運算符進行轉義。使用這個函數的情況有：字符串很長，其中包含大量特殊字符，而你不想輸入大量的反斜槓；你從用戶那裡獲取了一個字符串（例如，通過函數input），想將其用於正則表達式中。下面的示例說明了這個函數的工作原理：
>>>re.escape('www.python.org')
'www\\.python\\.org'
>>>re.escape('But where is the ambiguity?')
'But\\ where\\ is\\ the\\ ambiguity\\?'


調用模塊re中的函數時使用re.VERBOSE
要讓正則表達式更容易理解，一種辦法是在調用模塊re中的函數時使用標誌VERBOSE。這讓你能夠在模式中添加空白（空格、制表符、換行符等），而re將忽略它們——除非將它放在字符類中或使用反斜槓對其進行轉義。在這樣的正則表達式中，你還可添加注釋。
下述代碼創建的模式對象與emphasis_pattern等價，但使用了VERBOSE標誌：
emphasis_pattern=re.compile(r'''
\*              #起始突出標誌——一個星號
(               #與要突出的內容匹配的編組的起始位置
[^\*]+          #與除星號外的其他字符都匹配
)               #編組到此結束
\*              #結束突出標誌
''',re.VERBOSE)


re.IGNORECASE
在re模塊中，IGNORECASE是一個標誌（flag），可以在正則表達式的匹配中指示忽略大小寫。