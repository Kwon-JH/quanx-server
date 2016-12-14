/**
 * Created by yoonjechoi on 2016. 12. 13..
 */


var fs = require('fs');


var table = [];
for(var i = 1800; i < 2101; i++) {
    var filePath = 'data/data_' + i.toString() + ".json";
    var content = fs.readFileSync(filePath, { encoding:'utf-8'});

    var obj = JSON.parse(content);

    for(var j = 0; j < obj.length; j++) {
        table.push(obj[j]);
    }
}

fs.writeFileSync("solarTerm_1800-2100.json", JSON.stringify(table));
