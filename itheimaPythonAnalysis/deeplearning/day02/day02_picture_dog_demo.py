import tensorflow
import os
# 读取狗的图片
def picture_dog_demo(flie_list):
    # 1、创建文件名队列
    file_quece = tensorflow.train.string_input_producer(flie_list)

    # 2、读取和解码
    # 读取
    reader = tensorflow.WholeFileReader()
    key,value = reader.read(file_quece)
    print("key:\n",key)
    print("value:\n",value)
    # 解码,如果是png图片用decode_png()方法
    image_decode = tensorflow.image.decode_jpeg(value)
    print("image_decode:\n",image_decode)
    # 将图片缩放到同一大小
    image_resize = tensorflow.image.resize_images(image_decode,[200,200])
    print("image_resize:\n",image_resize)
    # 更新静态形状，将所有形状确定才能进行下边的批处理
    image_resize.set_shape([200,200,3])
    print("image_resize_after:\n",image_resize)
    # 3、批处理队列
    # 1:读取特征，2：文件数量，3：线程数，4：容量
    image_batch = tensorflow.train.batch([image_resize],batch_size=100,num_threads=1,capacity=100)
    print("image_patch:\n",image_batch)

    # 开启会话
    with tensorflow.Session() as sess:
        # 构建线程协调器
        coord = tensorflow.train.Coordinator()
        # 开启线程
        threads = tensorflow.train.start_queue_runners(sess=sess,coord=coord)
        key, value, image_decode, image_resize, image_batch = sess.run([key,value,image_decode,image_resize,image_batch])
        print("key:\n",key)
        print("value:\n",value)
        print("image_decode:\n",image_decode)
        print("image_resize:\n",image_resize)
        print("image_batch:\n",image_batch)
        # 终止线程
        coord.request_stop()
        coord.join(threads)
    return None

if __name__ == "__main__":
    # 获取路径下所有的文件
    picture_list = os.listdir("E:/python大数据资料/黑马-03-3天带你玩转Python深度学习/资料/深度学习day2资料/02-代码/dog")
    # 对文件名进行拼接
    file_path = "E:/python大数据资料/黑马-03-3天带你玩转Python深度学习/资料/深度学习day2资料/02-代码/dog/"
    flie_list = [os.path.join(file_path,file) for file in picture_list]
    # 读取狗的图片
    picture_dog_demo(flie_list)