# Copyright (c) 2021 Nippon Telegraph and Telephone corporation (NTT).
# All right reserved
import requests
import unidecode
import json
import time
import tqdm
import unicodedata


# Cleate urls list of tedtalk
def get_requets(url):
    get_url_info = requests.get(url)
    while get_url_info==429:
        print("Zzz...", url)
        time.sleep(10)
        get_url_info = requests.get(url)
    
    if get_url_info.status_code ==200:
        if "Sorry. We couldn't find a talk quite like that." in get_url_info.text:
            return None
        else:
            return get_url_info
    else:
        return None

# Download tedtalk's htmls
def download_tedtalks_list(undata_from=None):        
    page_idx=1
    fp=open("./talklist.json","w")
    talks={}
    
    while True:
        url="https://www.ted.com/talks/quick-list?page="+str(page_idx)
        print(url)
        get_url_info = get_requets(url)
        
        if "Sorry. We couldn't find a talk quite like that." in get_url_info.text or get_url_info.text is None :
            json.dump(talks, fp,indent=2)
            return 0
        elif "Error 429" in get_url_info.text:
            print("Zzz...")
            time.sleep(10)
        else:
            for line in get_url_info.text.split("\n"):
                if '<a href="/talks/' in line:
                    talk_idx=len(talks)
                    talks[talk_idx]={"url":line}
                    #print(talk_idx,"url",line)
                elif '.mp4' in line and 'Medium' in line:
                    #print(talk_idx,"mp4",line)
                    talks[talk_idx]["mp4"]=line
            page_idx+=1
            time.sleep(5)

# Parse htmls and make dataset
def crawle_talks():
    
    def parse(url):
        url=url.replace("<a href=\"","").replace("</a>","") 
        
        return unidecode.unidecode(url).split("\">")
    
    def get_abst(url):
        get_url_info = get_requets("https://www.ted.com"+url)
        if get_url_info is None:
            return 0

        for i in get_url_info.text.split("\n"):
            if i.startswith("<meta name=\"description\" content=\""):
                abst=i.replace("<meta name=\"description\" content=\"","").replace("\"/>","")
                return abst
        return None
        
    def get_transcript(url):
        
        def clean(text):
            text = unicodedata.normalize('NFKC', text)
            text = text.replace("&quot;"," ").replace("&#39;","'").replace("&amp;","&").replace("<p>","").replace("</p>","").replace("\t","").replace("\n","").replace("\r","")
            return text
        
        get_url_info = get_requets("https://www.ted.com"+url+"/transcript")
        
        while get_url_info==429:
            time.sleep(10)
            get_url_info = requests.get("https://www.ted.com"+url)
        
        if get_url_info is None or '<div class="Grid__cell' not in get_url_info.text:
            return None
        
        sent=[]
        lines=get_url_info.text.split("\n")
        idx=0
        start_cell=False
        
        while idx < len(lines):
            j=lines[idx].strip()
            if '<div class="Grid__cell' in j and '<p>' in lines[idx+1].strip(): 
                start_cell=True
            else:
                while start_cell and '</div>' not in j:
                    sent.append(clean(j))
                    idx+=1
                    j=lines[idx].strip()
        
                start_cell=False    
        
            idx+=1
        
        sent=clean(" ".join(sent))
        
        return sent
        
    data=json.load(open("./talklist.json"))
    num=0
    
    for idx in tqdm.tqdm(data.keys(),total=len(data)):
        num+=1
        if num==100:
            break
        try:
            url,title=parse(data[idx]["url"])
            speaker=title.split(": ")[0]
            data[idx]["speaker"]=speaker
            data[idx]["title"]=title.replace(speaker+": ","")
            data[idx]["abst"]=get_abst(url)
            data[idx]["doc"]=get_transcript(url)
    
            if "mp4" in data[idx]:
                data[idx]["key"]=parse(data[idx]["mp4"])[0].split("/")[-1].split(".mp4")[0]
        except:
            pass
    
    json.dump(data, open("./ted_summary.json","w"),indent=2)

if __name__ == "__main__":
    
    download_tedtalks_list()
    crawle_talks()

