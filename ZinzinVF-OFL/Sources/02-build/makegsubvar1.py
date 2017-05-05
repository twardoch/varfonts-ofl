#!/usr/bin/env python

def varrec(i): 
	print('      <FeatureVariationRecord index="%s">' % (i))
	print('        <ConditionSet>' % ())
	print('          <!-- ConditionCount=1 -->' % ())
	print('          <ConditionTable index="0" Format="1">' % ())
	print('            <AxisIndex value="0"/>' % ())
	print('            <FilterRangeMinValue value="0.001"/>' % ())
	print('            <FilterRangeMaxValue value="%s"/>' % (float(i)/1000+0.002))
	print('          </ConditionTable>' % ())
	print('        </ConditionSet>' % ())
	print('        <FeatureTableSubstitution>' % ())
	print('          <Version value="0x00010000"/>' % ())
	print('          <!-- SubstitutionCount=1 -->' % ())
	print('          <SubstitutionRecord index="0">' % ())
	print('            <FeatureIndex value="1"/>' % ())
	print('            <Feature>' % ())
	print('              <!-- LookupCount=1 -->' % ())
	print('              <LookupListIndex index="%s" value="%s"/>' % (i, i))
	print('            </Feature>' % ())
	print('          </SubstitutionRecord>' % ())
	print('        </FeatureTableSubstitution>' % ())
	print('      </FeatureVariationRecord>' % ())

for k in range(0, 351): 
	varrec(k)
