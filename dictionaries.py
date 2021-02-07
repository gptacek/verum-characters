sub_origins = {'krazax' : {'lowl','legi','peak','gree','forg','rang','mine'},
            'dolten' : {'nigh','grav','ward','blea','gamb','skit','fang','dark','fae'},
            'bloodwave bay' : {'mage','navi','spel','copp','ship','priv','brut','whis'},
            'the rift' : {'divi','luus','envu','prie','glat','grii','vrat','slog'},
            'steton' : {'bule','drag','floa','gian','mant','hide','roc','chim'},
            'daborak' : {'rive','band','dabo','stab','calv','cour','sold','plai'},
            'badlands' : {'wend','doom','bans','woef','twic'},
            'orde': {'pala','chur','inpl','expr','barr','wall','coin'},
            'khao': {'trac','mend','exil','drui','fora','dark','enfo'},
            'majital' : {'arca','merc','port','mira','guil','sand','oasi','ruin'}}

# order of list: [asi, speed, skill]

races = {'humans' : {'vari':[["choose2"], 30, ["choose1"]],'illi': ["none", 30, ["none"]]},
        'elves' : {'half':[['cha2','choose2'],30,["choose2"]],'high': [["dex2","int1"],30,[11]],'wood':[["dex2","wis1"],35,[11]],'dark':[["dex2","cha1"],30, [11]],'sea':[["dex2","con1"],30,[11]]},
        'gnomes' : {'fore': [["int2","dex1"], 25, ["none"]],'rock':[["int2","con1"], 25, ["none"]],'svir':[["int2","dex1"], 25, ["none"]]},
        'giant-kin' : {'firb': [["wis2","str1"], 30, ["none"]],'goli':[["str2","con1"], 30, [3]],'mino': [["str2","con1"], 30, [7]]},
        'skinwalker' : {'aara':[["dex2","wis1"], 25, ["none"]],'kits':[["wis2","choose1"], 30, [8]],'kenk':[["dex2","wis1"], 30, ["choose2"]],'taba':[["dex2","cha1"], 30, [11,16]],'tort': [["str2","wis1"], 30, [17]]},
        'dwarves' : {'moun': [["str2","con2"], 25, ['none']],'hill':[["con2","wis1"], 25, ['none']],'duer':[["con2","str1"], 25, ['none']]},
        'halflings' : {'ligh':[["dex2","cha1"], 25, ['none']],'stou': [["dex2","con1"], 25, ['none']],'song':[["cha2","dex1"], 25, [12]],'ghos':[["dex2","wis1"], 25, ['none']]},
        
        'greenskins' : {'half':[["str2","con1"], 30, [7]],'bugb':[["str2","dex1"], 30, [16]],'hobg':[["con2","int1"], 30, ["none"]],'orcs':[["str2","con1","int-2"], 30, [7]],'red':[["con2","str1"], 30, [7]],'gobl':[["dex2","con1"], 30, ["none"]]},
        'genasi' : {'eart':[["con2","str1"], 30, ["none"]],'wate':[["con2","wis1"], 30, ["none"]],'air':[["con2","dex1"], 30, ["none"]],'fire':[["con2","int1"], 30, ["none"]]},
        'tiefling' : {'asmo':[["cha2","int1"], 30, ["none"]],'baal':[["cha2","int1"], 30, ["none"]],'disp':[["cha2","dex1"], 30, ["none"]],'fier':[["cha2","wis1"], 30, ["none"]],'glas':[["cha2","dex1"], 30, ["none"]],'levi':[["cha2","con1"], 30, ["none"]],'mamm':[["cha2","int1"], 30, ["none"]],'meph':[["cha2","int1"], 30, ["none"]],'zari':[["cha2","str1"], 30, ["none"]]}, #can't do variant, too complicated ;w;
        'aasimar' : {'fall':[["cha2","str1"], 30, ["none"]],'prot':[["cha2","wis1"], 30, ["none"]],'scou':[["cha2","con1"], 30, ["none"]]},
        'lizardfolk' : {'yuan':[["cha2","int1"], 30, ["none"]],'kobo':[["dex2","str-2"], 30, ["none"]]},
        'fey' : {'chang':[["dex1","choose+2"], 30, [4]],'saty':[["cha2","choose1"], 30, ["none"]],'spri':[["dex2","cha1"], 20, ["none"]]},
        'other' : {'dham':[["choose+2","choose1"], 30, ["choose1"]],'reve':[["con4"], 30, ["none"]],'sire':[["cha2","choose1"], 30, [13]],'kuo':[["con2","choose1"], 30, ["none"]],'dra':[["cha1","str2"], 30, ["none"]],'tri':[["str1","con1","cha1"], 30, ["none"]]}}

gods = {'white' : {'vide','vavr','glor','rune','seve'},
        'grey' : {'iass','oun','ezok','kahe','wond','seke','matr','nero'},
        'green' : {'vins','inca','sill','lorn','gaze','gwai','talv'},
        'blue' : {'tilt','fala','cass','asta','raqu'},
        'black' : {'lori','olok','wode','baby','crow'}}