import tensorflow
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
# 1、TensorFlow基本结构
def tensorflow_demo():
    # 使用tensorFlow实现加法运算
    a = tensorflow.constant(2)
    b = tensorflow.constant(3)
    c = a + b
    print("c的值为：",c)

    # 开启会话
    with tensorflow.Session() as sess:
        c_value = sess.run(c)
        print("c_value:",c_value)
    return None

# 2、图的演示
def graph_demo():
    a = tensorflow.constant(2)
    b = tensorflow.constant(3)
    c = a + b
    # 查看默认图
    # 方法一：调用方法
    defult_g = tensorflow.get_default_graph()
    print("查看默认图：",defult_g)
    print("c的值为：", c)
    # 方法二：查看属性
    print("a的属性",a.graph)
    # 开启会话
    with tensorflow.Session() as sess:
        c_value = sess.run(c)
        print("c_value:", c_value)

    # 自定义图
    new_g = tensorflow.Graph()
    with new_g.as_default():
        a_new = tensorflow.constant(20)
        b_new = tensorflow.constant(30)
        c_new = tensorflow.add(a_new,b_new)
        print("c_new的属性值",c_new)

    # 开启会话
    with tensorflow.Session(graph=new_g) as new_sess:
        # 查看属性值，必须在session中调用eval()方法进行查看
        print("c_new的值：",c_new.eval())
        c_new_value = new_sess.run((c_new))
        print("c_new_value:",c_new_value)
    return None

# 3、图的可视化
def graph_look_demo():
    a = tensorflow.constant(2)
    b = tensorflow.constant(3)
    c = a + b
    # 查看默认图
    # 方法一：调用方法
    defult_g = tensorflow.get_default_graph()
    print("查看默认图：", defult_g)
    print("c的值为：", c)
    # 方法二：查看属性
    print("a的属性", a.graph)
    # 开启会话
    with tensorflow.Session() as sess:
        c_value = sess.run(c)
        print("c_value:", c_value)
        # 将图写入到本地生成events文件
        tensorflow.summary.FileWriter("./tmp/summay",graph=sess.graph)
        # 然后在终端中启动TensorBoard
        # 命令：tensorboard --logdir="./tmp/summay/"
        # 在浏览器中输入127.0.0.1::6006
    return None

# 4、张量的演示
def tensor_demo():
    # 定义张量:默认的类型为float32
    tensor1 = tensorflow.constant(3)
    tensor2 = tensorflow.constant([1,2,3,4])
    tensor3 = tensorflow.constant([[1],[2],[3],[4]],dtype=tensorflow.int64)
    print("tensor1:",tensor1)
    print("tensor2:",tensor2)
    print("tensor3:",tensor3)
    # 修改张量的类型
    tensor1_cast = tensorflow.cast(tensor1,dtype=tensorflow.int64)
    print("tensor1_cast:",tensor1_cast)
    # 更新/改变静态形状
    # 定义占位符
    # 没有完全固定下来的静态形状
    a_p = tensorflow.placeholder(dtype=tensorflow.float32,shape=[None,None])
    b_p = tensorflow.placeholder(dtype=tensorflow.float32,shape=[None,10])
    c_p = tensorflow.placeholder(dtype=tensorflow.float32,shape=[3,2])
    print("a_p",a_p)
    print("b_p",b_p)
    print("c_p",c_p)
    # 更新形状未确定的部分
    a_p.set_shape([2,3])
    b_p.set_shape([2,10])
    print("a_p",a_p)
    print("b_p",b_p)
    # 动态修改形状
    a_p_reshape = tensorflow.reshape(a_p,shape=[2,3,1])
    print("a_p_reshape",a_p_reshape)
    return None
# 5、张量类型的修改
def type_demo():
    tensor1 = tensorflow.constant(1)
    tensor1_cast = tensorflow.cast(tensor1,tensorflow.int64)
    print(tensor1)
    print(tensor1_cast)
    return None
# 6、张量形状的修改
def shape_demo():
    # 修改静态形状
    # 修改静态形状只能在形状么未确定的情况下才能修改
    a = tensorflow.placeholder(dtype=tensorflow.float32,shape=[None,None])
    b = tensorflow.placeholder(dtype=tensorflow.float32,shape=[None,3])
    c = tensorflow.placeholder(dtype=tensorflow.float32,shape=[3,3])
    print("a:",a)
    print("b:",b)
    print("c:",c)
    #修改张量的形状只能修改未确定的部分，不能跨维度
    a.set_shape([2,3])
    b.set_shape([5,3])
    print("a:", a)
    print("b:", b)

    # 动态修改形状,原始值不发生改变，返回一个新的张量
    # 动态修改形要元素数量保持一致(2*3=2*3*1)
    a_reshape = tensorflow.reshape(a,shape=[2,3,1])
    print("a_reshape:",a_reshape)
    return None
