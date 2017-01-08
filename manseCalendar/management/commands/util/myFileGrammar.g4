grammar myFileGrammar;

line: solarDate '\t' lunarDate;

solarDate: '양력' date;
lunarDate: '음력' date '(' monthKind ')';

date : year '년' month '월' day '일';
monthKind: '평달' | '윤달';

year: DIGIT*;
month: DIGIT*;
day : DIGIT*;


DIGIT: [0-9];

WS : [ \r\n]+ -> skip ; // skip spaces, tabs, newlines, \r (Windows)
