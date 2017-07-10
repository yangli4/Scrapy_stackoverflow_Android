#  爬取 Stackoverflow 1m 条问答

作为一个热爱编程的大学生，怎么能不知道面向 stackoverflow 编程呢。

打开 stackoverflow 主页，在 questions 页面下选择按 vote 排序，爬取前 20000 页，每页将问题数量设置为 50，共 1m 条，（实际上本来是想爬完 13m 条的，但 1m 条后面问题基本上都只有 1 个或 0 个回答，那就选取前 1m 就好吧）  
 
实际上用数据库去重后只有 999654 条问答信息 

# 对爬取数据进行简单分析  
## votes 分析
### 降序排列了 votes 数，生成折线图  

![Votes折线图](https://github.com/chenjiandongx/stackoverflow/blob/master/images/votes_0.png)  
2k 后的问题的 votes 数基本上就已经在 400 以下了，接着后面的就基本上是贴地飞行了  
votes 数最多 : [Why is it faster to process a sorted array than an unsorted array?](http://stackoverflow.com/questions/11227809/why-is-it-faster-to-process-a-sorted-array-than-an-unsorted-array)

### votes 数的连续分布情况  

![votes甘特图](https://github.com/chenjiandongx/stackoverflow/blob/master/images/votes_1.png)  
可见最多的还是集中在 1-2K 之间,从 6k 开始基本上就断层了  

### 具体数据  

| description  | count |
| -----------  | ----- |
| votes >= 500 | 1630  |
| votes >= 400 | 2325  |
| votes >= 300 | 3782  |
| votes >= 200 | 7062  |
| votes >= 100 | 19781 |  

如果以 100 为分界线的话，会得到这样的一个饼图  

![pie_votes_1](https://github.com/chenjiandongx/stackoverflow/blob/master/images/pie_votes_1.png)  
大于 100 的连 %2 都不到  

再来看看底层的数据  

| description | count   |
| ----------- | -----   |
| 1 <= votes <= 5    | 211804  |
| 6 <= votes <= 10   | 430935  |
| 11 <= votes <= 15  | 136647  |
| 16 <= votes <= 20  | 64541   |
| votes <= 20        | 843927  |  

可见 votes 小于 20 的，数量高达 84m  
看看总体的比例吧  
![pie_votes_2](https://github.com/chenjiandongx/stackoverflow/blob/master/images/pie_votes_2.png)  


## answers 分析
### 降序排列了 answers 数，生成折线图  
  
![answers折线图](https://github.com/chenjiandongx/stackoverflow/blob/master/images/answers_0.png)  
很明显 3k 之后的 answers 数基本上就小于 20 了  
answers 数最多: [What is the best comment in source code you have ever encountered? [closed]](http://stackoverflow.com/questions/184618/what-is-the-best-comment-in-source-code-you-have-ever-encountered)  

### answers 数的连续分布情况  

![answers甘特图](https://github.com/chenjiandongx/stackoverflow/blob/master/images/answers_1.png)  
150 后也就断层了，实际上能达到这样的回答数极少  

### 具体数据  
  
| description   | count |
| -----------   | ----- |
| answers >= 5   | 218059 |
| answers >= 10  | 34500  |
| answers >= 20  | 3808   |
| answers >= 30  | 968    |  

大于 30 的确实少的可怜，看看总体情况  
![pie_answer_1](https://github.com/chenjiandongx/stackoverflow/blob/master/images/pie_answer_1.png)  


## views 分析
### 降序排列了 views 数，生成折线图  

![views折线图](https://github.com/chenjiandongx/stackoverflow/blob/master/images/views_0.png)  
最高达到了 4.5m，100000 以后的基本上就不足 28000 了  
views 数最多: [How to undo last commit(s) in Git?](http://stackoverflow.com/questions/927358/how-to-undo-last-commits-in-git)


### views 数的连续分布情况  

![views甘特图](https://github.com/chenjiandongx/stackoverflow/blob/master/images/views_1.png)

### 具体数据  

| description   | count |
| -----------   | ----- |
| views >= 5000    | 486466  |
| views >= 10000   | 315576  |
| views >= 20000   | 171873  |
| views >= 50000   | 59363   | 
| views >= 100000  | 22224   | 
| views >= 200000  | 7030    |  

大部分问答的 views 数还是集中在 20000 以内  
还是得看看总体分布  
![bubble_views](https://github.com/chenjiandongx/stackoverflow/blob/master/images/bubble_views.png)

## 再看看 votes，views，answers 三者的散点图对应情况  
### votes - views  

![votes-views散点图](https://github.com/chenjiandongx/stackoverflow/blob/master/images/views_votes.png)  
### votes - answers  

![votes-answers散点图](https://github.com/chenjiandongx/stackoverflow/blob/master/images/answers_votes.png)
### views - answers  

![views-answers散点图](https://github.com/chenjiandongx/stackoverflow/blob/master/images/view_answers.png)  


总的来说，这三者对应关系类似于一个金字塔。三个图基本上都是左下角靠近原点的区域被填满，也就是说绝对大部分的问题的 votes，answers 和 views 都是属于最下层的。高质量活跃的问题是处于金字塔顶端的。三者的最高数好像也没特别明显的对应关系，且三者的最高数都不是同一个问题。


根据所有问题的 tags 提取出总量前 200 的关键词（前 50 条如下），第 1 名是 c#，python 排在第 5

```python
('c#', 94614),
('java', 93244),
('javascript', 76722),
('android', 69321),
('python', 62502),
('c++', 58173),
('php', 42596),
('ios', 37773),
('jquery', 37405),
('.net', 36180),
('html', 28536),
('css', 26174),
('c', 24699),
('objective-c', 23253),
('iphone', 22171),
('ruby-on-rails', 20143),
('sql', 19171),
('asp.net', 18060),
('mysql', 17559),
('ruby', 16397),
('r', 15670),
('git', 13139),
('linux', 13080),
('asp.net-mvc', 12857),
('angularjs', 12606),
('sql-server', 12473),
('node.js', 12212),
('django', 11576),
('arrays', 11006),
('algorithm', 10959),
('wpf', 10631),
('performance', 10619),
('xcode', 10613),
('string', 10426),
('windows', 10132),
('eclipse', 10117),
('scala', 9942),
('regex', 9685),
('multithreading', 9601),
('json', 9266),
('swift', 8950),
('c++11', 8939),
('haskell', 8823),
('osx', 8159),
('visual-studio', 8140),
('html5', 7627),
('database', 7567),
('xml', 7478),
('spring', 7464),
('unit-testing', 7253),
('bash', 6825)
```

### 这样看好像不太直观，所以就把它根据词频生成了词云  

![词云](https://github.com/chenjiandongx/stackoverflow/blob/master/images/word_cloud.jpg)


## 因为是用 Python 写的爬虫，所以重点来分析下 Python 类的问答
### votes 数前 10
* 6162 : [What does the “yield” keyword do in Python?](http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python)
* 3529 : [What is a metaclass in Python?](http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python)
* 3098 : [How do I check whether a file exists using Python?](http://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-using-python)
* 3035 : [Does Python have a ternary conditional operator?](http://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator)
* 2620 : [Calling an external command in Python](http://stackoverflow.com/questions/89228/calling-an-external-command-in-python)
* 2605 : [What does if __name__ == “__main__”: do?](http://stackoverflow.com/questions/419163/what-does-if-name-main-do)
* 2194 : [How to merge two Python dictionaries in a single expression?](http://stackoverflow.com/questions/38987/how-to-merge-two-python-dictionaries-in-a-single-expression)
* 2123 : [Sort a Python dictionary by value](http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value)
* 2058 : [How to make a chain of function decorators?](http://stackoverflow.com/questions/739654/how-to-make-a-chain-of-function-decorators)
* 1984 : [How to check if a directory exists and create it if necessary?](http://stackoverflow.com/questions/273192/how-to-check-if-a-directory-exists-and-create-it-if-necessary)


### answers 数前 10
* 191 : [Hidden features of Python [closed]](http://stackoverflow.com/questions/101268/hidden-features-of-python)
* 87 : [Best ways to teach a beginner to program? [closed]](http://stackoverflow.com/questions/3088/best-ways-to-teach-a-beginner-to-program)
* 55 : [Favorite Django Tips & Features?](http://stackoverflow.com/questions/550632/favorite-django-tips-features)
* 50 : [How do you split a list into evenly sized chunks?](http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks)
* 44 : [Calling an external command in Python](http://stackoverflow.com/questions/89228/calling-an-external-command-in-python)
* 43 : [How can I represent an 'Enum' in Python?](http://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python)
* 38 : [How to merge two Python dictionaries in a single expressions](http://stackoverflow.com/questions/38987/how-to-merge-two-python-dictionaries-in-a-single-expression)
* 38 : [Finding local IP addresses using Python's stdlib](http://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib)
* 37 : [Reverse a string in python without using reversed or [::-1]](http://stackoverflow.com/questions/18686860/reverse-a-string-in-python-without-using-reversed-or-1)
* 37 : [How do I check whether a file exists using Python?](http://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-using-python)


### views 数前 10
* 2121621 : [Parse String to Float or Int](http://stackoverflow.com/questions/379906/parse-string-to-float-or-int)
* 1905938 : [Using global variables in a function other than the one that created them](http://stackoverflow.com/questions/423379/using-global-variables-in-a-function-other-than-the-one-that-created-them)
* 1888666 : [How do I check whether a file exists using Python?](http://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-using-python)
* 1827126 : [Calling an external command in Python](http://stackoverflow.com/questions/89228/calling-an-external-command-in-python)
* 1699574 : [Converting integer to string in Python?](http://stackoverflow.com/questions/961632/converting-integer-to-string-in-python)
* 1686230 : [How do I read a file line-by-line into a list?](http://stackoverflow.com/questions/3277503/how-do-i-read-a-file-line-by-line-into-a-list)
* 1682307 : [Iterating over dictionaries using 'for' loops in Python](http://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops-in-python)
* 1569205 : [How to get the size of a list](http://stackoverflow.com/questions/1712227/how-to-get-the-size-of-a-list)
* 1554755 : [How do I install pip on Windows?](http://stackoverflow.com/questions/4750806/how-do-i-install-pip-on-windows)
* 1515505 : [Finding the index of an item given a list containing it in Python](http://stackoverflow.com/questions/176918/finding-the-index-of-an-item-given-a-list-containing-it-in-python)  

### 三者的前十中有两个问题是完全重叠的，分别是
* [How do I check whether a file exists using Python?](http://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-using-python)
* [Calling an external command in Python](http://stackoverflow.com/questions/89228/calling-an-external-command-in-python)


### 欢迎 Fork 和 Star