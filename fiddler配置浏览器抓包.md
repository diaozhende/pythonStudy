### fiddler配置浏览器抓包

#### 1、设置浏览器代理

火狐浏览器：选项-->网络设置-->设置

![](C:\Users\diaozhende\Pictures\Saved Pictures\md图片\火狐配置fiddler.png)

fiddler端口：tools-->option-->connections

![](C:\Users\diaozhende\Pictures\Saved Pictures\md图片\fiddler端口.png)

#### 2、配置fiddler和浏览器对https进行抓包

##### （1）从fiddler中导出证书

tools-->options-->https

![](C:\Users\diaozhende\Pictures\Saved Pictures\md图片\fiddler导出证书1.png)

![](C:\Users\diaozhende\Pictures\Saved Pictures\md图片\fiddler导出证书2.png)

##### （2）将证书导入到浏览器

经过上述步骤，桌面上会有一个FiddlerRoot.cer文件，这个就是证书

火狐浏览器：选项-->隐私和安全-->查看证书-->导入-->选择桌面上导出的证书

![](C:\Users\diaozhende\Pictures\Saved Pictures\md图片\火狐导入证书.png)