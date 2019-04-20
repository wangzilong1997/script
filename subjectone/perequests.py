import requests
import time
from lxml import etree

def getsubejectonetimu():
    page = 0
    getpage = requests.get(url='http://km1.jsyst.cn/fx/index.asp?page='+ str(page+1))
    # getpage.encoding = 'gb2312'
    selectorpage = etree.HTML(getpage.text)
    titlespage = selectorpage.xpath('//*[@id="side"]/div[2]/div[2]/ul/li')
    maxpage = len(titlespage)
    print(maxpage)
    for page in range(0,maxpage):
        get = requests.get(url='http://km1.jsyst.cn/fx/index.asp?page='+ str(page+1))
        get.encoding = 'gb2312'
        selector = etree.HTML(get.text)
        titles = selector.xpath('//*[@class="vehiclesIn2"]/p/a/text()')
        # print(selector)
        # print(get.text)
        print(titles)
        txtName = 'subjectonetimu.txt'
        lens = len(titles)
        print(lens)
        f = open(txtName,"a+",encoding='utf-8')
        for i in range(1,lens):
            new_subjectone = titles[i]+'\n'
            f.write(new_subjectone)
        f.close()
        page = page + 1
        time.sleep(2)

def getsubject():
    page = 0
    for i in range(0,1073):
        get = requests.get(url='http://km1.jsyst.cn/fx/q' + str(page + 1))
        get.encoding = 'gb2312'
        selector = etree.HTML(get.text)
        title = selector.xpath('//*[@id="side"]/div[3]/div/div/h1/text()')
        answers = selector.xpath('//*[@id="side"]/div[3]/div/div/p/text()')
        answer = selector.xpath('//*[@id="side"]/div[3]/div/div/p[last()-2]/font/b/text()')
        print(title)
        print(answers)
        print(answer)
        txtName = 'subjectone.txt'
        f = open(txtName,"a+",encoding='utf-8')
        new_titles = str(title) + '\n'
        new_answers = str(answers) + '\n'
        new_answer = str(answer) + '\n'
        f.write(new_titles)
        f.write(new_answers)
        f.write(new_answer)
        f.close()
        page = page + 1
        time.sleep(1)





def main():
    # getsubejectonetimu()
    getsubject()

if __name__ == '__main__':
    main()


