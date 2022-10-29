# Blog-Documents

https://blog.51cto.com/oldboy 

## Beautiful Soup的简介与安装
`Beautiful Soup`是一个可以从HTML或XML文件中提取数据的Python库.它能够通过你喜欢的转换器实现惯用的文档导航,查找,修改文档的功能.`Beautiful Soup`会帮你节省数小时甚至数天的工作时间.#

## Beautiful Soup 安装
`Beautiful Soup 3`目前已经停止开发，推荐在现在的项目中使用`Beautiful Soup 4`，不过它已经被移植到BS4了，也就是说导入时我们需要 `import bs4`。所以这里我们用的版本是`Beautiful Soup 4.4.0(简称BS4)`，另外据说BS4对Python3的支持不够好，不过我用的是Python2.7.7，如果有小伙伴用的是Python3版本，可以考虑下载BS3版本。

我们可以使用`pip`或`easy_install`来安装`Beautiful Soup`库：
```shell
easy_install beautifulsoup4
```

```shell
ip install beautifulsoup4
# 在Python3中安装
pi3 install beautifulsoup4
```

## 安装Lxml与html5lib
Beautiful Soup支持Python标准库中的HTML解析器,还支持一些第三方的解析器,其中一个是lxml.根据操作系统不同,可以选择下列方法来安装lxml:
```shell
apt-get install Python-lxml
easy_install lxml
pip install lxml
# python3版本
pip3 install lxml
```
另一个可供选择的解析器是纯Python实现的html5lib, html5lib的解析方式与浏览器相同,可以选择下列方法来安装html5lib:
```shell
apt-get install Python-html5lib
easy_install html5lib
pip install html5lib
pip3 install html5lib
`````

|  解析器   | 使用方法  | 优势  |劣势  |
|  ----  | ----  |  ----  | ----  |
| Python标准库  | BeautifulSoup(markup, "html.parser") | 1、Python的内置标准库 2、执行速度适中 3、文档容错能力强  | 1、Python 2.7.3 or 3.2.2)前 的版本中文档容错能力差 |
| lxml HTML 解析器 | BeautifulSoup(markup, "lxml") | 1、速度快 2、文档容错能力强  | 1、需要安装C语言库 |
| lxml XML 解析器  | BeautifulSoup(markup, ["lxml", "xml"]) BeautifulSoup(markup, "xml") | 1、速度快 2、唯一支持XML的解析器  | 1、需要安装C语言库 |
| html5lib | BeautifulSoup(markup, "html5lib") | 1、最好的容错性 2、以浏览器的方式解析文档 3、生成HTML5格式的文档  | 1、速度慢 2、不依赖外部扩展 |

推荐使用lxml作为解析器,因为效率更高. 在Python2.7.3之前的版本和Python3中3.2.2之前的版本,必须安装lxml或html5lib, 因为那些Python版本的标准库中内置的HTML解析方法不够稳定。


## 开始使用Beautiful Soup

由于Beautiful Soup文档的内容比较多，我们只整理一些常用的用法，更多可以参考Beautiful Soup官方文档

### 创建Beautiful Soup对象
使用BeautifulSoup前需要引入bs4库，我们仅需要将一段文档传入BeautifulSoup的构造器,就能得到一个文档的对象，；同时我们也可以传入一段字符串或者一个文件。

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("index.html"))

soup = BeautifulSoup("<html>data</html>")
```
首先,文档被转换成Unicode,并且HTML的实例都被转换成Unicode编码
``` python
soup = BeautifulSoup("spider test")
print(soup)
# <html><body><p>spider test</p></body></html>
```
然后,Beautiful Soup会选择最合适的解析器来解析这段文档,如果手动指定解析器那么Beautiful Soup会选择指定的解析器来解析文档。

### 四大对象种类
Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:

- Tag
- name
- attrs
一个tag可能有很多个属性，你可以使用如下两种方法获取。
```python
tag['class']

tag.attrs
- ```


