import scrapy

class FilimoCommentSpider(scrapy.Spider):
    name = 'filimo-comment'
    allowed_domains = ['www.filimo.com']
    start_urls = ['http://www.filimo.com/']

    def parse(self, response):
        for href in response.css('.ds-thumb_content_inner a'):
            yield response.follow(href, self.parse_comment)
        #    print(href) 
    def parse_comment(self ,response):
        for comment in response.css("div.comment-body"):
            comment_content = comment.css('.comment-content::text').get().strip()
            label = 0 if len(comment_content) > 0 else 1
            if(label == 1):
                comment_content = comment.css('.comment-content.is-spoil::text').getall()[1].strip()
            yield {
                'text': comment_content,
                'label': label,
                'link': response.url
            }