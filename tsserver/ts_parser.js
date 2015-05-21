/// <reference path="typescript.d.ts"/>
/// <reference path="node.d.ts"/>
var ts = require("typescript");
var TokenClass = ts.TokenClass;
var classifier = ts.createClassifier();
function parseLine(lineText) {
    var res = classifier.getClassificationsForLine(lineText, 0 /* None */, true);
    var start = 0;
    for (var _i = 0, _a = res.entries; _i < _a.length; _i++) {
        var entry = _a[_i];
        var cur_text = lineText.substr(start, entry.length);
        start += entry.length;
        console.log("content: " + cur_text + ", classification: " + TokenClass[entry.classification]);
    }
}
var content = "\n    var t: { memb: string };\n    document.createElement(\"div\");\n    var st = 10\n    console.log(\"this is a test\");\n";
parseLine(content);
