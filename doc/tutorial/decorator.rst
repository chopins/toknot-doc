装饰器
========================

装饰器操作由 ``Toknot\Boot\Decorator`` 提供。支持函数于类方法装饰。

.. function:: Kernel::decorator($func [, $isClass = false])

    :param string|array $func: 函数名，类名，或者包含类名与方法的数组
    :param boolean $isClass: 是否是类名，为 **true** 是，字符串才会被当成类名

.. class:: Toknot.Boot.Decorator($func [, $isClass = false])

    可直接实例化获得装饰器

::

    use Toknot\Boot\Kernel;

    function dec1($r) {
        echo $r;
        echo 'this dec1';
        return 2;
    }
    
    function dec2($r) {
        echo $r;
        echo 'this dec2'
        return function() {
            echo 'return function';
        }
    }
    
    /**
     * @decorator dec2
     * @decorator dec1
     */
    function call() {
        echo 'this call';
        return 1;
    }
    
    $dec = Kernel::single()->decorator('call');
    /*
     上面代码会依次输出：
     this call
     1
     this dec1
     2
     this dec2
    */
    $dec(); // 输出 return function
 
 Toknot 是使用 PHP 代码注释实现的装饰器，所以对于代码注释，必须符合规范。
 
 装饰器支持函数与类静态方法。可对函数，类方法，类进行装饰。
 
 如果装饰器是静态类方法，注释值应当是用 **::** 分割类名和方法名

