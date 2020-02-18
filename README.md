### 过滤器

### 提交记录
```
1、提交:demo


```



### 知识点
```
    https://github.com/spareribs/learning/tree/master/Django/Django_up

    class_02
    可以通过过滤器来修改变量的显示，过滤器的形式是：{{ variable | filter }}，管道符号'|'代表使用过滤器
    过滤器能够采用链式的方式使用，例如：{{ text | escape | linebreaks }}
    过滤器还可以带参数，例如： {{ bio|truncatewords:30 }}
    过滤器的参数中如果带有空格，那么需要用引号引起来，例如：{{ list | join : ", "}}
    django中有30多个内置过滤器 比如add，cut，date等。
```