# 7、变量OP
def variable_demo():
    # 创建变量
    a = tensorflow.Variable(initial_value=50)
    b = tensorflow.Variable(initial_value=60)
    c = tensorflow.add(a,b)
    # 变量初始化,如果不初始化在开启会话的时候会报错
    init = tensorflow.global_variables_initializer()
    with tensorflow.Session() as sess:
        # 运行初始化
        sess.run(init)
        a_value,b_value,c_value = sess.run([a,b,c])
        print("a_value:",a_value)
        print("b_value:",b_value)
        print("c_value:",c_value)
    return None

# 8、用tensorFlow实现线性回归
def linear_regression_demo():
    # 1、准备数据
    x = tensorflow.random_normal(shape=[100,1])
    y = tensorflow.matmul(x,[[0.8]])+0.7
    # 2、构建模型
    # 用变量的形式定义模型参数
    weights = tensorflow.Variable(initial_value=tensorflow.random_normal(shape=[1,1]),name="Weights")
    bias = tensorflow.Variable(initial_value=tensorflow.random_normal(shape=[1,1]),name="Bias")
    y_perdict = tensorflow.matmul(x,weights)+bias
    # 3、构建损失函数
    error = tensorflow.reduce_mean(tensorflow.square(y_perdict - y))
    # 4、优化损失函数
    optimizer = tensorflow.train.GradientDescentOptimizer(learning_rate=0.01).minimize(error)

    # 2_收集变量
    tensorflow.summary.scalar("error",error)# 折线图
    tensorflow.summary.histogram("weights",weights)# 直方图
    tensorflow.summary.histogram("bias",bias)
    # 3_合并变量
    merge = tensorflow.summary.merge_all()
    # 1*创建saver对象
    saver = tensorflow.train.Saver()
    # 初始化变量
    init = tensorflow.global_variables_initializer()
    # 开启会话
    with tensorflow.Session() as sess:
        sess.run(init)
        # 1_创建事件文件
        file_writer = tensorflow.summary.FileWriter("./tmp/linear",graph=sess.graph)
        print("训练前模型参数为：权重%f，偏置%f，损失为%f" % (weights.eval(), bias.eval(), error.eval()))
        # for i in range(1000):
        #     sess.run(optimizer)
        #     print("第%d次训练模型参数为：权重%f，偏置%f，损失为%f" % (i,weights.eval(), bias.eval(), error.eval()))
        #     # 5_运行合并变量操作
        #     summary = sess.run(merge)
        #     # 4_将每次迭代后的变量写入到事件文件
        #     file_writer.add_summary(summary,i)
        #     # 2*保存模型
        #     if i % 10 == 0:
        #         saver.save(sess,"./tmp/model/my_linear.ckpt")

        #加载模型
        if os.path.exists("./tmp/model/checkpoint"):
            saver.restore(sess,"./tmp/model/my_linear.ckpt")
        print("训练后模型参数为：权重%f，偏置%f，损失为%f" % (weights.eval(), bias.eval(), error.eval()))
    return None

# 9、命令行参数
def command_demo():
    # 1.定义命令行参数
    tensorflow.app.flags.DEFINE_integer("max_step",100,"训练模型的步数")
    tensorflow.app.flags.DEFINE_string("model_dir","None","文件路径")
    # 2.简化变量名
    FLAGS = tensorflow.app.flags.FLAGS
    print("max_step:",FLAGS.max_step)
    print("model_dir:",FLAGS.model_dir)
    return None
if __name__ == "__main__":
    # 代码1：TensorFlow基本结构
    # tensorflow_demo()
    # 代码2：图的演示
    # graph_demo()
    # 代码3：图的可视化
    # graph_look_demo()
    # 代码4：张量的演示
    # tensor_demo()
    # 代码5：张量类型的修改
    # type_demo()
    # 代码6:张量形状的修改
    shape_demo()
    # 代码7：变量OP
    # variable_demo()
    # 代码8：用tensorFlow实现线性回归
    # linear_regression_demo()
    # 代码9：命令行参数
    command_demo()