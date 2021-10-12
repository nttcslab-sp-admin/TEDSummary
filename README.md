# TEDSummary

#References
[1] Takatomo Kano, Atsunori Ogawa, Marc Delcroix, and Shinji Watanabe "Attention-based Multi-hypothesis Fusion for Speech Summarization," Proc. ASRU, pp. –, 2021
Citation
@inproceedings{attention-fusion,
 author = {Takatomo Kano and Atsunori Ogawa and Marc Delcroix and Shinji Watanabe},
 title = {Attention-based Multi-hypothesis Fusion for Speech Summarization},
 booktitle = {{ASRU 2021 - 2021 IEEE Automatic Speech Recoginition and Understanding Workshop (ASRU)}},
 pages={-}
 year = {2021}
}
#Install tools
Python 3.
requests
unidecode
json
tqdm
unicodedata
#How to run
cd TEDSummary/
python TEDListCrawler.py

#Outputs
telklist.json: URLs list for tedtalks.
ted_summary.json: Summarization dataset. That includes IDs, url, mp4 link, document, abstract, title, speaker name, and a key for Tedlium alignment.
