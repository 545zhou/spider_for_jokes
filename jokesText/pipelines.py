# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JokestextPipeline(object):
  def __init__(self):
  	self.file = open('jokestext.dat', 'ab')



  def process_item(self, item, spider):
	  val = "{0}\n".format(item['content'])
	  self.file.write(val)
	  return item
