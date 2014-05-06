from random import seed, randint, choice as randchoice

zalgoesup = [
    chr(int('030d',16)), chr(int('030e',16)), chr(int('0304',16)), chr(int('0305',16)),
    chr(int('033f',16)), chr(int('0311',16)), chr(int('0306',16)), chr(int('0310',16)),
    chr(int('0352',16)), chr(int('0357',16)), chr(int('0351',16)), chr(int('0307',16)),
    chr(int('0308',16)), chr(int('030a',16)), chr(int('0342',16)), chr(int('0343',16)),
    chr(int('0344',16)), chr(int('034a',16)), chr(int('034b',16)), chr(int('034c',16)),
    chr(int('0303',16)), chr(int('0302',16)), chr(int('030c',16)), chr(int('0350',16)),
    chr(int('0300',16)), chr(int('0301',16)), chr(int('030b',16)), chr(int('030f',16)), 
    chr(int('0312',16)), chr(int('0313',16)), chr(int('0314',16)), chr(int('033d',16)),
    chr(int('0309',16)), chr(int('0363',16)), chr(int('0364',16)), chr(int('0365',16)),
    chr(int('0366',16)), chr(int('0367',16)), chr(int('0368',16)), chr(int('0369',16)),
    chr(int('036a',16)), chr(int('036b',16)), chr(int('036c',16)), chr(int('036d',16)),
    chr(int('036e',16)), chr(int('036f',16)), chr(int('033e',16)), chr(int('035b',16)),
    chr(int('0346',16)), chr(int('031a',16))
]

zalgoesdown = [
    chr(int('0316',16)), chr(int('0317',16)), chr(int('0318',16)), chr(int('0319',16)),
    chr(int('031c',16)), chr(int('031d',16)), chr(int('031e',16)), chr(int('031f',16)),
    chr(int('0320',16)), chr(int('0324',16)), chr(int('0325',16)), chr(int('0326',16)),
    chr(int('0329',16)), chr(int('032a',16)), chr(int('032b',16)), chr(int('032c',16)),
    chr(int('032d',16)), chr(int('032e',16)), chr(int('032f',16)), chr(int('0330',16)),
    chr(int('0331',16)), chr(int('0332',16)), chr(int('0333',16)), chr(int('0339',16)),
    chr(int('033a',16)), chr(int('033b',16)), chr(int('033c',16)), chr(int('0345',16)),
    chr(int('0347',16)), chr(int('0348',16)), chr(int('0349',16)), chr(int('034d',16)),
    chr(int('034e',16)), chr(int('0353',16)), chr(int('0354',16)), chr(int('0355',16)),
    chr(int('0356',16)), chr(int('0359',16)), chr(int('035a',16)), chr(int('0323',16)) 
]

zalgoesnowhere = [
    chr(int('0315',16)), chr(int('031b',16)), chr(int('0340',16)), chr(int('0341',16)),
    chr(int('0358',16)), chr(int('0321',16)), chr(int('0322',16)), chr(int('0327',16)),
    chr(int('0328',16)), chr(int('0334',16)), chr(int('0335',16)), chr(int('0336',16)),
    chr(int('034f',16)), chr(int('035c',16)), chr(int('035d',16)), chr(int('035e',16)),
    chr(int('035f',16)), chr(int('0360',16)), chr(int('0362',16)), chr(int('0338',16)),
    chr(int('0337',16)), chr(int('0361',16)), chr(int('0489',16))
]

fuck = {
    'mini' : {
        'up'   : int(randint(0,8)), 
        'mid'  : int(randint(0,2)),
        'down' : int(randint(0,8))
    },
    'normal' : {
        'up'   : int(randint(0,16) /2 +1),
        'mid'  : int(randint(0,6)  /2),
        'down' : int(randint(0,16) /2 +1)
    },
    'maxi' : {
        'up'   : int(randint(0,64) /4 +3),
        'mid'  : int(randint(0,16) /4 +1),
        'down' : int(randint(0,64) /4 +3)
    }
}

def translate(inputtext, fuckuplevel='normal', fuckdownlevel='normal', fuckmidlevel='normal'):
    seed()
    outputtext = ""
    for c in list(inputtext):
        outputtext += c
        for x in range(fuck[fuckuplevel]['up']):
            outputtext += randchoice(zalgoesup)
        for x in range(fuck[fuckmidlevel]['mid']):
            outputtext += randchoice(zalgoesup)
        for x in range(fuck[fuckdownlevel]['down']):
            outputtext += randchoice(zalgoesup)

    return outputtext
