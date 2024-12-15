

# integer

```rs
let v: u16 = 38_u8 as u16;
```

38_u8 可以直接literal表示用 u8 格式， 

as u16 类型转换

两个方法其实很类似


# for loop range 

1..2
1..=2

```rs

    for i in -3..-2 {
        sum += i;
    }

    // 不包含 -2 

    assert_eq!(sum, -3);

    for c in 'a'..='z' {
        println!("{}",c as u8);
    }

    // 包含 'z'
```



# Diverging functions

```rs

// Solve it in two ways
// DON'T let `println!` works
fn main() {
    never_return();

    println!("Failed!");
}

fn never_return_fn() -> ! {
    panic!();
    unimplemented!();
    todo!();
}

```

感叹号类型  = Diverging functions

# for loop - enumerate

```rs

for (i, &item) in bytes.iter().enumerate() {}

```

这个item 实际上是 bytes 里面具体的值

这个和 ref 有点像是对称的操作? （就是）

```rs

    let c = '中';

    let r1 = &c;
    let ref r2 = c;

```


其实这并不是enumerate 的特殊用法
```rs

let k = something_referance;

let &real = k;

// equal to 

let real  = *k;

```


但是注意上面这个逻辑是无法直接编译的


something_reference 假设是 ref to something

那其实 let real = *something_reference  就是 。let real = something 

你是实际上在尝试 move out something，但是，something 现在被 somethin_reference 借走了，

无法执行 move 操作
