#encoding=utf-8
import scrapy
from freebuftools.items import FreebuftoolsItem
class FreeBufToolsSpider(scrapy.Spider):
    name = "freeBufTools"
    allowed_domains =["freebuf.com"]#域名
    start_urls =["http://www.freebuf.com/geek"]#初始页面，可更改为相应分类首页
    def parse(self,response):
        file=open("freebufgeek.html",'a')#写入爬取内容的文件，注意文件为追加模式

        for sel in response.xpath("//div[@class='news_inner news-list']/div[@class='news-info']/dl/dt/a"):#xpath路径父节点
            tools=FreebuftoolsItem()#新建保存item
            tools['title']=sel.xpath("text()").extract()[0].encode('utf-8')#提取文章题目并转换格式保存
            tools['link']=sel.xpath("@href").extract()[0].encode('utf-8')#提取文章链接并转换格式保存
            html='''<p><a href="'''+tools['link']+'''" target="_black">'''+tools['title']+"</a></p>"#拼接写入文件的html代码
            file.writelines(html)#将爬取内容写入文件
            yield tools#返回爬取内容
        url=response.xpath("//div[@id='pagination']/a/@href").extract()[0]#获取下一页的链接
        yield scrapy.Request(url,callback=self.parse)#回调本函数继续爬取下一页