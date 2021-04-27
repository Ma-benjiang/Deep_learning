#!usr/bin/python3
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import jieba
from sklearn.preprocessing import MinMaxScaler


def dictivec():
    #初始化一个对象
    dict=DictVectorizer(sparse=False)#sparse为True为稀疏矩阵的坐标，稀疏矩阵可以节省内存
    data=dict.fit_transform([{'city': '北京', 'temperature': 100},
                               {'city': '上海', 'temperature': 60},
                               {'city': '深圳', 'temperature': 30}])
    print(data)
    print(type(data))
    print(dict.get_feature_names())
    print(dict.inverse_transform(data))

def couvec():
    #实例化一个对象
    vector=CountVectorizer(min_df=1)
    #转换数据
    ret=vector.fit_transform(["life  is short,i like python", "life too long,i dislike python"])
    print(ret)
    print(vector.get_feature_names())
    print(ret.toarray())

def cutword():
    con1 = jieba.cut("今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。")

    con2 = jieba.cut("我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。")

    con3 = jieba.cut("如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。")
    print(con1)
    # 转换成列表
    print(type(con1))
    print('-' * 50)
    content1 = list(con1)
    content2 = list(con2)
    content3 = list(con3)
    print(content1)
    # 把列表转换成字符串
    print('-' * 50)
    c1 = ' '.join(content1)
    print(c1)
    c2 = ' '.join(content2)
    c3 = ' '.join(content3)

    return c1, c2, c3
def hanzivec():
    """
    中文特征值化
    :return: None
    """
    c1, c2, c3 = cutword()

    print(c1, c2, c3)

    cv = CountVectorizer()

    data = cv.fit_transform([c1, c2, c3])

    print(cv.get_feature_names())

    print(data.toarray())

    return None
def tfidfvec():
    """
    中文特征值化,倒排索引
    :return: None
    """
    c1, c2, c3 = cutword()

    print(c1, c2, c3)

    tf = TfidfVectorizer()

    data = tf.fit_transform([c1, c2, c3])

    print(tf.get_feature_names())

    print(data.toarray())

    return None
def mm():
    """
    归一化处理
    :return: NOne
    """
    # 归一化容易受极值的影响
    mm = MinMaxScaler(feature_range=(0, 1))

    data = mm.fit_transform([[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]])

    print(data)

    return None
if __name__ == '__main__':
    # dictivec()
    cutword()
   # hanzivec()
   # tfidfvec()
   #  mm()
