from datetime import date, timedelta
from pathlib import Path
import re

def pasqua(anno):
    a=anno%19; b=anno//100; c=anno%100; d=b//4; e=b%4
    f=(b+8)//25; g=(b-f+1)//3; h=(19*a+b-d-g+15)%30
    i=c//4; k=c%4; l=(32+2*e+2*i-h-k)%7; m=(a+11*h+22*l)//451
    n=h+l-7*m+114
    return date(anno,n//31,n%31+1)

def fold(line):
    chunks=[];part="";size=0
    for char in line:
        count=len(char.encode("utf-8"))
        if size+count>75:chunks.append(part);part=" ";size=1
        part+=char;size+=count
    return "\r\n".join(chunks+[part])

base=Path(__file__).parent
text=(base/"festivita_italia_2026_originale.ics").read_text(encoding="utf-8-sig")
blocks=re.findall(r"BEGIN:VEVENT\n(.*?)\nEND:VEVENT",text,re.S)
lines=["BEGIN:VCALENDAR","VERSION:2.0","PRODID:-//Jazia//Festivita italiane//IT","CALSCALE:GREGORIAN","METHOD:PUBLISH","X-WR-CALNAME:Festività italiane","X-WR-TIMEZONE:Europe/Rome","X-WR-CALDESC:Festività nazionali italiane 2026-2030. Testi in italiano."]
for year in range(2026,2031):
    for block in blocks:
        props=dict(line.split(":",1) for line in block.splitlines())
        uid=props["UID"].replace("-2026@",f"-{year}@")
        if uid.startswith("pasqua-"):start=pasqua(year)
        elif uid.startswith("pasquetta-"):start=pasqua(year)+timedelta(days=1)
        else:start=date(year,int(props["DTSTART;VALUE=DATE"][4:6]),int(props["DTSTART;VALUE=DATE"][6:8]))
        lines += ["BEGIN:VEVENT","UID:"+uid,"DTSTAMP:20261004T000000Z","DTSTART;VALUE=DATE:"+start.strftime("%Y%m%d"),"DTEND;VALUE=DATE:"+(start+timedelta(days=1)).strftime("%Y%m%d"),"SUMMARY;LANGUAGE=it:"+props["SUMMARY"],"DESCRIPTION;LANGUAGE=it:"+props["DESCRIPTION"],"TRANSP:TRANSPARENT","CLASS:PUBLIC","CATEGORIES:FESTIVITA-ITALIANE","END:VEVENT"]
lines.append("END:VCALENDAR")
(base/"festivita_italia.ics").write_bytes(("\r\n".join(map(fold,lines))+"\r\n").encode("utf-8"))
