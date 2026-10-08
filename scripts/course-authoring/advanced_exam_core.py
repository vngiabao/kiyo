"""Parse authored question rows; do not generate content, levels or answer keys."""
from exam_authoring import R,L,C,O,mix,write_bank

def questions(kind,text):
    out=[]
    for row in text.strip().splitlines():
        p=[s.strip() for s in row.split('|')]
        assert len(p)==12,p
        out.append(kind(p[0],p[1],p[2],list(zip(p[3:11:2],p[4:11:2])),p[11]))
    return out

def ordering(text):
    out=[]
    for row in text.strip().splitlines():
        p=[s.strip() for s in row.split('|')]
        assert len(p)==7,p
        out.append(O(p[0].split('/'),p[1],p[2],p[3:6],p[6]))
    return out

def group(r,l,o,c):
    return mix(questions(R,r),questions(L,l),ordering(o),questions(C,c))
