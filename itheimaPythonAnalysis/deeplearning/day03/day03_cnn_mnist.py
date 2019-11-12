import tensorflow
from tensorflow.examples.tutorials.mnist import input_data
# 利用卷积神经网络实现手写体数字识别
def create_weigth(shape):
    return tensorflow.Variable(tensorflow.random_normal(shape=shape))
# 构建卷积神经网络
def create_model(x):
    # 1、第一个卷积大层
    # 将[None,784]的形状进行修改
    input_x = tensorflow.reshape(x,shape=[-1,28,28,1])
    # 定义filter(权重)和偏置
    conv1_weigths = create_weigth([5,5,1,32])
    conv1_bais = create_weigth([32])
    conv1_x = tensorflow.nn.conv2d(input=input_x,filter=conv1_weigths,strides=[1,1,1,1],padding="SAME")

    # 激活层
    conv1_relu = tensorflow.nn.relu(conv1_x)
    # 池化层
    conv1_pool = tensorflow.nn.max_pool(value=conv1_relu,ksize=[1,2,2,1],strides=[1,2,2,1],padding="SAME")

    # 2、第二个卷积大层
    # 定义fliter和偏置
    conv2_weigths = create_weigth([5,5,32,64])
    conv2_bais = create_weigth([64])
    conv2_x = tensorflow.nn.conv2d(input=conv1_pool,filter=conv2_weigths,strides=[1,1,1,1],padding="SAME") + conv2_bais
    # 激活层
    conv2_relu = tensorflow.nn.relu(conv2_x)
    # 池化层
    conv2_pool = tensorflow.nn.max_pool(value=conv2_relu,ksize=[1,2,2,1],strides=[1,2,2,1],padding="SAME")

    # 3、全连接层
    x_fc = tensorflow.reshape(conv2_pool,shape=[-1,7*7*64])
    fc_weigths = create_weigth(shape=[7*7*64,10])
    fc_bais = create_weigth(shape=[10])
    y_perdict = tensorflow.matmul(x_fc,fc_weigths)+fc_bais
    return y_perdict
def cnn_mnist():
    # 1、读取数据
    mnist_data = input_data.read_data_sets("E:/python大数据资料/黑马-03-3天带你玩转Python深度学习/资料/深度学习day2资料/02-代码/mnist_data/",one_hot=True)
    # 用占位符的方式定义特征值和目标值
    x = tensorflow.placeholder(dtype=tensorflow.float32,shape = [None,784])
    y_true = tensorflow.placeholder(dtype=tensorflow.float32,shape=[None,10])
    y_perdict = create_model(x)
    # 3、构建损失函数
    lost_list = tensorflow.nn.softmax_cross_entropy_with_logits(labels=y_true,logits=y_perdict)
    lost = tensorflow.reduce_mean(lost_list)
    # 4、优化损失
    # learning_rate:学习率
    optimizer = tensorflow.train.AdamOptimizer(learning_rate=0.01).minimize(lost)
    # 5、计算准确率
    bool_list = tensorflow.equal(tensorflow.argmax(y_true,axis=1),tensorflow.argmax(y_perdict,axis=1))
    accurcy = tensorflow.reduce_mean(tensorflow.cast(bool_list,tensorflow.float32))

    # 初始化变量
    init = tensorflow.global_variables_initializer()
    # 开启会话
    with tensorflow.Session() as sess:
        sess.run(init)
        # 开始训练
        for i in range(5000):
            image,label = mnist_data.train.next_batch(50)
            sess.run(optimizer,feed_dict={x:image,y_true:label})
            print("第%d次的损失为%f，准确率为%f" % (i + 1, sess.run(lost,feed_dict={x:image,y_true:label}), sess.run(accurcy,feed_dict={x:image,y_true:label})))
    return None

if __name__ == "__main__":
    cnn_mnist()