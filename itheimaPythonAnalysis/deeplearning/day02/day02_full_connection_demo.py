import tensorflow
from tensorflow.examples.tutorials.mnist import input_data

# 手写体数字识别
def full_connection():
    # 1、读取数据
    minst = input_data.read_data_sets("E:/python大数据资料/黑马-03-3天带你玩转Python深度学习/资料/深度学习day2资料/02-代码/mnist_data/",one_hot=True)
    # 用占位符定义真实数据
    x = tensorflow.placeholder(dtype=tensorflow.float32,shape=[None,784])
    y_true = tensorflow.placeholder(dtype=tensorflow.float32,shape=[None,10])
    # 2、构造模型-全连接
    # [None, 784] * W[784, 10] + Bias = [None, 10]
    # 权重
    weight = tensorflow.Variable(initial_value=tensorflow.random_normal(shape=[784,10],stddev=0.01))
    # 偏置
    bias = tensorflow.Variable(initial_value=tensorflow.random_normal(shape=[10],stddev=0.1))
    y_perdict = tensorflow.matmul(x,weight)+bias
    # 3、构造损失函数
    loss_list = tensorflow.nn.softmax_cross_entropy_with_logits(logits=y_perdict,labels=y_true)
    loss = tensorflow.reduce_mean(loss_list)
    # 4、优化损失
    optimizer = tensorflow.train.AdadeltaOptimizer(learning_rate=0.1).minimize(loss)
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
            image,label = minst.train.next_batch(500)
            _,loss_value,accuracy_value = sess.run([optimizer,loss,accurcy],feed_dict={x:image,y_true:label})
            print("第%d次的损失为%f，准确率为%f" % (i + 1, loss_value, accuracy_value))
    return None

if __name__ == "__main__":
    # 手写体数字识别
    full_connection()