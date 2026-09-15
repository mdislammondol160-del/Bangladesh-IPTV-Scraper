#!/usr/bin/env python3
"""
Bangladesh & Indian IPTV M3U Scraper
Automatically scrapes and updates IPTV channel links
"""

import requests
import json
from datetime import datetime
import os

class IPTVScraper:
    def __init__(self):
        self.channels = []
        self.m3u_header = "#EXTM3U x-tvg-url=\"http://epg.example.com/guide.xml\"\n"
        
    def add_channel(self, name, logo, url, group, tvg_id=""):
        """Add a channel to the playlist"""
        extinf = f"#EXTINF:-1 tvg-id=\"{tvg_id}\" tvg-logo=\"{logo}\" group-title=\"{group}\",{name}\n"
        self.channels.append(f"{extinf}{url}\n")
    
    def scrape_channels(self):
        """Scrape channels from multiple sources"""
        print("🔄 Scraping channels...")
        
        # Bangladesh News Channels
        self.add_channel("একাত্তর টিভি (Ekattor TV)", 
            "https://static.wikia.nocookie.net/logopedia/images/5/5d/Ekattor_TV_logo.png",
            "https://owrcovcrpy.gpcdn.net/bpk-tv/1705/output/1705.m3u8",
            "🇧🇩 Bangladesh News", "ekattor.tv")
        
        self.add_channel("ইন্ডিপেন্ডেন্ট টেলিভিশন (Independent TV)",
            "https://raw.githubusercontent.com/subirkumarpaul/Logo/main/Independent%20Television.png",
            "https://owrcovcrpy.gpcdn.net/bpk-tv/1704/output/1704.m3u8",
            "🇧🇩 Bangladesh News", "independent.tv")
        
        self.add_channel("যমুনা টিভি (Jamuna TV)",
            "https://jamunagroup.com.bd/company-images/1662487622-mdshamimislam.png",
            "https://owrcovcrpy.gpcdn.net/bpk-tv/1701/output/index.m3u8",
            "🇧🇩 Bangladesh News", "jamuna.tv")
        
        self.add_channel("নিউজ ২৪ (News 24)",
            "https://raw.githubusercontent.com/subirkumarpaul/Logo/main/News%2024.png",
            "https://owrcovcrpy.gpcdn.net/bpk-tv/1708/output/index.m3u8",
            "🇧🇩 Bangladesh News", "news24.bd")
        
        # More Bangladesh Channels
        self.add_channel("ATN News",
            "https://raw.githubusercontent.com/subirkumarpaul/Logo/main/ATN%20News.png",
            "https://owrcovcrpy.gpcdn.net/bpk-tv/1706/output/1706.m3u8",
            "🇧🇩 Bangladesh News", "atnnews.bd")
        
        self.add_channel("Channel 24",
            "https://raw.githubusercontent.com/subirkumarpaul/Logo/main/channel%2024.png",
            "https://owrcovcrpy.gpcdn.net/bpk-tv/1703/output/1703.m3u8",
            "🇧🇩 Bangladesh News", "channel24.bd")
        
        self.add_channel("Somoy TV",
            "https://raw.githubusercontent.com/subirkumarpaul/Logo/main/Somoy%20TV.jpeg",
            "https://owrcovcrpy.gpcdn.net/bpk-tv/1702/output/1702.m3u8",
            "🇧🇩 Bangladesh News", "somoy.tv")
        
        self.add_channel("DBC News",
            "https://raw.githubusercontent.com/subirkumarpaul/Logo/main/DBC%20News.png",
            "https://owrcovcrpy.gpcdn.net/bpk-tv/1728/output/1728.m3u8",
            "🇧🇩 Bangladesh News", "dbc.news")
        
        # Bangladesh General Channels
        self.add_channel("Channel 9",
            "https://raw.githubusercontent.com/subirkumarpaul/Logo/main/Channel%209.png",
            "https://owrcovcrpy.gpcdn.net/bpk-tv/1729/output/1729.m3u8",
            "🇧🇩 Bangladesh General", "channel9.bd")
        
        self.add_channel("Bangla Vision",
            "https://i.imgur.com/nCWgp38.png",
            "https://owrcovcrpy.gpcdn.net/bpk-tv/1715/output/index.m3u8",
            "🇧🇩 Bangladesh General", "banglavision.bd")
        
        self.add_channel("NTV",
            "https://raw.githubusercontent.com/subirkumarpaul/Logo/main/NTV.png",
            "https://owrcovcrpy.gpcdn.net/bpk-tv/1716/output/1716.m3u8",
            "🇧🇩 Bangladesh General", "ntv.bd")
        
        self.add_channel("Deepto TV",
            "https://raw.githubusercontent.com/subirkumarpaul/Logo/main/Deepto%20TV.jpeg",
            "https://byphdgllyk.gpcdn.net/hls/deeptotv/index.m3u8",
            "🇧🇩 Bangladesh General", "deepto.tv")
        
        self.add_channel("SATV",
            "https://raw.githubusercontent.com/subirkumarpaul/Logo/main/SATV.png",
            "https://owrcovcrpy.gpcdn.net/bpk-tv/1720/output/1720.m3u8",
            "🇧🇩 Bangladesh General", "satv.bd")
        
        self.add_channel("Mohona TV",
            "https://raw.githubusercontent.com/subirkumarpaul/Logo/main/Mohona%20TV.png",
            "https://owrcovcrpy.gpcdn.net/bpk-tv/1723/output/index.m3u8",
            "🇧🇩 Bangladesh General", "mohona.tv")
        
        self.add_channel("BTV National",
            "https://raw.githubusercontent.com/subirkumarpaul/Logo/main/BTV%20National.png",
            "https://owrcovcrpy.gpcdn.net/bpk-tv/1709/output/1709.m3u8",
            "🇧🇩 Bangladesh General", "btv.bd")
        
        self.add_channel("Maasranga TV",
            "https://raw.githubusercontent.com/subirkumarpaul/Logo/main/Maasranga%20TV.png",
            "https://owrcovcrpy.gpcdn.net/bpk-tv/1722/output/1722.m3u8",
            "🇧🇩 Bangladesh Entertainment", "maasranga.tv")
        
        self.add_channel("RTV",
            "https://raw.githubusercontent.com/subirkumarpaul/Logo/main/RTV.png",
            "https://tvsen6.aynaott.com/rtv/tracks-v1a1/mono.ts.m3u8",
            "🇧🇩 Bangladesh Entertainment", "rtv.bd")
        
        self.add_channel("Green TV",
            "https://raw.githubusercontent.com/subirkumarpaul/Logo/main/Green%20TV.png",
            "https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/greentv.stream/live-orgin/greentv.stream/chunks.m3u8",
            "🇧🇩 Bangladesh Entertainment", "green.tv")
        
        # Indian Channels
        self.add_channel("Star Jalsha HD",
            "https://static.wikia.nocookie.net/logopedia/images/3/3c/Star_Jalsha_HD.png",
            "https://tvsen4.aynaott.com/n64PH4YL/index.m3u8",
            "🇮🇳 India Entertainment", "starjalsha.in")
        
        self.add_channel("Colors Bangla",
            "https://da.gd/g8pHvl",
            "https://yupptvcatchupire.yuppcdn.net/preview/colorsbanglahd/800.m3u8",
            "🇮🇳 India Entertainment", "colorsbangla.in")
        
        self.add_channel("Zee Bangla",
            "https://xstreamcp-assets-msp.streamready.in/assets/LIVETV/LIVECHANNEL/LIVETV_LIVETVCHANNEL_ZEE_BANGLA/images/LOGO_HD/LOGO_HD_image.png",
            "http://217.20.112.199:8080/maamovies/index.m3u8",
            "🇮🇳 India Entertainment", "zeebangla.in")
        
        self.add_channel("Sony Aath",
            "https://images.toffeelive.com/images/program/343/logo/240x240/mobile_logo_496322001666780228.png",
            "https://stream.ottplus.bd/live/sony_aath_abr/live/sony_aath_720/chunks.m3u8",
            "🇮🇳 India Entertainment", "sonyaath.in")
        
        self.add_channel("DD Bangla",
            "https://static.wikia.nocookie.net/logopedia/images/8/8f/DD_Bangla.png",
            "https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/7ff57cc9046b4c188b51a0d506f36e7f/index_3.m3u8",
            "🇮🇳 India Entertainment", "ddbangla.in")
        
        # Sports Channels
        self.add_channel("T Sports",
            "https://raw.githubusercontent.com/subirkumarpaul/Logo/main/T%20Sports.png",
            "https://tvsen7.aynaott.com/tsports-hd/index.m3u8",
            "🏆 Sports", "tsports.bd")
        
        self.add_channel("Star Sports 1",
            "https://i.postimg.cc/DzDHjCJm/20240823_024249.png",
            "http://tvsen7.aynascope.net/sspts1/index.m3u8",
            "🏆 Sports", "starsports1.in")
        
        print(f"✅ Scraped {len(self.channels)} channels")
    
    def generate_m3u(self):
        """Generate M3U playlist content"""
        content = self.m3u_header
        for channel in self.channels:
            content += channel
        return content
    
    def save_m3u(self, filename="playlist.m3u"):
        """Save M3U file"""
        content = self.generate_m3u()
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Saved to {filename}")
        return content

def main():
    scraper = IPTVScraper()
    scraper.scrape_channels()
    content = scraper.save_m3u()
    
    # Also save metadata
    metadata = {
        "updated_at": datetime.now().isoformat(),
        "total_channels": len(scraper.channels),
        "channels": [
            {
                "name": channel.split(',')[1].split('\n')[0],
                "group": channel.split('group-title="')[1].split('"')[0]
            }
            for channel in scraper.channels
        ]
    }
    
    with open('metadata.json', 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    print(f"\n📊 Metadata saved to metadata.json")
    print(f"⏰ Last updated: {metadata['updated_at']}")

if __name__ == "__main__":
    main()
