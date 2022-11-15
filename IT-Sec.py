import math

text = ' AH;W""SHVJSHAWVHTSD"SKHt AHJ HASKHW ASK HAS HlSJu;VWDZSijHt AHWtZHoSJAS HgSJ"S H SoS HJ;KjHAWHV"W AS HAJSHQKWoW "S HVzHJ HneSJHlSJ;S jHJ..SKHSJ SKHNiSJ SKHWiVHASKHW ASKSjHOz HAS.HWiiSKLKzSVV"S HlJSVS jHASKHeWKHneSJH-SJiS H;zu;jHoJVHntHAS.HWiiSKeJ nJLV"S HTeSKLjHASKHeWKHVzHLKzVVHeJSH.SJ HNiSJ SKHbJ LSKIHd AHOzKHJ;KHV"W AS HOJSiSHbtSKV"S Ht AHqSKnzSLSIHaWH"KW"H t HASKH-W  HneJVu;S HVJSHt AHVWL"ScH,bKWtjHoJV"HAtH t H:WJVSKC,HmH,sWj,HVWL"SHVJSjH,Ju;HoJ H:WJVSKI,HaWHV"Sii"SHSKHVJu;H t H;J Ht AHoSVW;HVJSHVJu;HKSu;"jHt AHWiVHSKHVJSHVzHSJ SHTSJ"iW LHW LSVS;S H;W""SjHAWHVWL"SHSKcH,wu;jHbKWtjHeJSHV"S;"HAJKHAWVHVu;zS jHAWVVHAtH:WJVSKHoJV"I,HmH,-W  j,HVWL"SHVJSjH,eWVHV"S;V"HAtHAWCHpu;HoJ H t H:WJVSKjH t HeJiiHJu;HWtu;HfWDV"HeSKAS FHLS;H;J Hnt.Hkt""I,HmH,wu;HbKWtj,HVWL"SHASKH-W  jH,eWVHeJiiV"HAtHAS  H Ju;"HWiiSVCHfWDV"HNW  V"HAtH Ju;"HeSKAS jHJ; HLJo"MVH tKHSJ .WiHJ HASKH?;KJV"S ;SJ"cHAWVHNW  HSKHAzu;H Ju;"H.Wu;S v,HmH,-W  j,HVWL"SHVJSjH,Ju;HeJiiHfWDV"HeSKAS jHLS;HLiSJu;H;J jHJu;H.tVVH;St"SH zu;HfWDV"HeSKAS I,HmH,GSJ jHbKWtj,HVWL"SHASKH-W  jH,AWVH.WLHJu;HJ;.H Ju;"HVWLS jHAWVHJV"H Ju;"HLt"jHAWVHJV"HntOJSiHOSKiW L"jHnt.HfWDV"HNW  HAJu;HASKHkt""H Ju;"H.Wu;S I,HmH,-W  jHVu;eW"nHNSJ HAt..SVHTStLv,HVWL"SHAJSHbKWtIH,:W  HSKH:WJVSKH.Wu;S jHVzHNW  HSKHWtu;HSJ S HfWDV"H.Wu;S IHRS;HVzZzK"H;J FHJu;HoJ H:WJVSKjHt AHAtHoJV"HAzu;H.SJ H-W  IHxJiiV"HAtHez;iH;J LS;S C,HaWHetKASHJ;.HLW nHoW LHnt.t"SjHt AHSKHLJ LH;J jHWoSKHJ;.HeWKHLW nHZiWtHAWoSJFHSKHnJ""SK"SHt AHoSo"SjHt AHAJSH: JSHt AHxWAS HVu;iz""SK"S HJ;.IHd AHAWHV"KJu;HVzHSJ HxJ AHtSoSKHAWVHBW AjHt AHAJSHxziNS HZizLS jHt AHSVHetKASHVzHAtSV"SKHeJSHLSLS HAS HwoS AHntcHAJSHkiWS""SKHeS;"S HOz HAS HkWSt.S jHt AHAWVHxWVVSKHLJ LH;zu;Ht AHoKWtV"SHVzjHWiVHzoHSVHNzu;"SjHt AHDiW"Vu;"SHW HAWVHdZSKjHt AHJ HASKHbSK SHVW;HSKHAJSHgu;JZZSjHAJSHLWoS HGz"Vu;tSVVSHWoHt AH"W n"S Ht AHVDKW LS HWtZHAS HxzLS IHazu;HeWKHASKHqJ..SiHJ HASKH-J""SH zu;HSJ HoJVVu;S HoiWtjHWoSKHW HAS HgSJ"S jHAWHnzLHSVHVzHKSu;"HKz"HWtZHeJSHSJ HVu;eSKSVHRSeJ""SKIHaWHLJ LHSKHLW nHOSKnWL"H;J Ht AHV"W AHAWHJ HVSJ SKHw LV"Ht AHVWL"ScH,-WS  iSJ jH-WS  iSJ jHQJ.DSHQSjHkt""hSjHkt""hSHJ HASKHgSSjH-SJ SHbKWtjHAJSHpiVSoJiijHxJiiH Ju;"HVzjHeJSHJu;Hez;iHeJiiI,H,GWjHeWVHeJiiHVJSHAS  C,HVWL"SHASKHkt""IH,wu;,FHVWL"SHASKH-W  jH,VJSHeJiiHfWDV"HeSKAS I,HmH,RS;H tKH;J jHVJSHJV"HSVHVu;z j,HVWL"SHASKHkt""IHaWHLJ LHSKH;J jHt AHWiVHSKHW NW.jHAWHeWKHAWHSJ SHLKzVVSH:JKu;SjHOz HiWt"SKHfWiWSV"S Ht.LSoS IHaWHAKWS L"SHSKVJS;HAtKu;HAWVHEziNFHJ eS AJLHeWKHWoSKHWiiSVH.J"H"WtVS AHt AH"WtVS AHBJu;"SK HSKiStu;"S"jHt AHVSJ SHbKWtHeWKHLW nHJ HRziAHLSNiSJAS"Ht AHVWVVHWtZHSJ S.H zu;HOJSiH;zS;SKS HQ;Kz Ht AH;W""SHAKSJHLKzVVSHLziAS SH:Kz S HWtZjHt AHt.HVJSH;SKt.jHAWHeWKHVzHOJSiHLSJV"iJu;SKHg"WW"jHt AHntHoSJAS HgSJ"S HOz HJ;KjHAWHV"W AS HneSJHlSJ;S HBJu;"SKjHAWVHLKzSVV"SHVzHAJuNHt AHVzHLKzVVHeJSHASKHWiiSKLKzSVV"SHQtK.jHoJVHntHAS.HWiiSKNiSJ V"S H:tSu;S iJu;"IHd AHWiiHAJSH:WJVSKHt AH:zS JLSjHAJSHiWLS HOzKHJ;KHWtZHAS H: JS Ht AHNtSVV"S HJ;KHAS HfW "zZZSiIH,bKWtj,HVWL"SHASKH-W  Ht AHVW;HVJSHVzHKSu;"HW jH,oJV"HAtH t HfWDV"C,HmH,sWj,HVWL"SHVJSjH,Ju;HoJ HfWDV"I,HaWHLJ LHSKH;J Ht AHVW;HVJSHKSu;"HW jHt AHAWHeWKHJ;.jHWiVHzoHSKHJ HAJSH;SiiSHgz  SHVWS;SIHwiVHSKHVJSHVzHSJ SHTSJ"iW LHW LSVS;S H;W""SjHVWL"SHSKcH,wu;HbKWtjHeJSHLt"HV"S;"HAJKHAWVjHAWVVHAtHfWDV"HoJV"v,HgJSHVWVVHWoSKHLW nHV"SJZHeJSHSJ HkWt.Ht AHKtS;K"SHt AHKSL"SHVJu;H Ju;"IHaWHVWL"SHSKcH,bKWtjH t HVSJHntZKJSAS jHAWVVHAtHfWDV"HoJV"jHAS  H t HNW  V"HAtHAzu;H Ju;"VH.S;KHeSKAS I,HmH,aWVHeJiiHJu;H.JKHoSAS NS j,HVWL"SHAJSHbKWtIHaW.J"HLJ LS HVJSHoSJASHntHkS""IHwoSKHVJSHeWKH Ju;"HntZKJSAS jHt AHAJSHRJSKHiJSVVHVJSH Ju;"HVu;iWZS FHVJSHAWu;"SHJ..SKjHeWVHVJSH zu;HeSKAS HNzS  "SIHaSKH-W  HVu;iJSZHKSu;"HLt"Ht AHZSV"jHSKH;W""SHW.HQWLHOJSiHiWtZS H.tSVVS FHAJSHbKWtHWoSKHNz  "SHLWKH Ju;"HSJ Vu;iWZS Ht AHeWKZHVJu;HAJSHLW nSHGWu;"HOz HSJ SKHgSJ"SHWtZHAJSHW ASKSHt AHAWu;"SHJ..SKHAWKtSoSKH Wu;jHeWVHVJSHez;iH zu;HeSKAS HNzS  "SjHt AHNz  "SHVJu;HAzu;HWtZH Ju;"VH.S;KHoSVJ  S IHp ASVVS Hezii"SHAJSHgz  SHWtZLS;S jHt AHWiVHVJSHAWVH-zKLS Kz"HVW;jHVS"n"SHVJSHVJu;HWtZKSu;"HJ.HkS""H;J Ht AHVW;HAWH;J SJ IHd AHWiVHVJSHWtVHAS.HbS V"SKHAJSHgz  SHVzH;SKWtZNz..S HVW;cHqWjHAWu;"SHVJSjHNW  HJu;H Ju;"HWtu;HAJSHgz  SHt AHAS H-z AHWtZLS;S HiWVVS CHmH,-W  j,HVWL"SHVJSHt AHV"JSVVHJ; H.J"HAS.HUiiS ozLS HJ HAJSHlJDDS FH,eWu;HWtZjHLS;H;J Hnt.Hkt""jHJu;HeJiiHeSKAS HeJSHASKHiJSoSHRz""I,HaSKH-W  HeWKH zu;HLW nHVu;iWZ"Kt NS jHWoSKHSKHSKVu;KWNHVzjHAWVVHSKHWtVHAS.HkS""HZJSiIHUKH.SJ "SjHSKH;WS""SHVJu;HOSK;zSK"jHKJSoHVJu;HAJSHwtLS HWtVHt AHVWL"ScH,wu;HbKWtjHeWVHVWLV"HAtC,HmH,-W  j,HVWL"SHVJSjH,eS  HJu;H Ju;"HAJSHgz  SHt AHAS H-z AHNW  HWtZLS;S HiWVVS jHAWVHNW  HJu;H Ju;"HWtV;Wi"S jHt AHJu;H;WoSHNSJ SHKt;JLSHg"t ASH.S;KjHAWVVHJu;HVJSH Ju;"HVSioV"HNW  HWtZLS;S HiWVVS I,HaWoSJHVW;HVJSHJ; HLW nHozSVSHW jHAWVVHJ; HSJ Hgu;WtASKHtSoSKiJSZIH,RiSJu;HLS;H;J jHJu;HeJiiHeSKAS HeJSHASKHiJSoSHRz""I,HmH,wu;HbKWtj,HVWL"SHASKH-W  Ht AHZJSiHOzKHJ;KHWtZHAJSH: JSjH,AWVHNW  HASKHkt""H Ju;"IH:WJVSKHt AHfWDV"HNW  HSKH.Wu;S FHmHJu;HoJ HAJu;jHLS;HJ HAJu;Ht AHoiSJoSHfWDV"I,HaWHtSoSKNW.HVJSHAJSHkzV;SJ"jHAJSHqWWKSHZizLS HJ;KHVzHeJiAHt.HAS H:zDZHt AHVJSHVu;KJScH,pu;H;Wi"SHAWVH Ju;"HWtVvHd AHJu;H;Wi"SHAWVH Ju;"HiWS LSKHWtVvHxJiiV"HAtH;J LS;S Cv,HaWHnzLHSKHVJu;HAJSHqzVSHW Ht AHiJSZHAWOz HeJSHt VJ  JLIHaKWtVVS HWoSKHLJ LHASKHg"tK.Ht AHoKWtV"SjHAWVVHSKHNWt.HWtZHAS HbtSVVS HV"S;S HNz  "SIHaJSHqWStVSKHt AHAJSHkWSt.SHetKAS Ht.LSeS;"jHt AHAJSHkSKLSHoSo"S jHt AHAJSHbSiVS V"tSuNSHKzii"S HJ HAJSHgSSjHt AHASKHqJ..SiHeWKHLW nHDSu;Vu;eWKnjHt AHSVHAz  SK"SHt AHoiJ"n"SjHt AHAJSHgSSHLJ LHJ HVzH;z;S HVu;eWKnS HxzLS HeJSH:JKu;"tSK.SHt AHkSKLSjHt AH;W""S HzoS HWiiSHSJ SHeSJVVSHgu;Wt.NKz SHWtZIHaWHVu;KJSHSKjHt AHNz  "SHVSJ HSJLS SVHxzK"H Ju;"H;zSKS cH,-WS  iSJ jH-WS  iSJ jHQJ.DSHQSjHkt""hSjHkt""hSHJ HASKHgSSjH-SJ SHbKWtjHAJSHpiVSoJiijHxJiiH Ju;"HVzjHeJSHJu;Hez;iHeJiiI,H,GWjHeWVHeJiiHVJSHAS  C,HVWL"SHASKHkt""IH,wu;j,HVWL"SHSKjH,VJSHeJiiHeSKAS HeJSHASKHiJSoSHRz""I,HmH,RS;H tKH;J jHVJSHVJ"n"HVu;z HeJSASKHJ HASKHbJVu;SK;tS""SI,HaWHVJ"nS HVJSH zu;HoJVHWtZHAS H;St"JLS HQWLIHUVHeWKHSJ .WiHSJ H-tSiiSKjHASKH;W""SHAKSJHOK'

