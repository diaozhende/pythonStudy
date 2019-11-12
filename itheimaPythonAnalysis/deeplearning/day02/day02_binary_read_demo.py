import tensorflow
import os

# TODO:读取二进制文件
class binary(object):
    def __init__(self):
        # 设置图像大小
        self.width = 32
        self.height = 32
        self.channel = 3
        # 设置图像的字节数
        self.image = self.height * self.width * self.channel
        self.label = 1
        self.sample = self.image + self.label

    # TODO:读取二进制文件方法
    def read_binary(self,file_path):
        # 1、构建文件名队列
        file_quece = tensorflow.train.string_input_producer(file_path)
        print("file_quece:\n",file_quece)
        # 2、读取和解码
        # 读取
        reader = tensorflow.FixedLengthRecordReader(self.sample)
        key,value = reader.read(file_quece)
        print("key:\n",key)
        print("value:\n",value)
        # 解码
        image_decode = tensorflow.decode_raw(value,tensorflow.uint8)
        print("image_decode:\n",image_decode)
        # 切片操作，将标签和图片分开
        label = tensorflow.slice(image_decode,[0],[1])
        image = tensorflow.slice(image_decode,[self.label],[self.image])
        print("label:\n",label)
        print("image:\n",image)

        # 调整图片的形状
        image_reshape = tensorflow.reshape(image,[self.channel,self.height,self.width])
        print("image_reshape:\n",image_reshape)

        # 对图片进行转置，转成批处理需要的格式
        # [1,2,0]：表示原数据下表为1的放到0位置，2放到1位置，0放到2位置
        image_transpose = tensorflow.transpose(image_reshape,[1,2,0])
        print("image_transpose:\n",image_transpose)
        # 3、批处理
        image_batch,label_batch = tensorflow.train.batch([image_transpose,label],batch_size=100,num_threads=1,capacity=100)

        # 开启会话
        with tensorflow.Session() as sess:
            # 构建线程协调员
            coord = tensorflow.train.Coordinator()
            threads = tensorflow.train.start_queue_runners(sess=sess,coord=coord)
            key, value, image_decode, label, image, image_reshape, image_transpose, image_batch,label_batch = sess.run([key,value,image_decode,label,image,image_reshape,image_transpose,image_batch,label_batch])
            print("key:\n",key)
            print("value:\n",value)
            print("image_decode:\n",image_decode)
            print("label:\n",label)
            print("image:\n",image)
            print("image_reshape:\n",image_reshape)
            print("image_transpose:\n",image_transpose)
            print("image_batch:\n",image_batch)
            # 关闭回收线程
            coord.request_stop()
            coord.join(threads)
        return image_batch,label_batch

    # TODO：将读取的图片数据写入到TFRecords文件
    def write_TFRecords(self,image_value,label_value):
        with tensorflow.python_io.TFRecordWriter("./TFRecords/cifar10.tfrecords") as writer:
            # 循环构造example对象，并序列化写入文件
            for i in range(100):
                image = image_value[i].tostring()
                label = label_value[i][0]
                example = tensorflow.train.Example(features=tensorflow.train.Features(feature={
                    "image":tensorflow.train.Feature(bytes_list=tensorflow.train.BytesList(value=[image])),
                    "label":tensorflow.train.Feature(int64_list=tensorflow.train.Int64List(value=[label]))
                }))
                # 将序列化后的example写入文件
                writer.write(example.SerializeToString())
        return None

    # TODO:读取TFRecords文件
    def read_TFRecords_demo(self):
        # 1、构建文件名队列
        file_queue = tensorflow.train.string_input_producer(["./TFRecords/cifar10.tfrecords"])
        # 2、读取和解码
        # 读取
        reader = tensorflow.TFRecordReader()
        key,value = reader.read(file_queue)

        # 解析example
        feature = tensorflow.parse_single_example(value,features={
            "image":tensorflow.FixedLenFeature([],tensorflow.string),
            "label":tensorflow.FixedLenFeature([],tensorflow.int64)
        })
        image_feature_value = feature["image"]
        label_feature_value = feature["label"]
        # 解码
        image_decode = tensorflow.decode_raw(image_feature_value,tensorflow.uint8)
        # 图像形状调整
        image_reshape = tensorflow.reshape(image_decode,[self.height,self.width,self.channel])

        # 3、批处理
        image_batch,label_batch = tensorflow.train.batch([image_reshape,label_feature_value],batch_size=100,num_threads=1,capacity=100)
        # 开启会话
        with tensorflow.Session() as sess:
            coord = tensorflow.train.Coordinator()
            # 开启线程
            threads = tensorflow.train.start_queue_runners(sess=sess,coord=coord)
            image_batch,label_batch = sess.run([image_batch,label_batch])
            print("label_batch:\n",label_batch)
            print("image_batch:\n",image_batch)
            # 终止线程
            coord.request_stop()
            # 回收线程
            coord.join(threads=threads)
if __name__ == "__main__":
    # 获取路径下所有的文件
    file_list = os.listdir("E:/python大数据资料/黑马-03-3天带你玩转Python深度学习/资料/深度学习day2资料/02-代码/cifar-10-batches-bin")
    # 将文件名和路径进行拼接，并把bin文件筛选出来
    path = "E:/python大数据资料/黑马-03-3天带你玩转Python深度学习/资料/深度学习day2资料/02-代码/cifar-10-batches-bin/"
    file_path = [os.path.join(path,fileName) for fileName in file_list if fileName[-3:] == "bin"]
    obj = binary()
    # image_batch, label = obj.read_binary(file_path)
    # obj.write_TFRecords(image_batch, label)
    obj.read_TFRecords_demo()