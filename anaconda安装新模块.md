## anaconda安装新模块

### 1、查看已安装的模块

```
conda list
```

### 2、如果需要安装如 numpy，在命令行中输入

```
anaconda search -t conda numpy
会搜索出numpy的各种版本（windows、linux等）
```

### 3、在命令行中输入，会显示安装命令

```
anaconda show xxxx/xxxxx
```

### 4、通过指定的命令进行按照

```
conda install --channel https://conda.anaconda.org/ukoethe numpy
```

