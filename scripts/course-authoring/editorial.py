"""Compact serialization of explicitly authored editorial material.

All examples, facts, distractors and feedback come from the unit source. This
helper supplies structure only; it does not invent Chinese course content.
"""
import common as c

def paired_unit(uid,title,goals,rows,*sections):
    """Serialize two explicitly written contexts per vocabulary item."""
    from context_recycling import CONTEXTS
    assert all(len(row)==8 for row in rows),(uid,'each word needs two authored contexts')
    CONTEXTS[uid]={r[0]:(r[6],r[7]) for r in rows}
    unit(uid,title,goals,[r[:6] for r in rows],*sections)

def unit(uid,title,goals,words,grammar,dialogue,reading,media,practice,pragmatics,turns,flags):
    def passage(suffix,spec):
        heading,purpose,rows,questions,blanks,drama=spec
        return c.text(uid,suffix,heading,purpose,rows,questions,blanks,drama)
    c.write(uid,title,goals,words,grammar,passage('d',dialogue),
        passage('r',reading),passage('media',media),practice,pragmatics,turns,flags)
