class c():
    title = '\x1b[1;32;40m'
    desc = '\x1b[1;37;40m'
    poor = '\x1b[1;31;40m'
    fair = '\x1b[1;33;40m'
    good = '\x1b[1;32;40m'
    great = '\x1b[1;36;40m'
    common = '\x1b[1;30;40m'
    uncommon = '\x1b[1;32;40m'
    rare = '\x1b[1;34;40m'
    epic = '\x1b[1;35;40m'
    legendary = '\x1b[1;36;40m'
    clear = '\x1b[0m'

class w():
    pre = ['Aa', 'Ae', 'Ai', 'Ao', 'Au', 'Ba', 'Be', 'Bi', 'Bo', 'Bu', 'Ca', 'Ce', 'Ci', 'Co', 'Cu', 'Da', 'De', 'Di', 'Do', 'Du', 'Ea', 'Ee', 'Ei', 'Eo', 'Eu', 'Fa', 'Fe', 'Fi', 'Fo', 'Fu', 'Ga', 'Ge', 'Gi', 'Go', 'Gu', 'Ha', 'Hi', 'He', 'Ho', 'Hu', 'Ia', 'Ie', 'Io', 'Ii', 'Iu', 'Ja', 'Je', 'Ji', 'Jo', 'Ju', 'Ka', 'Ke', 'Ki', 'Ko', 'Ku', 'La', 'Le', 'Li', 'Lo', 'Lu', 'Ma', 'Me', 'Mi', 'Mo', 'Mu', 'Na', 'Ni', 'Ne', 'No', 'Nu', 'Oa', 'Oe', 'Oi', 'Oo', 'Ou', 'Pa', 'Pe', 'Pi', 'Po', 'Pu', 'Qa', 'Qe', 'Qi', 'Qu', 'Qo', 'Ra', 'Re', 'Ri', 'Ro', 'Ru', 'Sa', 'Se', 'Si', 'So', 'Su', 'Ta', 'Te', 'Ti', 'To', 'Tu', 'Ua', 'Ue', 'Ui', 'Uo', 'Uu', 'Va', 'Ve', 'Vi', 'Vo', 'Vu', 'Wa', 'We', 'Wi', 'Wo', 'Wu', 'Xa', 'Xe', 'Xi', 'Xo', 'Xu', 'Za', 'Ze', 'Zi', 'Zo', 'Zu']
    suf = ['aer', 'ber', 'cer', 'der', 'eer', 'fer', 'ger', 'her', 'ier', 'jer', 'ker', 'ler', 'mer', 'ner', 'oer', 'per', 'qer', 'rer', 'ser', 'ter', 'uer', 'ver', 'wer', 'xer', 'yer', 'zer', 'aar', 'bar', 'car', 'dar', 'ear', 'far', 'gar', 'har', 'iar', 'jar', 'kar', 'lar', 'mar', 'nar', 'oar', 'par', 'qar', 'rar', 'sar', 'tar', 'uar', 'var', 'war', 'xar', 'yar', 'zar', 'air', 'bir', 'cir', 'dir', 'eir', 'fir', 'gir', 'hir', 'iir', 'jir', 'kir', 'lir', 'mir', 'nir', 'oir', 'pir', 'qir', 'rir', 'sir', 'tir', 'uir', 'vir', 'wir', 'xir', 'yir', 'zir', 'aor', 'bor', 'cor', 'dor', 'eor', 'for', 'gor', 'hor', 'ior', 'jor', 'kor', 'lor', 'mor', 'nor', 'oor', 'por', 'qor', 'ror', 'sor', 'tor', 'uor', 'vor', 'wor', 'xor', 'yor', 'zor', 'aur', 'bur', 'cur', 'dur', 'eur', 'fur', 'gur', 'hur', 'iur', 'jur', 'kur', 'lur', 'mur', 'nur', 'our', 'pur', 'qur', 'rur', 'sur', 'tur', 'uur', 'vur', 'wur', 'xur', 'yur', 'zur', 'aen', 'ben', 'cen', 'den', 'een', 'fen', 'gen', 'hen', 'ien', 'jen', 'ken', 'len', 'men', 'nen', 'oen', 'pen', 'qen', 'ren', 'sen', 'ten', 'uen', 'ven', 'wen', 'xen', 'yen', 'zen', 'aan', 'ban', 'can', 'dan', 'ean', 'fan', 'gan', 'han', 'ian', 'jan', 'kan', 'lan', 'man', 'nan', 'oan', 'pan', 'qan', 'ran', 'san', 'tan', 'uan', 'van', 'wan', 'xan', 'yan', 'zan', 'ain', 'bin', 'cin', 'din', 'ein', 'fin', 'gin', 'hin', 'iin', 'jin', 'kin', 'lin', 'min', 'nin', 'oin', 'pin', 'qin', 'rin', 'sin', 'tin', 'uin', 'vin', 'win', 'xin', 'yin', 'zin', 'aon', 'bon', 'con', 'don', 'eon', 'fon', 'gon', 'hon', 'ion', 'jon', 'kon', 'lon', 'mon', 'non', 'oon', 'pon', 'qon', 'ron', 'son', 'ton', 'uon', 'von', 'won', 'xon', 'yon', 'zon', 'aun', 'bun', 'cun', 'dun', 'eun', 'fun', 'gun', 'hun', 'iun', 'jun', 'kun', 'lun', 'mun', 'nun', 'oun', 'pun', 'qun', 'run', 'sun', 'tun', 'uun', 'vun', 'wun', 'xun', 'yun', 'zun', 'aek', 'bek', 'cek', 'dek', 'eek', 'fek', 'gek', 'hek', 'iek', 'jek', 'kek', 'lek', 'mek', 'nek', 'oek', 'pek', 'qek', 'rek', 'sek', 'tek', 'uek', 'vek', 'wek', 'xek', 'yek', 'zek', 'aak', 'bak', 'cak', 'dak', 'eak', 'fak', 'gak', 'hak', 'iak', 'jak', 'kak', 'lak', 'mak', 'nak', 'oak', 'pak', 'qak', 'rak', 'sak', 'tak', 'uak', 'vak', 'wak', 'xak', 'yak', 'zak', 'aik', 'bik', 'cik', 'dik', 'eik', 'fik', 'gik', 'hik', 'iik', 'jik', 'kik', 'lik', 'mik', 'nik', 'oik', 'pik', 'qik', 'rik', 'sik', 'tik', 'uik', 'vik', 'wik', 'xik', 'yik', 'zik', 'aok', 'bok', 'cok', 'dok', 'eok', 'fok', 'gok', 'hok', 'iok', 'jok', 'kok', 'lok', 'mok', 'nok', 'ook', 'pok', 'qok', 'rok', 'sok', 'tok', 'uok', 'vok', 'wok', 'xok', 'yok', 'zok', 'auk', 'buk', 'cuk', 'duk', 'euk', 'fuk', 'guk', 'huk', 'iuk', 'juk', 'kuk', 'luk', 'muk', 'nuk', 'ouk', 'puk', 'quk', 'ruk', 'suk', 'tuk', 'uuk', 'vuk', 'wuk', 'xuk', 'yuk', 'zuk', 'aeo', 'beo', 'ceo', 'deo', 'eeo', 'feo', 'geo', 'heo', 'ieo', 'jeo', 'keo', 'leo', 'meo', 'neo', 'oeo', 'peo', 'qeo', 'reo', 'seo', 'teo', 'ueo', 'veo', 'weo', 'xeo', 'yeo', 'zeo', 'aao', 'bao', 'cao', 'dao', 'eao', 'fao', 'gao', 'hao', 'iao', 'jao', 'kao', 'lao', 'mao', 'nao', 'oao', 'pao', 'qao', 'rao', 'sao', 'tao', 'uao', 'vao', 'wao', 'xao', 'yao', 'zao', 'aio', 'bio', 'cio', 'dio', 'eio', 'fio', 'gio', 'hio', 'iio', 'jio', 'kio', 'lio', 'mio', 'nio', 'oio', 'pio', 'qio', 'rio', 'sio', 'tio', 'uio', 'vio', 'wio', 'xio', 'yio', 'zio', 'aoo', 'boo', 'coo', 'doo', 'eoo', 'foo', 'goo', 'hoo', 'ioo', 'joo', 'koo', 'loo', 'moo', 'noo', 'ooo', 'poo', 'qoo', 'roo', 'soo', 'too', 'uoo', 'voo', 'woo', 'xoo', 'yoo', 'zoo', 'auo', 'buo', 'cuo', 'duo', 'euo', 'fuo', 'guo', 'huo', 'iuo', 'juo', 'kuo', 'luo', 'muo', 'nuo', 'ouo', 'puo', 'quo', 'ruo', 'suo', 'tuo', 'uuo', 'vuo', 'wuo', 'xuo', 'yuo', 'zuo', 'aez', 'bez', 'cez', 'dez', 'eez', 'fez', 'gez', 'hez', 'iez', 'jez', 'kez', 'lez', 'mez', 'nez', 'oez', 'pez', 'qez', 'rez', 'sez', 'tez', 'uez', 'vez', 'wez', 'xez', 'yez', 'zez', 'aaz', 'baz', 'caz', 'daz', 'eaz', 'faz', 'gaz', 'haz', 'iaz', 'jaz', 'kaz', 'laz', 'maz', 'naz', 'oaz', 'paz', 'qaz', 'raz', 'saz', 'taz', 'uaz', 'vaz', 'waz', 'xaz', 'yaz', 'zaz', 'aiz', 'biz', 'ciz', 'diz', 'eiz', 'fiz', 'giz', 'hiz', 'iiz', 'jiz', 'kiz', 'liz', 'miz', 'niz', 'oiz', 'piz', 'qiz', 'riz', 'siz', 'tiz', 'uiz', 'viz', 'wiz', 'xiz', 'yiz', 'ziz', 'aoz', 'boz', 'coz', 'doz', 'eoz', 'foz', 'goz', 'hoz', 'ioz', 'joz', 'koz', 'loz', 'moz', 'noz', 'ooz', 'poz', 'qoz', 'roz', 'soz', 'toz', 'uoz', 'voz', 'woz', 'xoz', 'yoz', 'zoz', 'auz', 'buz', 'cuz', 'duz', 'euz', 'fuz', 'guz', 'huz', 'iuz', 'juz', 'kuz', 'luz', 'muz', 'nuz', 'ouz', 'puz', 'quz', 'ruz', 'suz', 'tuz', 'uuz', 'vuz', 'wuz', 'xuz', 'yuz', 'zuz', 'aey', 'bey', 'cey', 'dey', 'eey', 'fey', 'gey', 'hey', 'iey', 'jey', 'key', 'ley', 'mey', 'ney', 'oey', 'pey', 'qey', 'rey', 'sey', 'tey', 'uey', 'vey', 'wey', 'xey', 'yey', 'zey', 'aay', 'bay', 'cay', 'day', 'eay', 'fay', 'gay', 'hay', 'iay', 'jay', 'kay', 'lay', 'may', 'nay', 'oay', 'pay', 'qay', 'ray', 'say', 'tay', 'uay', 'vay', 'way', 'xay', 'yay', 'zay', 'aiy', 'biy', 'ciy', 'diy', 'eiy', 'fiy', 'giy', 'hiy', 'iiy', 'jiy', 'kiy', 'liy', 'miy', 'niy', 'oiy', 'piy', 'qiy', 'riy', 'siy', 'tiy', 'uiy', 'viy', 'wiy', 'xiy', 'yiy', 'ziy', 'aoy', 'boy', 'coy', 'doy', 'eoy', 'foy', 'goy', 'hoy', 'ioy', 'joy', 'koy', 'loy', 'moy', 'noy', 'ooy', 'poy', 'qoy', 'roy', 'soy', 'toy', 'uoy', 'voy', 'woy', 'xoy', 'yoy', 'zoy', 'auy', 'buy', 'cuy', 'duy', 'euy', 'fuy', 'guy', 'huy', 'iuy', 'juy', 'kuy', 'luy', 'muy', 'nuy', 'ouy', 'puy', 'quy', 'ruy', 'suy', 'tuy', 'uuy', 'vuy', 'wuy', 'xuy', 'yuy', 'zuy', 'aea', 'bea', 'cea', 'dea', 'eea', 'fea', 'gea', 'hea', 'iea', 'jea', 'kea', 'lea', 'mea', 'nea', 'oea', 'pea', 'qea', 'rea', 'sea', 'tea', 'uea', 'vea', 'wea', 'xea', 'yea', 'zea', 'aaa', 'baa', 'caa', 'daa', 'eaa', 'faa', 'gaa', 'haa', 'iaa', 'jaa', 'kaa', 'laa', 'maa', 'naa', 'oaa', 'paa', 'qaa', 'raa', 'saa', 'taa', 'uaa', 'vaa', 'waa', 'xaa', 'yaa', 'zaa', 'aia', 'bia', 'cia', 'dia', 'eia', 'fia', 'gia', 'hia', 'iia', 'jia', 'kia', 'lia', 'mia', 'nia', 'oia', 'pia', 'qia', 'ria', 'sia', 'tia', 'uia', 'via', 'wia', 'xia', 'yia', 'zia', 'aoa', 'boa', 'coa', 'doa', 'eoa', 'foa', 'goa', 'hoa', 'ioa', 'joa', 'koa', 'loa', 'moa', 'noa', 'ooa', 'poa', 'qoa', 'roa', 'soa', 'toa', 'uoa', 'voa', 'woa', 'xoa', 'yoa', 'zoa', 'aua', 'bua', 'cua', 'dua', 'eua', 'fua', 'gua', 'hua', 'iua', 'jua', 'kua', 'lua', 'mua', 'nua', 'oua', 'pua', 'qua', 'rua', 'sua', 'tua', 'uua', 'vua', 'wua', 'xua', 'yua', 'zua', 'aed', 'bed', 'ced', 'ded', 'eed', 'fed', 'ged', 'hed', 'ied', 'jed', 'ked', 'led', 'med', 'ned', 'oed', 'ped', 'qed', 'red', 'sed', 'ted', 'ued', 'ved', 'wed', 'xed', 'yed', 'zed', 'aad', 'bad', 'cad', 'dad', 'ead', 'fad', 'gad', 'had', 'iad', 'jad', 'kad', 'lad', 'mad', 'nad', 'oad', 'pad', 'qad', 'rad', 'sad', 'tad', 'uad', 'vad', 'wad', 'xad', 'yad', 'zad', 'aid', 'bid', 'cid', 'did', 'eid', 'fid', 'gid', 'hid', 'iid', 'jid', 'kid', 'lid', 'mid', 'nid', 'oid', 'pid', 'qid', 'rid', 'sid', 'tid', 'uid', 'vid', 'wid', 'xid', 'yid', 'zid', 'aod', 'bod', 'cod', 'dod', 'eod', 'fod', 'god', 'hod', 'iod', 'jod', 'kod', 'lod', 'mod', 'nod', 'ood', 'pod', 'qod', 'rod', 'sod', 'tod', 'uod', 'vod', 'wod', 'xod', 'yod', 'zod', 'aud', 'bud', 'cud', 'dud', 'eud', 'fud', 'gud', 'hud', 'iud', 'jud', 'kud', 'lud', 'mud', 'nud', 'oud', 'pud', 'qud', 'rud', 'sud', 'tud', 'uud', 'vud', 'wud', 'xud', 'yud', 'zud', 'aeg', 'beg', 'ceg', 'deg', 'eeg', 'feg', 'geg', 'heg', 'ieg', 'jeg', 'keg', 'leg', 'meg', 'neg', 'oeg', 'peg', 'qeg', 'reg', 'seg', 'teg', 'ueg', 'veg', 'weg', 'xeg', 'yeg', 'zeg', 'aag', 'bag', 'cag', 'dag', 'eag', 'fag', 'gag', 'hag', 'iag', 'jag', 'kag', 'lag', 'mag', 'nag', 'oag', 'pag', 'qag', 'rag', 'sag', 'tag', 'uag', 'vag', 'wag', 'xag', 'yag', 'zag', 'aig', 'big', 'cig', 'dig', 'eig', 'fig', 'gig', 'hig', 'iig', 'jig', 'kig', 'lig', 'mig', 'nig', 'oig', 'pig', 'qig', 'rig', 'sig', 'tig', 'uig', 'vig', 'wig', 'xig', 'yig', 'zig', 'aog', 'bog', 'cog', 'dog', 'eog', 'fog', 'gog', 'hog', 'iog', 'jog', 'kog', 'log', 'mog', 'nog', 'oog', 'pog', 'qog', 'rog', 'sog', 'tog', 'uog', 'vog', 'wog', 'xog', 'yog', 'zog', 'aug', 'bug', 'cug', 'dug', 'eug', 'fug', 'gug', 'hug', 'iug', 'jug', 'kug', 'lug', 'mug', 'nug', 'oug', 'pug', 'qug', 'rug', 'sug', 'tug', 'uug', 'vug', 'wug', 'xug', 'yug', 'zug', 'aeh', 'beh', 'ceh', 'deh', 'eeh', 'feh', 'geh', 'heh', 'ieh', 'jeh', 'keh', 'leh', 'meh', 'neh', 'oeh', 'peh', 'qeh', 'reh', 'seh', 'teh', 'ueh', 'veh', 'weh', 'xeh', 'yeh', 'zeh', 'aah', 'bah', 'cah', 'dah', 'eah', 'fah', 'gah', 'hah', 'iah', 'jah', 'kah', 'lah', 'mah', 'nah', 'oah', 'pah', 'qah', 'rah', 'sah', 'tah', 'uah', 'vah', 'wah', 'xah', 'yah', 'zah', 'aih', 'bih', 'cih', 'dih', 'eih', 'fih', 'gih', 'hih', 'iih', 'jih', 'kih', 'lih', 'mih', 'nih', 'oih', 'pih', 'qih', 'rih', 'sih', 'tih', 'uih', 'vih', 'wih', 'xih', 'yih', 'zih', 'aoh', 'boh', 'coh', 'doh', 'eoh', 'foh', 'goh', 'hoh', 'ioh', 'joh', 'koh', 'loh', 'moh', 'noh', 'ooh', 'poh', 'qoh', 'roh', 'soh', 'toh', 'uoh', 'voh', 'woh', 'xoh', 'yoh', 'zoh', 'auh', 'buh', 'cuh', 'duh', 'euh', 'fuh', 'guh', 'huh', 'iuh', 'juh', 'kuh', 'luh', 'muh', 'nuh', 'ouh', 'puh', 'quh', 'ruh', 'suh', 'tuh', 'uuh', 'vuh', 'wuh', 'xuh', 'yuh', 'zuh', 'aej', 'bej', 'cej', 'dej', 'eej', 'fej', 'gej', 'hej', 'iej', 'jej', 'kej', 'lej', 'mej', 'nej', 'oej', 'pej', 'qej', 'rej', 'sej', 'tej', 'uej', 'vej', 'wej', 'xej', 'yej', 'zej', 'aaj', 'baj', 'caj', 'daj', 'eaj', 'faj', 'gaj', 'haj', 'iaj', 'jaj', 'kaj', 'laj', 'maj', 'naj', 'oaj', 'paj', 'qaj', 'raj', 'saj', 'taj', 'uaj', 'vaj', 'waj', 'xaj', 'yaj', 'zaj', 'aij', 'bij', 'cij', 'dij', 'eij', 'fij', 'gij', 'hij', 'iij', 'jij', 'kij', 'lij', 'mij', 'nij', 'oij', 'pij', 'qij', 'rij', 'sij', 'tij', 'uij', 'vij', 'wij', 'xij', 'yij', 'zij', 'aoj', 'boj', 'coj', 'doj', 'eoj', 'foj', 'goj', 'hoj', 'ioj', 'joj', 'koj', 'loj', 'moj', 'noj', 'ooj', 'poj', 'qoj', 'roj', 'soj', 'toj', 'uoj', 'voj', 'woj', 'xoj', 'yoj', 'zoj', 'auj', 'buj', 'cuj', 'duj', 'euj', 'fuj', 'guj', 'huj', 'iuj', 'juj', 'kuj', 'luj', 'muj', 'nuj', 'ouj', 'puj', 'quj', 'ruj', 'suj', 'tuj', 'uuj', 'vuj', 'wuj', 'xuj', 'yuj', 'zuj', 'aex', 'bex', 'cex', 'dex', 'eex', 'fex', 'gex', 'hex', 'iex', 'jex', 'kex', 'lex', 'mex', 'nex', 'oex', 'pex', 'qex', 'rex', 'sex', 'tex', 'uex', 'vex', 'wex', 'xex', 'yex', 'zex', 'aax', 'bax', 'cax', 'dax', 'eax', 'fax', 'gax', 'hax', 'iax', 'jax', 'kax', 'lax', 'max', 'nax', 'oax', 'pax', 'qax', 'rax', 'sax', 'tax', 'uax', 'vax', 'wax', 'xax', 'yax', 'zax', 'aix', 'bix', 'cix', 'dix', 'eix', 'fix', 'gix', 'hix', 'iix', 'jix', 'kix', 'lix', 'mix', 'nix', 'oix', 'pix', 'qix', 'rix', 'six', 'tix', 'uix', 'vix', 'wix', 'xix', 'yix', 'zix', 'aox', 'box', 'cox', 'dox', 'eox', 'fox', 'gox', 'hox', 'iox', 'jox', 'kox', 'lox', 'mox', 'nox', 'oox', 'pox', 'qox', 'rox', 'sox', 'tox', 'uox', 'vox', 'wox', 'xox', 'yox', 'zox', 'aux', 'bux', 'cux', 'dux', 'eux', 'fux', 'gux', 'hux', 'iux', 'jux', 'kux', 'lux', 'mux', 'nux', 'oux', 'pux', 'qux', 'rux', 'sux', 'tux', 'uux', 'vux', 'wux', 'xux', 'yux', 'zux']
    des = ['Ancient', 'Beautiful', 'Boring', 'Bustling', 'Charming', 'Contemporary', 'Compact', 'Crowded', 'Exciting', 'Expensive', 'Fantastic', 'Elaborate', 'Fascinating', 'Huge', 'Lively', 'Popular', 'Polluted', 'Squalid', 'Destitute', 'War-torn', 'Fortified', 'Haunted', 'Pillaged', 'Cursed', 'Mysterious', 'Dangerous']
    tit = ['the Jewel of the East', 'the Jewel of the North', 'the Jewel of the South', 'the Jewel of the West', 'the Walled-City', 'the City of the Damned', 'the Jungle Heart', 'the Forest Heart', 'the Heart of the Sea', 'of the Merchant Coast', 'the Realm of Shadow', 'the Lions Pride', 'the Titans Forge', 'the Land of Peace'] 
    mar = ['Fishing', 'Herding', 'Smithing', 'Mining', 'Alchemy', 'Lodging', 'Trade', 'Armaments', 'Mercenary Work', 'Dungeoneering', 'Herb Gathering', 'Sea Trade', 'Piracy', 'Raiding', 'Brothels', 'Gambling', 'Contraband', 'Black Market', 'Slaving', 'Farming', 'Masonry', 'Armor Smithing', 'Weapon Smithing', 'Hunting', 'Sanctuary']
    gov = ['Unitary State', 'Federation', 'Confederation', 'Anarchy', 'Democracy', 'Oligarchy', 'Autocracy', 'Peoples Republic', 'Aristocracy', 'Plutocracy', 'Kraterocracy', 'Stratocracy', 'Timocracy', 'Meritocracy', 'Technocracy', 'Geniocracy', 'Noocracy', 'Theocracy', 'Kritarchy', 'Particracy', 'Ergatocracy', 'Netocracy', 'Civilian Dictatorship', 'Military Dictatorship', 'Tribalism', 'Monarchism', 'Despotism', 'Feudalism', 'Capitalism', 'Socialism', 'Communism', 'Totalitarianism', 'City-State', 'Commune', 'Colony', 'Alliance', 'Empire', 'Commonwealth']
    cri = [c.poor + 'High' + c.clear, c.fair + 'Medium' + c.clear, c.good + 'Low' + c.clear]
    rel1 = ['God', 'Lord', 'Deva', 'King', 'Queen', 'Father', 'Mother', 'Essence', 'Embodiment', 'Aspect', 'Demigod', 'Avatar', 'Bhodisattva', 'Keeper', 'Khan', 'Spirit']
    rel2 = ['Death', 'Life', 'Darkness', 'Righteousness', 'Vengeance', 'Passion', 'Lust', 'Greed', 'Power', 'Fire', 'Ice', 'Water', 'Mist', 'Stars', 'Light', 'Shadows', 'Revenge', 'Battle', 'War', 'Bloodlust', 'Blood', 'Bone', 'Flesh', 'Stone', 'Earth', 'Lighting', 'Thunder', 'Rain']
    rac = ['Human', 'Orc', 'Elf', 'Halfling', 'Goblin', 'Dwarf', 'Half-Orc', 'Half-Elf', 'Half-Fiend', 'Gnome']
    cla = ['Warlord', 'Fighter', 'Thief', 'Pirate', 'Ninja', 'Mage', 'Wizard', 'Acolyte', 'Priest', 'Blacksmith', 'Hunter', 'Monk', 'Warlock', 'Bard', 'Druid', 'Paladin', 'Fisherman', 'Merchant', 'Alchemist', 'Wanderer', 'City Guard', 'Knight', 'Noble', 'Maester', 'Innkeeper', 'Fortune Teller', 'Mystic', 'Sorceror', 'Barbarian', 'Savage', 'Cannibal', 'Brothel Worker', 'Brothel Owner', 'Streetwalker', 'Slave', 'Captain', 'Ferryman', 'Beggar', 'Drunkard', 'Maniac', 'Criminal', 'Thug', 'Commoner', 'Civilian', 'Farmer', 'Carpenter', 'Ship Builder', 'Sailor', 'Guard Captain', 'Lich', 'Werewolf', 'Vampire', 'Lorekeeper', 'Librarian', 'Magician', 'Prophet', 'Psychic', 'Apothecary', 'Grave Digger', 'Pallbearer', 'Doctor', 'Physician', 'Healer', 'Cleric', 'Armorer', 'Weaponsmith', 'Pugilist', 'Mercenary', 'Sell Sword', 'Traveler', 'Street Urchin', 'Refugee', 'Pilgrim' ]
    rar = [c.common, c.uncommon, c.rare, c.epic, c.legendary]
    rum = []
    mon = []
    arm = []
    wep = []
    hos = [c.poor + 'Hostile' + c.clear, c.fair + 'Aggressive' + c.clear, c.good + 'Passive' + c.clear]
    pot = []
    tom = []
    dun = []
    # Strange Crimes for City/Village/Town
    vic = ['A group of travelers lead by a', 'A caravan lead by a', 'An adventuring party lead by a', 'A group of pilgrims following a', 'A young', 'An old', 'A down on his luck', 'A common', 'A few', 'A hated', 'Another', 'A middle aged', 'The family of a', 'The friend of a', 'A strange', 'A famous', 'A well liked', 'A simple dressed', 'An extravagantly dressed', 'A commonly dressed', 'A down on her luck']
    vic2 = ['local', 'foreign', 'exotic looking']
    vic3 = ['man', 'woman', 'craftsman', 'guard', 'noble', 'slave', 'servant', 'child', 'lord', 'mage', 'priest', 'merchant', 'thief', 'assassin', 'officer', 'hobo', 'streetwalker', 'criminal', 'art', 'collector', 'archivist']
    # 'have been...'
    vic4 = ['killed', 'robbed', 'kidnapped', 'extorted', 'blackmailed', 'attacked', 'eaten', 'decapitated', 'mutilated', 'assaulted', 'taken hostage', 'banished to another plane', 'blown up', 'set on fire', 'polymorphed', 'fed to wild animals', 'thrown into a pit', 'tricked', 'cloned', 'shrunk']
    # location
    vic5 = ['at home', 'in the street in broad daylight in a dark alley', 'in a tavern', 'at a brothel', 'on the outskirts of town', 'in the park', 'in someone’s garden', 'in a temple', 'on the town square', 'down by the lake', 'the swamp', 'in the nearby ruin', 'in a nearby cave', 'by the sewer exit', 'in a guard tower', 'in an abandoned house', 'in an abandoned warehouse', 'in an old mansion', 'in the stable of an old estate', 'in the greenhouse of an old mansion', 'in a crypt', 'in a library', 'at the victims own place of work', 'in the victims own bedroom', 'in a hidden room in the victims own house', 'in the common room of a local guild', 'on a boat on the lake', 'on a quiet mountain road', 'on a track in the woods', 'out by the waterfall', 'in the cathedral', 'in the old church', 'in the catacombs', 'at an undisclosed location']
    # circumstances
    vic6 = ['to no real surprise to the local population.', 'under obviously mysterious circumstances.', 'causing great unrest among the local population.', 'like several similar victims before.', 'without getting any real attention from the local population.', 'and the remnants of dark magic is still draining all light from the spot.', 'and the local population hasn’t spokena word since.', 'and the town is now under curfew.', 'and people believe it to be politically motivated.', 'as it happens every month.']
    # 'the case is being handled by...'
    vic7 = ['the city guard', 'royal guard', 'a fearsome crew with obvious scars of battle', 'a strange and quiet group, not known by any of the locals', 'men of the church', 'an old man in a robe and his dog', 'a middle aged woman in a simple uniform with her young male assistant', 'a young man, who will not disclose his relationship to the victim assisted by his mute brother']
    # 'and are .. on solving it'
    vic8 = ['keen on', 'not very interested in', 'doing all they can in', 'letting no one stand in their way of', 'not doing so much for', 'clearly making sure nothing is done in']
    # 'and are .. to share details'
    vic9 = ['are hostile when asked', 'are in no way willing', 'are very skeptical', 'are scared', 'are clearly not allowed', 'are, when completely hammered, somewhat willing',' skeptical, but somewhat willing', 'somewhat willing', 'willing', 'very willing', 'way too willing', 'telling everyone trying']
    # source
    vic10 = ['According to your sources on the local tavern, there is', 'A less reputable local paper writes about', 'A scrawny town crier tell passersby of', 'A group of craftsmen walking by talks about', 'According to the flyers distributed in quite overwhelming numbers around town, there is definitely', 'A man without teeth comes up and whispers to you', 'By the gate, a hideously deformed man passes you a note mentioning', 'At the scene of the crime is a verse from a poem, written with intestines laid out in beautiful cursive - it has', 'A note on your bed speaks of', 'You have heard the victim scream something, when the crime took place, that hinted at']
    # 'a connection to...'
    vic11 = ['a local cult with rather extreme beliefs.', 'a lock of strange fur.', 'a rumored jealous lover.', 'a hot tempered spouse.', 'the local child, the one with the strangest eyes.', 'markings of something having entered from beyond.', 'remnants of the darkest magic.', 'revenge.', 'lust.', 'greed.', 'a murky acquaintance from the victim’s past.', 'that old tablet covered in obscure symbols.', 'the terrible story no one wants to remember.', 'an old friend of yours.', 'a beautiful young woman, who only came to town recently.', 'another horrid crime committed not long ago.', 'the escaped criminal, rumored to be in hiding nearby.', 'markings of a wild animal.', 'that deep rumble, that you might hear coming from below the surface of the paved roads from time to time.']
