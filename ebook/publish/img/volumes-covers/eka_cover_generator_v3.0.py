"""
EKA Cover Generator v3.0

Adds Gumroad square thumbnails (1200 x 1200 by default, exceeding the
minimum 600 x 600 requirement supplied by the user).

Requires: Pillow
Run: python eka_cover_generator_v3.py
"""
from __future__ import annotations
import math
from pathlib import Path
from typing import Iterable
from PIL import Image, ImageDraw, ImageFilter, ImageFont

# ---------------- Feature switches ----------------
USE_3D_SHADOW = True
USE_GRADIENT_BACKGROUND = True
USE_HD_PRINT_VERSION = True

# ---------------- Brand configuration ----------------
VERSION = "3.0"
SERIES_1 = "EXECUTABLE KNOWLEDGE"
SERIES_2 = "ARCHITECTURE (EKA)"
DISCIPLINE = "Mastering Ontology Engineering"
HERITAGE = "with Protégé and Pizza.owl"
JOURNEY = "From Pizza.owl to Executable Intelligence"
AUTHOR = "XIAOQI ZHAO"
OUT = Path("eka_generated_covers")
PRINT_DPI = 300

PRESETS = {
    "amazon":  {"label":"Amazon版本", "w":1600,"h":2560,"dpi":72,"suffix":"amazon"},
    "leanpub": {"label":"Leanpub版本","w":1600,"h":2560,"dpi":144,"suffix":"leanpub"},
    "print":   {"label":"高清印刷版（300 DPI）","w":1800,"h":2700,"dpi":300,"suffix":"print_300dpi"},
    "website": {"label":"网站宣传横幅版","w":2800,"h":1000,"dpi":72,"suffix":"website"},
    "linkedin":{"label":"LinkedIn推广图版","w":1200,"h":627,"dpi":72,"suffix":"linkedin"},
    "gumroad": {"label":"Gumroad Thumbnail","w":1200,"h":1200,"dpi":72,"suffix":"gumroad_thumbnail"},
}

VOLUMES = [
 {"volume":1,"chapters":"Chapters 00-08","theme":"SEMANTIC FOUNDATIONS","description":"Learning Ontology Engineering through Protégé and Pizza.owl","background":"#0B2E28","accent":"#1D9E75","light":"#9FE1CB"},
 {"volume":2,"chapters":"Chapters 09-13","theme":"SEMANTIC RELATIONSHIPS","description":"Mastering Object Properties and Ontology Structures","background":"#0A2138","accent":"#378ADD","light":"#B5D4F4"},
 {"volume":3,"chapters":"Chapters 14-16","theme":"SEMANTIC LOGIC","description":"OWL Restrictions, Reasoning and Governance","background":"#211A3D","accent":"#7F77DD","light":"#CECBF6"},
 {"volume":4,"chapters":"Chapters 17-24","theme":"SEMANTIC KNOWLEDGE ENGINEERING","description":"The Semantic Knowledge Development Lifecycle (SKDL)","background":"#2D1F0B","accent":"#E8913A","light":"#F5D0A0"},
 {"volume":5,"chapters":"Chapters 25-30","theme":"KNOWLEDGE GRAPH ENGINEERING","description":"Transforming Ontologies into Connected Intelligence","background":"#1E293B","accent":"#38BDF8","light":"#BAE6FD"},
 {"volume":6,"chapters":"Chapters 31-36","theme":"AI-READY SEMANTIC SYSTEMS","description":"Knowledge Graphs, Agents and Intelligent Retrieval","background":"#18222A","accent":"#64748B","light":"#CBD5E1"},
 {"volume":7,"chapters":"Chapters 37-42","theme":"EXECUTABLE INTELLIGENCE","description":"Realizing the Vision of Executable Knowledge Architecture","background":"#1C0A0A","accent":"#E11D48","light":"#FDA4AF"},
]

