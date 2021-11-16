# TEDSummary
TEDSummary is a speech summary corpus. It includes TED talks subtitle (Document), Title-Detail (Summary), speaker name (Meta info), MP4 URL, and utterance id. This script crawls the TEDTalk website to get the above information.  This script does not supply audio data. However, you can use the utterance id to align TED-LIUM3 (https://www.openslr.org/51/) or extract audio from the MP4 file.
# References
[1] Takatomo Kano, Atsunori Ogawa, Marc Delcroix, and Shinji Watanabe "Attention-based Multi-hypothesis Fusion for Speech Summarization," Proc. ASRU, pp. –, 2021
  
  Citation  
  @inproceedings{attention-fusion,  
  author = {Takatomo Kano and Atsunori Ogawa and Marc Delcroix and Shinji Watanabe},  
  title = {Attention-based Multi-hypothesis Fusion for Speech Summarization},  
  booktitle = {{ASRU 2021 - 2021 IEEE Automatic Speech Recoginition and Understanding Workshop (ASRU)}},  
  pages={-},  
  year = {2021}  
  }
# Install tools
Python 3.
requests
unidecode
json
tqdm
unicodedata
# How to run
cd TEDSummary/
python TEDListCrawler.py

# Outputs
  telklist.json: URLs list for tedtalks.  
  ted_summary.json: Summarization dataset. That includes summary IDs, TEDTalk URL, mp4 URL, document, abstract, title, speaker name, and uttrance id for Tedlium alignment.
