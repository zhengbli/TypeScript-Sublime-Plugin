/// <reference path="typescript.d.ts"/>
/// <reference path="node.d.ts"/>
import ts = require("typescript");
import TokenClass = ts.TokenClass;

interface SublimeRegion {
    region: [number, number];
    scope: string;
}

var classifier = ts.createClassifier();

function parseLine(lineText: string) {
    var res = classifier.getClassificationsForLine(
        lineText,
        ts.EndOfLineState.None,
        true
        );
    var start = 0
    for( var entry of res.entries ) {
        var cur_text = lineText.substr(start, entry.length);
        start += entry.length;
        console.log("content: " + cur_text + ", classification: " + TokenClass[entry.classification]);
    }
}

var content = `
    var t: { memb: string };
    document.createElement("div");
    var st = 10
    console.log("this is a test");
`

parseLine(content);

