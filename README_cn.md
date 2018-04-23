
# 转换 python 的 dict/list/nested 类型数据（含互相嵌套）到 PHP 能识别的 HTTP 参数（urlencoded）


## 安装

```sh
pip install to_php_post_arr
```


## 使用


```py
from to_php_post_arr.convert import recursive_urlencode

a = [1, 2]
print(recursive_urlencode(a))
# 输出：0=1&1=2


a2 = (1, '2')
print(recursive_urlencode(a2))
# 输出：0=1&1=2


b = {'a': 11, 'b': 'foo'}
print(recursive_urlencode(b))
# 输出：a=11&b=foo


c = {'a': 11, 'b': [1, 2]}
print(recursive_urlencode(c))
# 输出：a=11&b[0]=1&b[1]=2


d = [1, {'a': 11, 'b': 22}]
print(recursive_urlencode(d))
# 输出：0=1&1[a]=11&1[b]=22


e = {'a': 11, 'b': [1, {'c': 123}, [3, 'foo']]}
print(recursive_urlencode(e))
# 输出：a=11&b[0]=1&b[1][c]=123&b[2][0]=3&b[2][1]=foo

f = ['测试中文']
print(recursive_urlencode(f))
# test chinese 
# 输出：0=%E6%B5%8B%E8%AF%95%E4%B8%AD%E6%96%87

```

## PHP 的 urlencoded 数组数据
- http://php.net/manual/en/faq.html.php#faq.html.arrays



## 测试
```sh
cd tests

python -m unittest test_convert
```



## 感谢 
- 代码参考: https://stackoverflow.com/a/4014164/2752670
