It's a spider to using scrapy to scrape jokes from online. 

Right now the spide can only crawl joke texts from qiushibaidke.com

To start the spider, type in terminal:
	scrapy crawl joke

The scraped data will be stored in jokestext.dat	

To auto run scrapy, Autorun.sh has been built to accomplish such a goal. 
To load the Autorun.sh to launchctl, do the follwing:
	1, chmod 777 Autorun.sh
	2, create com.scrapy.launchctl.plist in directory /Users/tao/Libray/LaunchAgents. 
		The interval has been set to 2 days.
	3, in terminal type in: launchctl load com.scrapy.launchctl.plist 
Once the mission has been changed, it's needed to reload the mission to launchctl.
In terminal:
	1, type: launchctl unload com.scrapy.launchctl.plist to unload mission
	2, type: launchctl load com.scrapy.launchctl.plist  to reload mission
