//============================================================
// Original ZALGO text script by tchouky
//============================================================

var zalgomap = {
    up: [
        '\u030d', '\u030e', '\u0304', '\u0305',
        '\u033f', '\u0311', '\u0306', '\u0310',
        '\u0352', '\u0357', '\u0351', '\u0307',
        '\u0308', '\u030a', '\u0342', '\u0343',
        '\u0344', '\u034a', '\u034b', '\u034c',
        '\u0303', '\u0302', '\u030c', '\u0350',
        '\u0300', '\u0301', '\u030b', '\u030f',
        '\u0312', '\u0313', '\u0314', '\u033d',
        '\u0309', '\u0363', '\u0364', '\u0365',
        '\u0366', '\u0367', '\u0368', '\u0369',
        '\u036a', '\u036b', '\u036c', '\u036d',
        '\u036e', '\u036f', '\u033e', '\u035b',
        '\u0346', '\u031a'
    ],
    down: [
        '\u0316', '\u0317', '\u0318', '\u0319',
        '\u031c', '\u031d', '\u031e', '\u031f',
        '\u0320', '\u0324', '\u0325', '\u0326',
        '\u0329', '\u032a', '\u032b', '\u032c',
        '\u032d', '\u032e', '\u032f', '\u0330',
        '\u0331', '\u0332', '\u0333', '\u0339',
        '\u033a', '\u033b', '\u033c', '\u0345',
        '\u0347', '\u0348', '\u0349', '\u034d',
        '\u034e', '\u0353', '\u0354', '\u0355',
        '\u0356', '\u0359', '\u035a', '\u0323' 
    ],
    mid: [
        '\u0315', '\u031b', '\u0340', '\u0341',
        '\u0358', '\u0321', '\u0322', '\u0327',
        '\u0328', '\u0334', '\u0335', '\u0336',
        '\u034f', '\u035c', '\u035d', '\u035e',
        '\u035f', '\u0360', '\u0362', '\u0338',
        '\u0337', '\u0361', '\u0489'   
    ]
};
zalgomap.all = [].concat(zalgomap.up, zalgomap.down, zalgomap.mid);

// utils funcs
//---------------------------------------------------
//gets an int between 0 and max
function rand(max) {
    return Math.floor(Math.random() * max);
}
    //gets a random char from a zalgo char table
function getRandomFromArray(array) {
    return array[rand(array.length)];
}
function inArray(arr,obj) {
    return (arr.indexOf(obj) != -1);
}

var howfucked = {
    up: {
        none: function () { return 0; },
        mini: function () { return rand(8); },
        norm: function () { return rand(16) /2 +1; },
        maxi: function () { return rand(64) /4 +3; }
    },
    mid: { 
        none: function () { return 0; },
        mini: function () { return rand(2); },
        norm: function () { return rand(6)  /2; },
        maxi: function () { return rand(16) /4 +1; }
    },
    down: { 
        none: function () { return 0; },
        mini: function () { return rand(8); },
        norm: function () { return rand(16) /2 +1; },
        maxi: function () { return rand(64) /4 +3; }
    }
}

function fuck(input, fuckup, fuckmid, fuckdown) {
    if (typeof(fuckup)   ==='undefined') { fuckup   = "norm"; }
    if (typeof(fuckmid)  ==='undefined') { fuckmid  = "norm"; }
    if (typeof(fuckdown) ==='undefined') { fuckdown = "norm"; }

    var output = '';

    for (var x in input) {
        // Skip any character that we think is already a zalgo character
        if (inArray(zalgomap.all, input[x])) {
            continue;
        }
        thisChar = input[x];
        //console.log(thisChar);
        output += thisChar;

        var y;
        for (y=0; y < howfucked['up'][fuckup](); y++) {
            output += getRandomFromArray(zalgomap.up);
        }
        for (y=0; y < howfucked['mid'][fuckmid](); y++) {
            output += getRandomFromArray(zalgomap.mid);
        }
        for (y=0; y < howfucked['down'][fuckdown](); y++) {
            output += getRandomFromArray(zalgomap.down);
        }
    }

    return output;
}

console.log(fuck('asdf'));

// .load /Users/mrled/Documents/unicoed/zalgo.js
