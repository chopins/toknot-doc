类与方法操作
========================

Toknot 框架提供了一组类、方法、函数的访问方法。这些方法主要由 ``Toknot\Boot\Object`` ,  ``Toknot\Boot\ObjectHelper`` , ``Toknot\Boot\MethodHelper`` 提供。但是以上类都无法直接实例化。

主要函数参考
----------------------------------------

Toknot 对于 PHP 的类于方法等语言元素进行了适当的封装和扩展。当类继承了 ``Toknot\Boot\Object`` 抽象类后，会获得以下方法：

.. function:: static callFunc($callable [, $argv = array() ])
    
    :param callable $callable: 可调用函数
    :param array $argv: 传给函数的参数
    :returns: 返回传入的函数运行的返回值
    :rtype: mix
    
    本静态方法是 PHP ``call_user_func_array`` 函数的优化版本，当传入的如果是数组时，实际会调用 ``Object::callMethod()`` 方法

.. function:: static invokeStatic($class, $method [, $argv = array()])

    :param string $class: 静态方法的类名
    :param string $method: 静态方法名
    :param array $argv: 传给静态方法的参数
    :returns: 返回静态方法运行的返回值
    :rtype: mix
    
    调用指定类的静态方法，而没有访问可见性的限制
    
    .. note :: 如果不在类中显示的申明使用  ``Toknot\Boot\ObjectHelper`` 将只能访问 **public** 与 **protected** 方法

.. function:: static callMethod($obj, $method [, $argv = array()])

    :param object $obj: 方法所在对象
    :param string $method: 调用的方法
    :param array $argv: 传给方法的参数
    :returns: 返回方法运行的返回值
    :rtype: mix
    
    调用指定对象的方法，而没有访问可见性的限制
    
    .. note :: 如果不在类中显示的申明使用  ``Toknot\Boot\ObjectHelper`` 将只能访问 **public** 与 **protected** 方法
    

.. function:: static constructArgs($className [, $argv = array()])

    :param string $className: 类名
    :param array $argv: 实例化类时传入的参数
    
    用于实例化对象，而只需要传入一个数组参数。本函数无法突破访问可见性。

.. function:: invokeMethod($method [,$argv = array()])

    :param string $method: 调用的方法
    :param array $argv: 传给方法的参数
    :returns: 返回方法运行的返回值
    :rtype: mix
    
    调用自身对象实例的一个方法，而没有访问可见性的限制。
    
    .. note :: 如果不在类中显示的申明使用  ``Toknot\Boot\ObjectHelper`` 将只能访问 **public** 与 **protected** 方法
    

.. function:: static __class()

    :returns: 方法当前调用类的类名字
    :rtype: string
    
    获得当前类的类名字。与 PHP 5.5 的 ``::class`` 魔术常量类似。
    

获取类方法名
-------------------------------------

继承 ``Toknot\Boot\Object`` 的类有可以直接获取到方法名字符串。见以下例子：

::

    use Toknot\Boot\Object;
    class Foo extends Object {
        public getValue() {
        }
        
        public static getStatic() {
        }
    }
    
    echo Foo::__method()->getValue; // 输出 'getValue'
    echo Foo::__method()->getStatic; //输出 'getStatic'
    
    $obj = new Foo;
    $obj->__callable()->getValue(); // 返回 array($obj,'getValue')

以上方法通过 ``Toknot\Boot\MethodHelper`` 实现， 该类无法被继承与直接实例化

只读类属性
--------------------------------
 
Toknot 通过类属性的注释来实现了只读属性控制。需要类申明时继承了 ``Toknot\Boot\Object`` 时，并且给私有或保护属性添加 **@readonly** 注释，该属性将在类外只能读取，而不能修改其值。例如:

::

    use Toknot\Boot\Object;
    class Foo extends Object {
    
        /**
         * @readonly
         */
        private $pro = 1;
        
        /**
         * @readonly
         */
        protected $pro2 = 'the protected';
    }
    
    $obj = new Foo;
    echo $obj->pro; // 输出 1
    echo $obj->pro2; //输出 'the protected'
    $obj->pro = 1; // 出现PHP错误
    $obj->pro2 = 2; // 出现PHP错误
    
    
只读属性并不会影响 PHP 对象和类的可见性。

.. note :: 子类如果覆盖了 ``Object::__get($name)`` 方法或者未在该方法中调用 ``parent::__get($name)`` 本特性将无效

.. note :: 子类如果实现了 **__set($name, $value)** 方法并且破坏了类方法的访问可见性，本特性无效

.. note :: 注释格式必须符合 PHP 文档注释规则

单列模式
----------------------------------

在 ``Toknot\Boot\Object`` 类中， Toknot 实现了一套单列方法。使用如下方法来获得类的单例：

.. function:: sinlge([$param1 [, $param2 ...])

例子：

::
    
    use Toknot\Boot\Object;
    class Foo extends Object {
    }
    
    $obj = Foo::single();
    
当传入的参数数目或值发生变化后，类实例将会发生变化。如果未传入参数时，将会获返回最近的一个实例，如果没有将会实现一个无参数实例。


迭代器与数组访问
-----------------------------------

``Toknot\Boot\Object`` 类实现了一个替代器，并且也实现了数组访问。迭代数据通过以下方法设置：

.. function:: setIteratorArray([ $data = array()])

``Toknot\Boot\Object`` 其他实现方法
----------------------------------------------

.. function:: paramsHash($param)
    
    :param array $param: 需要获得消息摘要的数组
    :returns:  消息摘要
    :rtype: string
    
    获取一个数组的消息摘要。返回一个长度为40的字符串
    
.. function:: __toString()

    本方法将返回类名与当前实例的hash值组成的字符串，类似 ``Foo(#335dfr4sa2s3fdf)`` ，PHP的特性，当直接输出对象时，本函数会被调用
  
.. function:: __clone()

    本方法会复制迭代数组
    
    

