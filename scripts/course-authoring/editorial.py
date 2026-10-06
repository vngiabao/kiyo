"""Compact serialization of explicitly authored editorial material.

All examples, facts, distractors and feedback come from the unit source. This
helper supplies structure only; it does not invent Chinese course content.
"""
import common as c

def unit(uid,title,goals,words,grammar,dialogue,reading,media,practice,pragmatics,turns,flags):
    def passage(suffix,spec):
        heading,purpose,rows,questions,blanks,drama=spec
        return c.text(uid,suffix,heading,purpose,rows,questions,blanks,drama)
    c.write(uid,title,goals,words,grammar,passage('d',dialogue),
        passage('r',reading),passage('media',media),practice,pragmatics,turns,flags)