FONT_CANDIDATES = {
 "serif_bold":["DejaVuSerif-Bold.ttf","/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf","C:/Windows/Fonts/georgiab.ttf","/Library/Fonts/Georgia Bold.ttf"],
 "sans":["DejaVuSans.ttf","/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf","C:/Windows/Fonts/arial.ttf","/Library/Fonts/Arial.ttf"],
 "sans_bold":["DejaVuSans-Bold.ttf","/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf","C:/Windows/Fonts/arialbd.ttf","/Library/Fonts/Arial Bold.ttf"],
 "sans_italic":["DejaVuSans-Oblique.ttf","/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf","C:/Windows/Fonts/ariali.ttf","/Library/Fonts/Arial Italic.ttf"],
}
def font_path(role):
    for p in FONT_CANDIDATES[role]:
        try: ImageFont.truetype(p,20); return p
        except OSError: pass
    raise FileNotFoundError(f"No usable font for {role}")
F_SERIF=font_path("serif_bold"); F_SANS=font_path("sans"); F_BOLD=font_path("sans_bold"); F_ITALIC=font_path("sans_italic")

def rgb(h):
    h=h.lstrip("#"); return tuple(int(h[i:i+2],16) for i in (0,2,4))
def blend(a,b,t): return tuple(round(x+(y-x)*t) for x,y in zip(a,b))
def lighten(h,t=.5): return blend(rgb(h),(255,255,255),t)

def background(w,h,bg,accent):
    if not USE_GRADIENT_BACKGROUND: return Image.new("RGB",(w,h),rgb(bg))
    top=blend(rgb(bg),rgb(accent),.16); bottom=blend(rgb(bg),(0,0,0),.22)
    im=Image.new("RGB",(w,h)); d=ImageDraw.Draw(im)
    for y in range(h):
        c=blend(top,bottom,y/max(1,h-1)); d.line((0,y,w,y),fill=c)
    return im

def wrap_pixels(draw,text,font,max_w):
    lines=[]
    for paragraph in text.splitlines() or [text]:
        words=paragraph.split(); current=""
        for word in words:
            trial=word if not current else current+" "+word
            if draw.textbbox((0,0),trial,font=font)[2] <= max_w: current=trial
            else:
                if current: lines.append(current)
                current=word
        if current: lines.append(current)
    return "\n".join(lines)

