import pandas

def user_id_alise_id():
    # 1、读取数据
    aisles = pandas.read_csv("E:/python大数据资料/黑马-02-最简单快速入门python机器学习/资料/机器学习day1资料/02-代码/instacart/aisles.csv")
    order_products = pandas.read_csv(
        "E:/python大数据资料/黑马-02-最简单快速入门python机器学习/资料/机器学习day1资料/02-代码/instacart/order_products__prior.csv")
    orders = pandas.read_csv("E:/python大数据资料/黑马-02-最简单快速入门python机器学习/资料/机器学习day1资料/02-代码/instacart/orders.csv")
    products = pandas.read_csv("E:/python大数据资料/黑马-02-最简单快速入门python机器学习/资料/机器学习day1资料/02-代码/instacart/products.csv")
    # 2、合并表，将user_id和aisle_id合并到一起
    # 2.1、将orders表和order_products__prior进行合并
    order_order_product_data = pandas.merge(orders, order_products,on=["order_id", "order_id"])
    # 2.2、将order_order_product_data表和products表进行合并
    product_order_product_data = pandas.merge(order_order_product_data, products,on=["product_id", "product_id"])
    # 2.3、将product_order_product_data表和aisles表进行合并
    user_id_aisle_id_data = pandas.merge(product_order_product_data, aisles,on=["aisle_id", "aisle_id"])
    print(user_id_aisle_id_data)


if __name__ == '__main__':
    user_id_alise_id()