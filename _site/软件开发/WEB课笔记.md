# MongoDb

启用服务
```sh
sudo systemctl start mongod
sudo systemctl stop mongod
```


# ES6

####

```js

Symbol()
# 唯一标识

WeakMap()
# 涉及到一些内存自动清除

Map()
# 

Set()

```

## JS  类 构造函数

原型空间

```js
Person.prototype.hobby = function(){
	//xxxx
}

```

```js

Person.prototype.constructor === Person;
// true

let zhangshan = new Person('xxx');
zhangsan.constructor === Person;
// true

```

保证同类不同的实例可以共享空间


\_\_proto\_\_ 和 prototype, 类Person 才有 prototype,
let alan = new Person('alan');
alan没有 prototype,但是有 \_\_proto\_\_




## Call Bind Apply

都是可以改变函数里的 this 的方法

```js

function foo (name){

    console.log(this, name)
}

let obj = {'s': 'a'}
foo.call(obj, 'a')
foo.apply(obj, ['a'])
foo.bind(obj)('a') 

// {'s':'a'} 'a'
```

## 继承

有了上面这几个函数,现在我们可以定义继承关系:

```js

function Dad(name, age){
    this.name = name
    this.age = age
    this.money = 10000
}

function Son(name, age, xxx){
    Dad.call(this,name,age)
}

let s = new Son('alan', 20)
s.money == 10000
```
一般对方法的继承,会用 原型 ,prototype


```js

class Son extends Dad{
 
    constructor(name){
	super(name);
    }
}

```

## 抽象类
class AbstractPerson{

	constructor(){
		if(new.target === AbstractPerson){
			throw new Error("抽象类不能直接被实例化");
		}
	
	}
}


## 私有属性

\# 号修饰符
```js

function Person(name){

	let _weight = 130
}

class person{
    #weight = 130
    constructor(name){
	this.name = name
    }

    getWeight(){
	return this.#weight
    }
}

```

## 静态成员

```js

function Person(name){
    this.name = name;
}
Person.num = 10;

console.log(zhanghsan.num) // undefined


// ES6
class Person{

	constructor(name){
		this.name = name
	}

	static num = 10;
	static fn(){
		console.log('fn')
	}
}

```

可以应用在,只能实例化一次


```js
class Person{

	static instance
	constructor(name){
		if (! Person.instance){
			Person.instance = this
		} else {
			return Person.instance
		}
		this.name = name
	}

}

```


# import

```js
import('./a.js').then( res => {});

```
这是个异步的import, promise








## 设计模式


### 设计模式原则

- 单一原则： 一个类 模块 只有一个职责, 颗粒度尽量低。

- 开闭原则： 尽量少的更改功能, 向上兼容 (对扩展开放, 对修改关闭)

- 里氏替换原则： 子类可以替换父类

- 迪米特法则： 最小知识法则, 不用和陌生人讲话, 组建通信, 不建议跨级别通信

- 借口隔离原则： 多个特定的客户端好于一个通用型的接口

- 依赖倒置原则

### 设计模式

三个大类, 创建型, 结构型, 行为型


单例模式：

一个类只有一个实例,  window, 


``` js

class Person{
	static instance;

	constructor(name) {
		if( !Person.instance) {
			Person.instance = this;
		} else{

			return Person.instance;
		}
		this.name = name;

	}

	}

}

// 也是一个单例
let obj1 = {
	name: "alan"
}


// 通用单例
function createInstance(creator){
	let instance;
	return function(...args){
		if (!instance){
			instance = new creator(...args);
		}
		return instance
	}
}
// 很奇妙的每次调用这个函数都会创建一个新的instance？

// no,  这个知识相当于是一个新的creator, 我们new 它的时候, 就会保留一个instance

let newCreator = new createInstance(Person)

let alan = new newInstance("alan");
let blan = new newInstance("blan");

console.log(blan) // is alan

```


### 工厂模式

### 装饰器模式

类似 extends

```js
class Yase{
	construcro(){
		this.name = "yase";
	}
	release(){
		console.log("释放技能");
	}

}

let yase = new Yase();
yase.release();

function attack(){
	console.log("attck ");
}

Function.prototype.Decorator = function (fn){
	this();
	fn();
}


yase.release.Decorator(attack)();



```

### 观察者模式

有点像 event listener
```js

document.querSelector(".box").addEventListener("click", function(){
});



let obj = {
	fn1(){
	console.log("fn1");

	}
}

let obj2 = {
	fn2(){
	console.log("fn2");

	}
}


class MyEvent{
	constructor(){
		this.handles = {}
	}

	addEvent(eventName, fn){
		if(typeof this.handles[evnetName] === "undefined"){
			this.handles[eventName] = [];
		}
		this.hanldes[eventName].push(fn);
	}

	trigger(eventName){

		if(!(eventName in this.handles)){
		return 
		} 
		this.handles[eventName].forEach(fn =>{fn();});
	}
}


let eventObj = new MyEvent();

eventObj.addEvent("myevent", obj1.fn1);
eventObj.addEvent("myevent", obj2.fn2);


```



### 代理模式



```js

let zhangsan = {
	sellHouse(num){
		console.log("卖了" + num + "万元");
	}
}

let proxySeller = {
	sellHouse(hasSold, num){
		if(hasSold){
			zhangsan.sellHouse(num-2);
		} else {
			zhangsan.sellHouse(num);
		}
}

proxySeller.sellHouse(true,100);



// 加载等待照片
function proxyImg(src){
	let myImg = new CreateImage();
	let loadzimg = new Image();
	loadImg.src = src;
	loadImg.onload = function (){
		myImg.setsrc(src);
	}
}
proxyImg('www.xxxxxxx');

```


### 适配器


```js


```


### mixin 混入模式


<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
