# Machine-learning 
## 学习特征工程
### 1.字典特征抽取
sklearn.feature_extraction.DictVectorizer
* 实例化类DicVectorizer
* 调用fit_transform方法输入数据并转换
### 2.文本特征抽取
sklearn.feature_extraction.text.CountVectorizer
#### 英文文本特征值化
* 实例化类CountVectorizer
* 调用fit_transform方法输入数据并转换
#### 中文文本特征值化
* jieba分词
* 实例化类CountVectorizer
* 调用fit_transform方法输入数据并转换
### 3.TF-IDF
* API：sklearn.feature_extraction.text.TfidfVectorizer
* 概念：https://zhuanlan.zhihu.com/p/31197209
### 4.数据的特征处理
#### 归一化
* 概念：（x-min(x))/(max(x)-min(x))
* sklearn归一化API:  sklearn.preprocessing.MinMaxScaler
#### 标准化
* sklearn特征化API:  scikit-learn.preprocessing.StandardScaler