def fit(draw,text,path,max_w,max_h,max_size,min_size=16,max_lines=3):
    for size in range(max_size,min_size-1,-2):
        f=ImageFont.truetype(path,size); wrapped=wrap_pixels(draw,text,f,max_w); spacing=max(4,size//6)
        box=draw.multiline_textbbox((0,0),wrapped,font=f,spacing=spacing,align="center")
        if box[2]-box[0]<=max_w and box[3]-box[1]<=max_h and wrapped.count("\n")+1<=max_lines:
            return wrapped,f,spacing
    f=ImageFont.truetype(path,min_size); return wrap_pixels(draw,text,f,max_w),f,max(4,min_size//6)

def center(im,draw,x,y,text,font,fill,spacing=6,shadow=False):
    if shadow and USE_3D_SHADOW:
        layer=Image.new("RGBA",im.size,(0,0,0,0)); sd=ImageDraw.Draw(layer); off=max(3,im.width//300)
        sd.multiline_text((x+off,y+off),text,font=font,fill=(0,0,0,130),anchor="ma",align="center",spacing=spacing)
        layer=layer.filter(ImageFilter.GaussianBlur(max(2,off//2))); im.paste(layer,(0,0),layer)
    draw.multiline_text((x,y),text,font=font,fill=fill,anchor="ma",align="center",spacing=spacing)

def pizza(draw,cx,cy,size,accent,bg):
    pts=[]
    for i in range(71):
        a=math.radians(-150+120*i/70); pts.append((cx+size*math.cos(a),cy+size*math.sin(a)))
    pts.append((cx,cy+size*1.15)); draw.polygon(pts,fill=rgb(accent))
    cr=size+5; thick=max(10,int(size*.11))
    for i in range(71):
        a=math.radians(-150+120*i/70); x=cx+cr*math.cos(a); y=cy+cr*math.sin(a)
        draw.ellipse((x-thick/2,y-thick/2,x+thick/2,y+thick/2),fill=lighten(accent,.5))
    for dx,dy,rr in [(-.03,-.05,.13),(-.22,.16,.11),(.19,.13,.12),(.08,.36,.10),(-.14,.38,.09)]:
        x=cx+size*dx; y=cy+size*dy; r=size*rr; draw.ellipse((x-r,y-r,x+r,y+r),fill=rgb(bg))

def portrait(v,w,h,dpi,path):
    s=w/1600; im=background(w,h,v["background"],v["accent"]); d=ImageDraw.Draw(im); x=w//2
    d.rectangle((int(w*.028),int(w*.028),w-int(w*.028),h-int(w*.028)),outline=rgb(v["accent"]),width=max(2,int(w*.0015)))
    def put(text,pathf,y,maxw,maxh,maxsize,minsize,lines,color,shadow=False):
        t,f,sp=fit(d,text,pathf,int(maxw*w),int(maxh*h),max(12,int(maxsize*s)),max(10,int(minsize*s)),lines)
        center(im,d,x,int(y*h),t,f,color,sp,shadow)
    put(JOURNEY,F_SANS,.04,.78,.045,36,22,2,rgb(v["light"])); pizza(d,x,h*.18,w*.115,v["accent"],v["background"])
    put(SERIES_1,F_SERIF,.35,.86,.06,82,50,1,(255,255,255),True); put(SERIES_2,F_SERIF,.395,.86,.06,82,50,1,(255,255,255),True)
    put(DISCIPLINE,F_SANS,.452,.74,.034,42,25,1,rgb(v["light"])); put(HERITAGE,F_ITALIC,.482,.74,.034,44,25,1,rgb(v["accent"]))
    d.line((w*.375,h*.521,w*.625,h*.521),fill=rgb(v["accent"]),width=max(3,int(3*s)))
    put(f"VOLUME {v['volume']}",F_BOLD,.54,.55,.055,74,42,1,rgb(v["accent"]),True); put(v["chapters"],F_SANS,.585,.6,.04,44,28,1,(255,255,255))
    put(v["theme"],F_BOLD,.675,.82,.075,48,26,2,rgb(v["light"])); put(v["description"],F_SANS,.72,.78,.095,42,24,3,rgb(v["light"]))
    put(AUTHOR,F_BOLD,.92,.55,.04,50,30,1,(255,255,255)); path.parent.mkdir(parents=True,exist_ok=True); im.save(path,dpi=(dpi,dpi),optimize=True); return im

def gumroad_thumbnail(v,path):
    """Square Gumroad thumbnail optimized for small-card readability."""
    p=PRESETS["gumroad"]; w=h=p["w"]; im=background(w,h,v["background"],v["accent"]); d=ImageDraw.Draw(im); x=w//2
    d.rectangle((30,30,w-30,h-30),outline=rgb(v["accent"]),width=3)
    pizza(d,x,h*.22,w*.13,v["accent"],v["background"])
    def put(text,fp,y,maxw,maxh,maxsize,minsize,lines,color,shadow=False):
        t,f,sp=fit(d,text,fp,int(maxw*w),int(maxh*h),maxsize,minsize,lines); center(im,d,x,int(y*h),t,f,color,sp,shadow)
    put("EXECUTABLE KNOWLEDGE\nARCHITECTURE (EKA)",F_SERIF,.42,.88,.18,64,38,2,(255,255,255),True)
    put(f"VOLUME {v['volume']}",F_BOLD,.61,.55,.08,58,32,1,rgb(v["accent"]),True)
    put(v["theme"],F_BOLD,.70,.82,.12,44,24,2,rgb(v["light"]))
    put("Protégé • Pizza.owl • Ontology Engineering",F_SANS,.86,.88,.06,28,18,2,rgb(v["light"]))
    put(AUTHOR,F_BOLD,.935,.55,.045,28,18,1,(255,255,255))
    path.parent.mkdir(parents=True,exist_ok=True); im.save(path,dpi=(72,72),optimize=True); return im

def shadow_paste(canvas,cover,pos):
    x,y=pos
    if USE_3D_SHADOW:
        sh=Image.new("RGBA",canvas.size,(0,0,0,0)); sd=ImageDraw.Draw(sh); off=max(5,cover.width//22)
        sd.rectangle((x+off,y+off,x+cover.width+off,y+cover.height+off),fill=(0,0,0,180)); sh=sh.filter(ImageFilter.GaussianBlur(max(5,cover.width//28))); canvas.paste(sh,(0,0),sh)
    canvas.paste(cover,(x,y))

def promo(kind,path):
    p=PRESETS[kind]; w,h=p["w"],p["h"]; im=background(w,h,"#111827","#378ADD"); d=ImageDraw.Draw(im)
    title,f,sp=fit(d,"EXECUTABLE KNOWLEDGE ARCHITECTURE (EKA)",F_BOLD,int(w*.9),int(h*.11),58 if kind=="website" else 38,20,2)
    center(im,d,w//2,int(h*.045),title,f,(255,255,255),sp,True)
    sub,f,sp=fit(d,JOURNEY,F_SANS,int(w*.8),int(h*.07),32 if kind=="website" else 23,16,2); center(im,d,w//2,int(h*.12),sub,f,(170,178,190),sp)
    cols=7 if kind=="website" else 4; cw=int(w*(.105 if kind=="website" else .145)); ch=int(cw*1.6); gap=int(w*(.012 if kind=="website" else .022)); top=int(h*(.20 if kind=="website" else .24))
    for i,v in enumerate(VOLUMES):
        row=i//cols; col=i%cols; count=min(cols,len(VOLUMES)-row*cols); roww=count*cw+(count-1)*gap; sx=(w-roww)//2
        temp=portrait(v,500,800,72,OUT/"_temporary"/f"v{v['volume']}.png").resize((cw,ch),Image.Resampling.LANCZOS)
        shadow_paste(im,temp,(sx+col*(cw+gap),top+row*(ch+int(h*.07))))
    path.parent.mkdir(parents=True,exist_ok=True); im.save(path,dpi=(p["dpi"],p["dpi"]),optimize=True)

def choose_volumes():
    print("\n请选择需要生成的卷：\n0. 全部 Volume 1-7\n1-7. 指定 Volume")
    raw=input("请输入卷号 [默认 0]：").strip() or "0"
    if raw=="0": return VOLUMES
    try:
        n=int(raw); return [next(v for v in VOLUMES if v["volume"]==n)]
    except Exception:
        print("输入无效，改为生成全部。") ; return VOLUMES

def covers(kind,vols):
    p=PRESETS[kind]; folder=OUT/p["suffix"]; print(f"\n正在生成：{p['label']} ({p['w']} x {p['h']}, {p['dpi']} DPI)")
    for v in vols:
        out=folder/f"EKA_Volume_{v['volume']}_{p['suffix']}.png"
        if kind=="gumroad": gumroad_thumbnail(v,out)
        else: portrait(v,p["w"],p["h"],p["dpi"],out)
        print("已生成：",out)

def menu():
    print(f"\n{'='*62}\nEKA Cover Generator v{VERSION}\n{'='*62}")
    print("自动生成：\n1. Amazon版本\n2. Leanpub版本\n3. 高清印刷版（300 DPI）\n4. 网站宣传横幅版\n5. LinkedIn推广图版\n6. Gumroad Thumbnail（正方形 1200x1200）\n7. 一次生成全部版本\n0. 退出")
    print(f"\nUSE_3D_SHADOW = {USE_3D_SHADOW}\nUSE_GRADIENT_BACKGROUND = {USE_GRADIENT_BACKGROUND}\nUSE_HD_PRINT_VERSION = {USE_HD_PRINT_VERSION}\n")

def main():
    OUT.mkdir(parents=True,exist_ok=True); menu(); c=input("请选择输出类型 [0-7]：").strip()
    if c=="0": return
    if c in {"1","2","3","6"}:
        kind={"1":"amazon","2":"leanpub","3":"print","6":"gumroad"}[c]
        if kind=="print" and not USE_HD_PRINT_VERSION: print("高清印刷版开关已关闭。"); return
        covers(kind,choose_volumes()); return
    if c=="4": promo("website",OUT/"website"/"EKA_7_Volumes_Website_Banner.png"); return
    if c=="5": promo("linkedin",OUT/"linkedin"/"EKA_7_Volumes_LinkedIn.png"); return
    if c=="7":
        for kind in ("amazon","leanpub","gumroad"): covers(kind,VOLUMES)
        if USE_HD_PRINT_VERSION: covers("print",VOLUMES)
        promo("website",OUT/"website"/"EKA_7_Volumes_Website_Banner.png")
        promo("linkedin",OUT/"linkedin"/"EKA_7_Volumes_LinkedIn.png")
        print("全部版本生成完成：",OUT.resolve()); return
    print("输入无效，请输入 0-7。")

if __name__ == "__main__": main()
