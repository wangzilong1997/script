import pandas as pd
import os
def getyourdata():
    #dir = os.getcwd()
    inputdir = input('输入需要的文件夹地址:')
    sdid = input('输入需要的学号:')
    df_empty=pd.DataFrame(columns=['学年','学期','课程代码','课程名称','学号','姓名','任课教师','教学班','学院','年级','专业','班级','选修类型','期末考试时间','期末考试地点'])

    for parents,dirnames,filenames in os.walk(inputdir):
        print(parents)
        print(dirnames)
        print(filenames)
        
        for filename in filenames:
            df=pd.read_excel(os.path.join(parents,filename))
            df_empty=df_empty.append(df,sort=True,ignore_index=True)
    #df_empty.to_excel('C:\\Users\\13217\\Desktop\\选课名单(提前考试+期末考试+课程小测)\\a.xls')


    print(typeof(int(sdid)))
    sid = int(sdid)
    lis = df_empty[(df_empty['学号'] == sid)]
    ylis = lis.index.tolist()
    #print(lis)
    print(ylis)

    #拿出该值 并进行查找即可
    for i in ylis:
        print(df_empty.iloc[[i]])
    #print(df_empty)

    
def typeof(variate):
    type=None
    if isinstance(variate,int):
        type = "int"
    elif isinstance(variate,str):
        type = "str"
    elif isinstance(variate,float):
        type = "float"
    elif isinstance(variate,list):
        type = "list"
    elif isinstance(variate,tuple):
        type = "tuple"
    elif isinstance(variate,dict):
        type = "dict"
    elif isinstance(variate,set):
        type = "set"
    return type

if __name__ == '__main__':
    getyourdata();