kombi = 'ABCDEFGHIJKLMNOPQRSTUVWZabcdefghijklmnopqrstuvwxz -"_.:,;!?[]()'  
zählen = []
prozent = []
listDoppel = {}
for x in range(len(kombi)):
    zählen.append(0)
for i, s in enumerate(kombi):
    zählen[i] = text.count(s)
gesammt = len(text)
for y,p in enumerate(zählen):
    prozent.append(f'{kombi[y]}: {round(p * 100 / len(text), 6)}')
#print(zählen)
print(prozent)
for d, do in enumerate(text):
    try:
        if do == text[d +1]:
            if do in listDoppel:
                listDoppel[do] = listDoppel.get(do) + 1
            else:listDoppel[do] = 1
    except:
        pass
print(listDoppel)

# H=18 S=11  leerzeichen=8 J=6.2 W=5,7 V=5,4   A=4,48  "=4,33  K=4,18   ;=3,98
# E N I R T S A H D

neu = ''
for s in text:
    if s == 'H':
        neu += '     '
    elif s == 'S':
        neu += 'e'  
    elif s == ' ':
        neu += 'n'
    elif s == 'J':
        neu += 'i'
    elif s == 'W':
        neu += 'a'
    elif s == 'V':
        neu += 's'
    elif s == 'u':
        neu += 'c'
    elif s == ';':
        neu += 'h'
    elif s == '"':
        neu += 't'
    elif s == 'N':
        neu += 'k'
    elif s == 'A':
        neu += 'd'
    elif s == 't':
        neu += 'u'
    elif s == 'L':
        neu += 'g'
    elif s == '.':
        neu += 'm'
    elif s == 'K':
        neu += 'r'
    elif s == 'z':
        neu += 'o'
    elif s == 'i':
        neu += 'l'
    elif s == ':':
        neu += 'K'
    elif s == 'Q':
        neu += 'T'
    elif s == 'b':
        neu += 'F'
    elif s == 'g':
        neu += 'S'
    elif s == '-':
        neu += 'M'
    elif s == 'j':
        neu += ','    
    elif s == 'o':
        neu += 'b'
    elif s == 'k':
        neu += 'B'
    elif s == 'q':
        neu += 'H'
    elif s == 'Z':
        neu += 'f'
    elif s == 'e':
        neu += 'w'
    elif s == 'D':
        neu += 'p'
    elif s == 'n':
        neu += 'z'
    elif s == 'T':
        neu += 'Z'
    elif s == 'l':
        neu += 'R'
    elif s == 'd':
        neu += 'U'
    elif s == 'O':
        neu += 'v'
    elif s == 'I':
        neu += '.'
    elif s == 'a':
        neu += 'D'
    elif s == 'c':
        neu += ':'
    elif s == 'f':
        neu += 'P'
    elif s == 'p':
        neu += 'I'
    elif s == 'U':
        neu += 'E'
    elif s == 'G':
        neu += 'N'
    elif s == ',':
        neu += '"'
    elif s == 'x':
        neu += 'W'
    elif s == 'v':
        neu += '!'
    elif s == 'R':
        neu += 'G'
    elif s == 'm':
        neu += 'O'
    elif s == 'w':
        neu += 'A'
    elif s == 'B':
        neu += 'L'
    elif s == '?':
        neu += 'C'
    
    else: neu += '_'
    
    
print(neu)

# abcdefghijklmnopqrstuvwxyz
# DF:UwPS*l,BROzbIH**uc!AW*o