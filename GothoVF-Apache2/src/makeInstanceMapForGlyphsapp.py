#!/usr/bin/env python
# This script generates a text file
# the contents of which can be copied into the clipboard
# then pasted into the left pane of Glyphs 
# Font Info / Instances tab

def line(s, l): 
    s += l + "\n"
    return s

custs = {
    0: "", 
}

wghts = {
    50: ["100 Th", "Thin"], 
    75: ["200 ExLt", "ExtraLight"], 
    110: ["300 Lt", "Light"], 
    150: ["400 Rg", ""], 
    180: ["500 Md", "Medium"], 
    220: ["600 SmBd", "SemiBold"], 
    250: ["700 Bd", "Bold"], 
    275: ["800 ExBd", "ExtraBold"], 
    300: ["900 Blk", "Black"],
}

wdths = { 
    70: ["2 ExCd", "Extra Condensed"], 
    77: ["3 Cd", "Condensed"], 
    84: ["4 SmCd", "SemiCondensed"], 
    92: ["5 No", ""], 
    100: ["6 SmWd", "Semi Expanded"], 
    110: ["7 Wd", "Expanded"], 
    120: ["8 ExWd", "Extra Expanded"], 
}
italics = { 
    0: ["", "GothoVF"], 
} 

italic = italics[0] # set 0 for upright, 1 for italic, then run

s = ''
s = line(s, '(')
for cust in sorted(custs.keys()): 
    for wdth in sorted(wdths.keys()): 
        for wght in sorted(wghts.keys()): 
            s = line(s, '        {')
#            s = line(s, '        customParameters =         (')
#            s = line(s, '                        {')
#            s = line(s, '                name = "Rename Glyphs";')
#            s = line(s, '                value =                 (')
#            s = line(s, '                    "six.alt=six,nine.alt=nine,g.alt=g,R.alt=R"')
#            s = line(s, '                );')
#            s = line(s, '            }')
#            s = line(s, '        );')
            s = line(s, '        interpolationCustom = %s;' % (cust))
            s = line(s, '        interpolationWeight = %s;' % (wght))
            s = line(s, '        interpolationWidth = %s;' % (wdth))
            s = line(s, '        name = "%s%s %s%s";' % (custs[cust], wdths[wdth][0], wghts[wght][0], italic[0]))
            if wghts[wght][1] != "": 
                s = line(s, '        weightClass = %s;' % (wghts[wght][1]))
            if wdths[wdth][1] != "": 
                s = line(s, '        widthClass = "%s";' % (wdths[wdth][1]))
            s = line(s, '    },')

s = line(s, ')')
f = file("%s.txt" % italic[1], "w")
f.write(s)
f.close()

