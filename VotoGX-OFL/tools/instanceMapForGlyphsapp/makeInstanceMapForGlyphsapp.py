#!/usr/bin/env python
# This script generates a text file
# the contents of which can be copied into the clipboard
# then pasted into the left pane of Glyphs 
# Font Info / Instances tab

def line(s, l): 
    s += l + "\n"
    return s

custs = {
    12: "12", 
    18: "18", 
    24: "24", 
    36: "36", 
    48: "48", 
    60: "60", 
    72: "72",
}

wghts = {
    28: ["100", "Thin"], 
    37: ["200", "ExtraLight"], 
    51: ["300", "Light"], 
    70: ["400", ""], 
    92: ["500", "Medium"], 
    118: ["600", "SemiBold"], 
    144: ["700", "Bold"], 
    171: ["800", "ExtraBold"], 
    194: ["900", "Black"],
}

wdths = { 
    50: ["1", "Ultra Condensed"], 
    60: ["2", "Extra Condensed"], 
    70: ["3", "Condensed"], 
    80: ["4", "SemiCondensed"], 
    90: ["5", ""], 
    100: ["6", "Semi Expanded"], 
    110: ["7", "Expanded"], 
    120: ["8", "Extra Expanded"], 
    130: ["9", "Ultra Expanded"], 
}
italics = { 
    0: ["", "VotoSerif-MM"], 
    1: [" i", "VotoSerif-ItalicMM"],
} 

italic = italics[1] # set 0 for upright, 1 for italic, then run

s = ''
s = line(s, '(')
for cust in sorted(custs.keys()): 
    for wdth in sorted(wdths.keys()): 
        for wght in sorted(wghts.keys()): 
            s = line(s, '        {')
            s = line(s, '        interpolationCustom = %s;' % (cust))
            s = line(s, '        interpolationWeight = %s;' % (wght))
            s = line(s, '        interpolationWidth = %s;' % (wdth))
            s = line(s, '        name = "%s %s %s%s";' % (custs[cust], wdths[wdth][0], wghts[wght][0], italic[0]))
            if wghts[wght][1] != "": 
                s = line(s, '        weightClass = %s;' % (wghts[wght][1]))
            if wdths[wdth][1] != "": 
                s = line(s, '        widthClass = "%s";' % (wdths[wdth][1]))
            s = line(s, '    },')
s = line(s, ')')
f = file("%s.txt" % italic[1], "w")
f.write(s)
f.close()

