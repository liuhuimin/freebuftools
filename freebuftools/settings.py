# -*- coding: utf-8 -*-

# Scrapy settings for freebuftools project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'freebuftools'

SPIDER_MODULES = ['freebuftools.spiders']
NEWSPIDER_MODULE = 'freebuftools.spiders'
ITEM_PIPELINES = {
    'freebuftools.pipelines.FreebuftoolsPipeline': 300,
    }
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'freebuftools (+http://www.yourdomain.com)'
