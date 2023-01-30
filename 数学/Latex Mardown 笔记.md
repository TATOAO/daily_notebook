# Latex #

### Bold text
有好多方法都能让字体变粗体，大家自己感受一下：
1.   \\(\mathbf{q}\\) \mathbf 这个不支持geek character 
2.   \\(\boldsymbol{q}\\) \boldsymbol
3.   \\(\pmb{q}\\) \pmb
4.   \\(q\\) 这是正常形态

横向对比更明显
\\( \mathbf{q}, \boldsymbol{q}, \pmb{q}, q\\)

# Markdown #

我现在渐渐理解Markdown的精髓了，它就是一个过渡文本和HTML的强大工具，可能不是过渡，是容纳/包括。

### 直接调用 JS！ - Graph 

!!! 这个功能不能直接使用，我记得我当年确实是能用起来的，现在可能是因为浏览器协议变了，或者我当时使用的是其他的markdown interpreter，总之现在是没办法直接在markdown里面调用js script. 

[visjs 这个是个非常好的网站，Js + visualization, 这次用的是它的Network](https://visjs.org/ ":)")

直接把下面这一段复制到markdown里，就可以生成下面的Network啦！

``` js
<script type="text/javascript" src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>

<style type="text/css">
#mynetwork {
    width: 600px;
    height: 400px;
    border: 1px solid lightgray;
}
</style>
<div id="mynetwork"></div>

<script type="text/javascript">
    // create an array with nodes
    var nodes = new vis.DataSet([
        {id: 1, label: 'Node 1'},
        {id: 2, label: 'Node 2'},
        {id: 3, label: 'Node 3'},
        {id: 4, label: 'Node 4'},
        {id: 5, label: 'Node 5'}
    ]);

    // create an array with edges
    var edges = new vis.DataSet([
        {from: 1, to: 3},
        {from: 1, to: 2},
        {from: 2, to: 4},
        {from: 2, to: 5}
    ]);

    // create a network
    var container = document.getElementById('mynetwork');

    // provide the data in the vis format
    var data = {
        nodes: nodes,
        edges: edges
    };
    var options = {};

    // initialize your network!
    var network = new vis.Network(container, data, options);
</script>
```

it is not working ? 

<script type="text/javascript" src="http://localhost:8340/aaa">

</script>

fwf

<script type="text/javascript" src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js">



console.log('xxxxxwefwofjweofj');
</script>

<style type="text/css">

#mynetwork {
    width: 600px;
    height: 400px;
    border: 1px solid lightgray;
}
</style>

<div id="mynetwork">
jiwfe
</div>


<
jwiefj
jweijfowjef

<script type="text/javascript">

    alert('wwww');
    // create an array with nodes
    var nodes = new vis.DataSet([
        {id: 1, label: 'Node 1'},
        {id: 2, label: 'Node 2'},
        {id: 3, label: 'Node 3'},
        {id: 4, label: 'Node 4'},
        {id: 5, label: 'Node 5'}
    ]);

    // create an array with edges
    var edges = new vis.DataSet([
        {from: 1, to: 3},
        {from: 1, to: 2},
        {from: 2, to: 4},
        {from: 2, to: 5}
    ]);

    // create a network
    var container = document.getElementById('mynetwork');

    // provide the data in the vis format
    var data = {
        nodes: nodes,
        edges: edges
    };
    var options = {};

    // initialize your network!
    var network = new vis.Network(container, data, options);

	console.log("xxxxxx");

    // container.innerText = "aaaaaaaaaaaa"
</script>


 

[d3js 有待挖掘](https://d3js.org/ ":)")


### Mini map navigator 

