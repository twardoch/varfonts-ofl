#!/usr/bin/env python
import sys

def varrec(i, m): 
	lines = []
	lines.append('      <FeatureVariationRecord index="%s">' % (i))
	lines.append('        <ConditionSet>' % ())
	lines.append('          <!-- ConditionCount=1 -->' % ())
	lines.append('          <ConditionTable index="0" Format="1">' % ())
	lines.append('            <AxisIndex value="0"/>' % ())
	lines.append('            <FilterRangeMinValue value="%s"/>' % (float(i+1)/(m+2)))
	lines.append('            <FilterRangeMaxValue value="%s"/>' % (float(i+2)/(m+2)))
	lines.append('          </ConditionTable>' % ())
	lines.append('        </ConditionSet>' % ())
	lines.append('        <FeatureTableSubstitution>' % ())
	lines.append('          <Version value="0x00010000"/>' % ())
	lines.append('          <!-- SubstitutionCount=1 -->' % ())
	lines.append('          <SubstitutionRecord index="0">' % ())
	lines.append('            <FeatureIndex value="1"/>' % ())
	lines.append('            <Feature>' % ())
	lines.append('              <!-- LookupCount=1 -->' % ())
	for j in range(0, i+1): 
		lines.append('              <LookupListIndex index="%s" value="%s"/>' % (j, j))
	lines.append('            </Feature>' % ())
	lines.append('          </SubstitutionRecord>' % ())
	lines.append('        </FeatureTableSubstitution>' % ())
	lines.append('      </FeatureVariationRecord>' % ())
	return lines

lines = []
lines += [line.rstrip() for line in file('ZinzinVF.G_S_U_B_.begin.ttx').readlines()]
m = int(sys.argv[1])
for k in range(0, m): 
	lines += varrec(k, m)
lines += [line.rstrip() for line in file('ZinzinVF.G_S_U_B_.end.ttx').readlines()]
out = file('ZinzinVF.G_S_U_B_.ttx', 'w')
out.write('\n'.join(lines))
out.close()
print('OK')
