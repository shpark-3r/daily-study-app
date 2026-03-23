"""Daily study content generator for 5 subjects."""

import hashlib
from datetime import date


def _day_index(d: date, pool_size: int, subject: str) -> int:
    """Deterministic daily index based on date + subject."""
    seed = f"{d.isoformat()}-{subject}"
    h = int(hashlib.md5(seed.encode()).hexdigest(), 16)
    return h % pool_size


GERMAN = [
    {"title": "독일어 인사 표현", "content": "Guten Morgen (좋은 아침) / Guten Tag (안녕하세요) / Guten Abend (좋은 저녁) / Auf Wiedersehen (안녕히 가세요) / Tschüss (잘 가)"},
    {"title": "독일어 자기소개", "content": "Ich heiße... (제 이름은...) / Ich komme aus... (저는 ...에서 왔습니다) / Ich bin ... Jahre alt (저는 ...살입니다) / Freut mich (반갑습니다)"},
    {"title": "독일어 숫자 1-20", "content": "eins, zwei, drei, vier, fünf, sechs, sieben, acht, neun, zehn, elf, zwölf, dreizehn, vierzehn, fünfzehn, sechzehn, siebzehn, achtzehn, neunzehn, zwanzig"},
    {"title": "독일어 요일", "content": "Montag(월) / Dienstag(화) / Mittwoch(수) / Donnerstag(목) / Freitag(금) / Samstag(토) / Sonntag(일)"},
    {"title": "독일어 색깔", "content": "rot(빨강) / blau(파랑) / grün(초록) / gelb(노랑) / schwarz(검정) / weiß(하양) / grau(회색) / braun(갈색)"},
    {"title": "독일어 동사 변화 - sein", "content": "ich bin / du bist / er ist / wir sind / ihr seid / sie sind (영어 be동사에 해당)"},
    {"title": "독일어 동사 변화 - haben", "content": "ich habe / du hast / er hat / wir haben / ihr habt / sie haben (영어 have에 해당)"},
    {"title": "독일어 관사 (정관사)", "content": "남성: der / 여성: die / 중성: das / 복수: die — 예: der Mann, die Frau, das Kind"},
    {"title": "독일어 음식 어휘", "content": "Brot(빵) / Käse(치즈) / Wurst(소시지) / Apfel(사과) / Wasser(물) / Bier(맥주) / Kaffee(커피)"},
    {"title": "독일어 질문 표현", "content": "Was? (무엇?) / Wer? (누구?) / Wo? (어디?) / Wann? (언제?) / Warum? (왜?) / Wie? (어떻게?) / Wie viel? (얼마나?)"},
    {"title": "독일어 가족 어휘", "content": "Vater(아버지) / Mutter(어머니) / Bruder(형제) / Schwester(자매) / Sohn(아들) / Tochter(딸) / Großvater(할아버지)"},
    {"title": "독일어 전치사 (장소)", "content": "in(안에) / auf(위에) / unter(아래에) / neben(옆에) / vor(앞에) / hinter(뒤에) / zwischen(사이에)"},
    {"title": "독일어 일상 동사", "content": "gehen(가다) / kommen(오다) / machen(만들다) / sehen(보다) / essen(먹다) / trinken(마시다) / schlafen(자다)"},
    {"title": "독일어 형용사", "content": "groß(큰) / klein(작은) / gut(좋은) / schlecht(나쁜) / schön(아름다운) / alt(오래된) / neu(새로운) / schnell(빠른)"},
    {"title": "독일어 날씨 표현", "content": "Es ist warm(따뜻하다) / Es ist kalt(춥다) / Es regnet(비가 온다) / Es schneit(눈이 온다) / Die Sonne scheint(해가 빛난다)"},
    {"title": "독일어 시간 표현", "content": "Wie spät ist es? (몇 시입니까?) / Es ist drei Uhr (3시입니다) / halb vier (3시 반) / Viertel nach/vor (15분 후/전)"},
    {"title": "독일어 교통수단", "content": "Auto(자동차) / Bus(버스) / Zug(기차) / Fahrrad(자전거) / Flugzeug(비행기) / U-Bahn(지하철) / Straßenbahn(트램)"},
    {"title": "독일어 감정 표현", "content": "glücklich(행복한) / traurig(슬픈) / müde(피곤한) / wütend(화난) / überrascht(놀란) / nervös(긴장된)"},
    {"title": "독일어 쇼핑 표현", "content": "Wie viel kostet das? (이거 얼마예요?) / Ich möchte... (저는 ...을 원합니다) / Die Rechnung bitte (계산서 주세요)"},
    {"title": "독일어 월 이름", "content": "Januar, Februar, März, April, Mai, Juni, Juli, August, September, Oktober, November, Dezember"},
    {"title": "독일어 부정관사", "content": "남성: ein / 여성: eine / 중성: ein — 부정: kein/keine/kein — 예: ein Hund, eine Katze, kein Problem"},
    {"title": "독일어 분리동사", "content": "aufstehen(일어나다): Ich stehe auf / einkaufen(쇼핑하다): Ich kaufe ein / anfangen(시작하다): Ich fange an"},
    {"title": "독일어 재귀동사", "content": "sich freuen(기뻐하다) / sich setzen(앉다) / sich waschen(씻다) / sich fühlen(느끼다)"},
    {"title": "독일어 접속사", "content": "und(그리고) / aber(하지만) / oder(또는) / weil(왜냐하면) / dass(~라는 것) / wenn(만약/~할 때)"},
    {"title": "독일어 신체 부위", "content": "Kopf(머리) / Auge(눈) / Nase(코) / Mund(입) / Ohr(귀) / Hand(손) / Fuß(발) / Herz(심장)"},
    {"title": "독일어 직업 어휘", "content": "Arzt(의사) / Lehrer(교사) / Ingenieur(엔지니어) / Student(학생) / Koch(요리사) / Polizist(경찰관)"},
    {"title": "독일어 비교급/최상급", "content": "schnell → schneller → am schnellsten / gut → besser → am besten / groß → größer → am größten"},
    {"title": "독일어 과거형 (현재완료)", "content": "Ich habe gegessen(먹었다) / Ich bin gegangen(갔다) / haben/sein + 과거분사 형태"},
    {"title": "독일어 방향/위치", "content": "links(왼쪽) / rechts(오른쪽) / geradeaus(직진) / oben(위) / unten(아래) / hier(여기) / dort(저기)"},
    {"title": "독일어 계절과 자연", "content": "Frühling(봄) / Sommer(여름) / Herbst(가을) / Winter(겨울) / Baum(나무) / Blume(꽃) / Berg(산) / See(호수)"},
]

JAPANESE = [
    {"title": "일본어 히라가나 あ행", "content": "あ(a) い(i) う(u) え(e) お(o) — 일본어의 가장 기본 문자입니다"},
    {"title": "일본어 히라가나 か행", "content": "か(ka) き(ki) く(ku) け(ke) こ(ko) — 가행 발음 연습"},
    {"title": "일본어 히라가나 さ행", "content": "さ(sa) し(shi) す(su) せ(se) そ(so) — し는 si가 아닌 shi 발음"},
    {"title": "일본어 히라가나 た행", "content": "た(ta) ち(chi) つ(tsu) て(te) と(to) — ち는 chi, つ는 tsu 주의"},
    {"title": "일본어 히라가나 な행", "content": "な(na) に(ni) ぬ(nu) ね(ne) の(no) — の는 ~의 조사로도 사용"},
    {"title": "일본어 인사말", "content": "おはようございます(좋은 아침) / こんにちは(안녕하세요) / こんばんは(좋은 저녁) / さようなら(안녕히)"},
    {"title": "일본어 자기소개", "content": "はじめまして(처음 뵙겠습니다) / 私は...です(저는 ...입니다) / よろしくお願いします(잘 부탁드립니다)"},
    {"title": "일본어 숫자 1-10", "content": "一(いち) 二(に) 三(さん) 四(し/よん) 五(ご) 六(ろく) 七(しち/なな) 八(はち) 九(きゅう) 十(じゅう)"},
    {"title": "일본어 요일", "content": "月曜日(げつようび) 火曜日(かようび) 水曜日(すいようび) 木曜日(もくようび) 金曜日(きんようび) 土曜日(どようび) 日曜日(にちようび)"},
    {"title": "일본어 기본 동사", "content": "食べる(たべる・먹다) / 飲む(のむ・마시다) / 行く(いく・가다) / 来る(くる・오다) / 見る(みる・보다)"},
    {"title": "일본어 형용사 (い형)", "content": "大きい(おおきい・큰) / 小さい(ちいさい・작은) / 高い(たかい・높은/비싼) / 安い(やすい・싼) / おいしい(맛있는)"},
    {"title": "일본어 형용사 (な형)", "content": "きれい(な)(예쁜) / 静か(しずか)(な)(조용한) / 元気(げんき)(な)(건강한) / 好き(すき)(な)(좋아하는)"},
    {"title": "일본어 카타카나 ア행", "content": "ア(a) イ(i) ウ(u) エ(e) オ(o) — 외래어 표기에 사용"},
    {"title": "일본어 가족 호칭", "content": "お父さん(아버지) / お母さん(어머니) / 兄(あに・형/오빠) / 姉(あね・누나/언니) / 弟(おとうと) / 妹(いもうと)"},
    {"title": "일본어 조사 기초", "content": "は(~은/는) / が(~이/가) / を(~을/를) / に(~에) / で(~에서) / の(~의) / と(~와/과)"},
    {"title": "일본어 시간 표현", "content": "今(いま・지금) / 今日(きょう・오늘) / 明日(あした・내일) / 昨日(きのう・어제) / 毎日(まいにち・매일)"},
    {"title": "일본어 위치 표현", "content": "上(うえ・위) / 下(した・아래) / 右(みぎ・오른쪽) / 左(ひだり・왼쪽) / 前(まえ・앞) / 後ろ(うしろ・뒤)"},
    {"title": "일본어 색깔", "content": "赤(あか・빨강) / 青(あお・파랑) / 白(しろ・하양) / 黒(くろ・검정) / 緑(みどり・초록) / 黄色(きいろ・노랑)"},
    {"title": "일본어 음식 어휘", "content": "ご飯(ごはん・밥) / パン(빵) / 肉(にく・고기) / 魚(さかな・생선) / 野菜(やさい・채소) / 水(みず・물)"},
    {"title": "일본어 교통수단", "content": "電車(でんしゃ・전철) / バス(버스) / 車(くるま・자동차) / 自転車(じてんしゃ・자전거) / 飛行機(ひこうき・비행기)"},
    {"title": "일본어 て형 활용", "content": "食べて(먹어서) / 飲んで(마셔서) / 行って(가서) / して(해서) — て형은 연결, 요청에 사용"},
    {"title": "일본어 ます형", "content": "食べます(먹습니다) / 飲みます(마십니다) / 行きます(갑니다) — 정중체 표현"},
    {"title": "일본어 감정 표현", "content": "嬉しい(うれしい・기쁜) / 悲しい(かなしい・슬픈) / 怖い(こわい・무서운) / 楽しい(たのしい・즐거운)"},
    {"title": "일본어 계절", "content": "春(はる・봄) / 夏(なつ・여름) / 秋(あき・가을) / 冬(ふゆ・겨울) — 日本は四季がはっきりしています"},
    {"title": "일본어 쇼핑 표현", "content": "いくらですか(얼마입니까?) / これをください(이것 주세요) / 大きいサイズはありますか(큰 사이즈 있나요?)"},
    {"title": "일본어 N5 한자 (1)", "content": "日(ひ/にち・날) / 月(つき/げつ・달) / 火(ひ/か・불) / 水(みず/すい・물) / 木(き/もく・나무)"},
    {"title": "일본어 N5 한자 (2)", "content": "金(かね/きん・금/돈) / 土(つち/ど・흙) / 人(ひと/じん・사람) / 大(おお/だい・큰) / 小(ちい/しょう・작은)"},
    {"title": "일본어 존경어 기초", "content": "いらっしゃる(いる/行く의 존경어) / おっしゃる(言う의 존경어) / 召し上がる(食べる의 존경어)"},
    {"title": "일본어 접속 표현", "content": "そして(그리고) / でも(하지만) / だから(그래서) / それから(그 다음에) / しかし(그러나)"},
    {"title": "일본어 날씨 표현", "content": "天気(てんき・날씨) / 晴れ(はれ・맑음) / 雨(あめ・비) / 雪(ゆき・눈) / 風(かぜ・바람) / 暑い(あつい・덥다) / 寒い(さむい・춥다)"},
]

ENGLISH = [
    {"title": "영어 구동사 (Phrasal Verbs) #1", "content": "look up (찾아보다) / give up (포기하다) / put off (미루다) / turn down (거절하다) / figure out (알아내다)"},
    {"title": "영어 구동사 (Phrasal Verbs) #2", "content": "bring up (화제를 꺼내다) / run into (우연히 만나다) / come across (발견하다) / break down (고장나다) / take over (인수하다)"},
    {"title": "영어 혼동 단어 #1", "content": "affect(영향주다) vs effect(효과) / complement(보완) vs compliment(칭찬) / principal(주된) vs principle(원칙)"},
    {"title": "영어 혼동 단어 #2", "content": "lay(놓다) vs lie(눕다) / raise(올리다) vs rise(오르다) / advise(조언하다-동사) vs advice(조언-명사)"},
    {"title": "영어 비즈니스 이메일 표현", "content": "I'm writing to inquire about... / Please find attached... / I look forward to hearing from you / Don't hesitate to contact me"},
    {"title": "영어 시제 - 현재완료 vs 과거", "content": "I have lived here for 5 years (지금도 살고 있음) vs I lived there for 5 years (더 이상 안 살음) — 현재와의 연결 유무가 핵심"},
    {"title": "영어 관계대명사", "content": "who(사람 주격) / whom(사람 목적격) / which(사물) / that(사람/사물) / whose(소유격) — The man who called is my boss."},
    {"title": "영어 가정법", "content": "If I were you, I would... (현재 반대 가정) / If I had known, I would have... (과거 반대 가정) — were/had + would 패턴"},
    {"title": "영어 접두사", "content": "un-(반대: unhappy) / re-(다시: redo) / pre-(미리: preview) / mis-(잘못: misunderstand) / over-(과도: overwork)"},
    {"title": "영어 접미사", "content": "-ful(가득한: helpful) / -less(없는: careless) / -ment(명사화: development) / -tion(명사화: education) / -able(가능한: readable)"},
    {"title": "영어 관용표현 #1", "content": "a piece of cake (매우 쉬운) / break the ice (분위기를 풀다) / hit the nail on the head (정확히 맞추다) / once in a blue moon (매우 드물게)"},
    {"title": "영어 관용표현 #2", "content": "burn the midnight oil (밤늦게까지 일하다) / bite the bullet (어려운 결정을 하다) / cost an arm and a leg (매우 비싸다)"},
    {"title": "영어 전치사 - at/on/in (시간)", "content": "at + 시각(at 3pm) / on + 요일/날짜(on Monday) / in + 월/년/계절(in March, in 2024) — 작은 단위→큰 단위"},
    {"title": "영어 전치사 - at/on/in (장소)", "content": "at + 지점(at the station) / on + 표면(on the table) / in + 공간 안(in the room) — 점→면→공간"},
    {"title": "영어 수동태", "content": "능동: They built the house → 수동: The house was built (by them) — be + 과거분사, 행위자보다 대상이 중요할 때"},
    {"title": "영어 직접/간접 화법", "content": "직접: He said, \"I am tired.\" / 간접: He said that he was tired. — 시제 한 단계 후퇴 (am→was)"},
    {"title": "영어 TOEIC 필수 어휘 #1", "content": "implement(실행하다) / deadline(마감) / approximately(대략) / accommodate(수용하다) / mandatory(필수의)"},
    {"title": "영어 TOEIC 필수 어휘 #2", "content": "revenue(수익) / negotiate(협상하다) / confidential(기밀의) / comply(준수하다) / subsequent(이후의)"},
    {"title": "영어 연결어 (Transition Words)", "content": "However(그러나) / Moreover(더욱이) / Therefore(그러므로) / Nevertheless(그럼에도) / Furthermore(게다가) / In addition(추가로)"},
    {"title": "영어 조동사 뉘앙스", "content": "must(~해야 한다, 강한 의무) / should(~해야 한다, 조언) / might(~일 수도, 약한 가능성) / could(~할 수도, 능력/가능성)"},
    {"title": "영어 to부정사 vs 동명사", "content": "want/hope/decide + to V / enjoy/avoid/consider + V-ing / stop to V(~하기 위해 멈추다) vs stop V-ing(~하는 것을 멈추다)"},
    {"title": "영어 비교급/최상급", "content": "tall→taller→tallest / beautiful→more beautiful→most beautiful / good→better→best / bad→worse→worst"},
    {"title": "영어 분사구문", "content": "Walking down the street, I saw him. (길을 걷다가 그를 보았다) — 주어 같을 때 접속사+주어 생략, 동사를 -ing로"},
    {"title": "영어 강조구문", "content": "It is ... that ~ (강조): It was John that broke the window. / do/does/did 강조: I do understand."},
    {"title": "영어 콜로케이션", "content": "make a decision (결정하다) / take a break (쉬다) / do homework (숙제하다) / have a meeting (회의하다) / pay attention (주의를 기울이다)"},
    {"title": "영어 발음 규칙", "content": "gh는 묵음(night, though) 또는 f발음(enough, laugh) / kn의 k묵음(know, knife) / wr의 w묵음(write, wrong)"},
    {"title": "영어 반의어 쌍", "content": "abundant↔scarce / ancient↔modern / bold↔timid / conceal↔reveal / expand↔contract / generous↔stingy"},
    {"title": "영어 동의어 그룹", "content": "big = large = enormous = huge = immense / small = tiny = minute = miniature / happy = glad = delighted = thrilled"},
    {"title": "영어 조건문 정리", "content": "Type 0: If water boils, it evaporates (사실) / Type 1: If it rains, I'll stay (가능) / Type 2: If I were rich (비현실) / Type 3: If I had known (과거 비현실)"},
    {"title": "영어 문장 부호 사용법", "content": "세미콜론(;): 관련된 독립절 연결 / 콜론(:): 목록이나 설명 도입 / 대시(—): 부연 설명 / 아포스트로피('): 소유격, 축약"},
]

CHINESE = [
    {"title": "중국어 성조 연습", "content": "1성(ˉ 높고 평평): māmā / 2성(ˊ 올라감): máfan / 3성(ˇ 내렸다 올림): mǎ / 4성(ˋ 내려감): mà — 妈麻马骂"},
    {"title": "중국어 인사 표현", "content": "你好(nǐ hǎo·안녕) / 谢谢(xiè xie·감사) / 对不起(duì bu qǐ·미안) / 没关系(méi guān xi·괜찮아) / 再见(zài jiàn·안녕히)"},
    {"title": "중국어 자기소개", "content": "我叫...(wǒ jiào·제 이름은) / 我是韩国人(wǒ shì hánguó rén·한국인입니다) / 认识你很高兴(rèn shi nǐ hěn gāo xìng·반갑습니다)"},
    {"title": "중국어 숫자 1-10", "content": "一(yī) 二(èr) 三(sān) 四(sì) 五(wǔ) 六(liù) 七(qī) 八(bā) 九(jiǔ) 十(shí)"},
    {"title": "중국어 요일", "content": "星期一(xīngqī yī·월) / 星期二(화) / 星期三(수) / 星期四(목) / 星期五(금) / 星期六(토) / 星期天(일)"},
    {"title": "중국어 기본 동사", "content": "吃(chī·먹다) / 喝(hē·마시다) / 去(qù·가다) / 来(lái·오다) / 看(kàn·보다) / 说(shuō·말하다) / 做(zuò·하다)"},
    {"title": "중국어 가족 호칭", "content": "爸爸(bàba·아빠) / 妈妈(māma·엄마) / 哥哥(gēge·형) / 姐姐(jiějie·언니) / 弟弟(dìdi·남동생) / 妹妹(mèimei·여동생)"},
    {"title": "중국어 의문사", "content": "什么(shénme·무엇) / 谁(shéi·누구) / 哪里(nǎlǐ·어디) / 什么时候(shénme shíhou·언제) / 为什么(wèishénme·왜) / 怎么(zěnme·어떻게)"},
    {"title": "중국어 양사 (量词)", "content": "个(gè·일반) / 本(běn·책) / 杯(bēi·잔) / 件(jiàn·옷/사건) / 只(zhī·동물) — 숫자와 명사 사이에 필수"},
    {"title": "중국어 시간 표현", "content": "现在(xiànzài·지금) / 今天(jīntiān·오늘) / 明天(míngtiān·내일) / 昨天(zuótiān·어제) / 几点(jǐ diǎn·몇 시)"},
    {"title": "중국어 위치 표현", "content": "上面(shàngmiàn·위) / 下面(xiàmiàn·아래) / 里面(lǐmiàn·안) / 外面(wàimiàn·밖) / 前面(qiánmiàn·앞) / 后面(hòumiàn·뒤)"},
    {"title": "중국어 색깔", "content": "红色(hóngsè·빨강) / 蓝色(lánsè·파랑) / 绿色(lǜsè·초록) / 黄色(huángsè·노랑) / 白色(báisè·하양) / 黑色(hēisè·검정)"},
    {"title": "중국어 음식 주문", "content": "菜单(càidān·메뉴) / 我要这个(wǒ yào zhège·이거 주세요) / 多少钱(duōshao qián·얼마) / 买单(mǎidān·계산)"},
    {"title": "중국어 교통수단", "content": "公共汽车(gōnggòng qìchē·버스) / 地铁(dìtiě·지하철) / 出租车(chūzū chē·택시) / 火车(huǒchē·기차) / 飞机(fēijī·비행기)"},
    {"title": "중국어 형용사", "content": "大(dà·큰) / 小(xiǎo·작은) / 多(duō·많은) / 少(shǎo·적은) / 好(hǎo·좋은) / 快(kuài·빠른) / 慢(màn·느린)"},
    {"title": "중국어 了 용법", "content": "동작 완료: 我吃了(먹었다) / 변화: 天气冷了(추워졌다) — 了는 '완료'와 '변화' 두 가지 핵심 용법"},
    {"title": "중국어 把 구문", "content": "把 + 목적어 + 동사: 把书放在桌子上(책을 탁자 위에 놓다) — 목적어를 동사 앞으로 이동시키는 구문"},
    {"title": "중국어 是...的 강조구문", "content": "我是昨天来的(어제 온 거예요) — 이미 발생한 사건의 시간/장소/방식을 강조할 때 사용"},
    {"title": "중국어 보어 (补语)", "content": "결과보어: 看完(다 보다) / 방향보어: 走进来(걸어 들어오다) / 가능보어: 看得懂(봐서 이해할 수 있다)"},
    {"title": "중국어 접속사", "content": "和(hé·그리고) / 但是(dànshì·하지만) / 因为...所以(yīnwèi...suǒyǐ·왜냐하면...그래서) / 虽然...但是(suīrán...dànshì·비록...하지만)"},
    {"title": "중국어 날씨 표현", "content": "天气(tiānqì·날씨) / 热(rè·덥다) / 冷(lěng·춥다) / 下雨(xià yǔ·비오다) / 下雪(xià xuě·눈오다)"},
    {"title": "중국어 쇼핑 표현", "content": "太贵了(tài guì le·너무 비싸요) / 便宜一点(piányi yīdiǎn·좀 싸게) / 可以试试吗(kěyǐ shìshi ma·입어봐도 돼요?)"},
    {"title": "중국어 감정 표현", "content": "高兴(gāoxìng·기쁜) / 难过(nánguò·슬픈) / 生气(shēngqì·화난) / 害怕(hàipà·무서운) / 累(lèi·피곤한)"},
    {"title": "중국어 HSK1 필수 단어", "content": "学习(xuéxí·공부) / 工作(gōngzuò·일) / 朋友(péngyou·친구) / 学校(xuéxiào·학교) / 医院(yīyuàn·병원) / 商店(shāngdiàn·가게)"},
    {"title": "중국어 전화/인터넷", "content": "手机(shǒujī·휴대폰) / 电脑(diànnǎo·컴퓨터) / 上网(shàng wǎng·인터넷하다) / 打电话(dǎ diànhuà·전화하다) / 发短信(fā duǎnxìn·문자보내다)"},
    {"title": "중국어 신체 부위", "content": "头(tóu·머리) / 眼睛(yǎnjing·눈) / 耳朵(ěrduo·귀) / 嘴(zuǐ·입) / 手(shǒu·손) / 脚(jiǎo·발)"},
    {"title": "중국어 비교 표현", "content": "A比B + 형용사: 他比我高(그가 나보다 크다) / A没有B + 형용사: 我没有他高(나는 그만큼 크지 않다)"},
    {"title": "중국어 능원동사", "content": "会(huì·할 수 있다/할 줄 알다) / 能(néng·능력상 가능) / 可以(kěyǐ·허가) / 想(xiǎng·~하고 싶다) / 要(yào·~할 것이다)"},
    {"title": "중국어 부사", "content": "很(hěn·매우) / 都(dōu·모두) / 也(yě·역시) / 还(hái·아직/또) / 就(jiù·곧/바로) / 才(cái·겨우/비로소)"},
    {"title": "중국어 존칭/겸양", "content": "您(nín·당신-존칭) / 请(qǐng·~해 주세요) / 贵姓(guì xìng·성이 어떻게 되시나요) / 不好意思(bù hǎoyìsi·실례합니다)"},
]

MATH = [
    {"title": "수학 - 이차방정식", "content": "ax² + bx + c = 0의 근의 공식: x = (-b ± √(b²-4ac)) / 2a — 판별식 D = b²-4ac > 0 (두 실근), = 0 (중근), < 0 (허근)"},
    {"title": "수학 - 피타고라스 정리", "content": "직각삼각형에서 a² + b² = c² (c는 빗변) — 3-4-5, 5-12-13, 8-15-17은 자주 나오는 피타고라스 삼조"},
    {"title": "수학 - 삼각함수 기본", "content": "sin θ = 대변/빗변 / cos θ = 인접변/빗변 / tan θ = 대변/인접변 — sin²θ + cos²θ = 1"},
    {"title": "수학 - 로그 법칙", "content": "log(ab) = log a + log b / log(a/b) = log a - log b / log(aⁿ) = n·log a / logₐb = ln b / ln a"},
    {"title": "수학 - 등차수열", "content": "일반항: aₙ = a₁ + (n-1)d / 합: Sₙ = n(a₁ + aₙ)/2 = n(2a₁ + (n-1)d)/2 — d는 공차"},
    {"title": "수학 - 등비수열", "content": "일반항: aₙ = a₁ · rⁿ⁻¹ / 합: Sₙ = a₁(1-rⁿ)/(1-r) (r≠1) — r은 공비, |r|<1이면 무한급수 합 = a₁/(1-r)"},
    {"title": "수학 - 미분 기초", "content": "f'(x) = lim(h→0) [f(x+h)-f(x)]/h — 기본: (xⁿ)' = nxⁿ⁻¹ / (eˣ)' = eˣ / (ln x)' = 1/x / (sin x)' = cos x"},
    {"title": "수학 - 적분 기초", "content": "∫xⁿ dx = xⁿ⁺¹/(n+1) + C / ∫eˣ dx = eˣ + C / ∫1/x dx = ln|x| + C / ∫sin x dx = -cos x + C"},
    {"title": "수학 - 행렬 기초", "content": "2×2 행렬 곱셈: [a b; c d]·[e f; g h] = [ae+bg af+bh; ce+dg cf+dh] — 행렬식: ad-bc"},
    {"title": "수학 - 확률 기초", "content": "P(A∪B) = P(A) + P(B) - P(A∩B) / 독립: P(A∩B) = P(A)·P(B) / 조건부: P(A|B) = P(A∩B)/P(B)"},
    {"title": "수학 - 순열과 조합", "content": "순열: P(n,r) = n!/(n-r)! (순서O) / 조합: C(n,r) = n!/[r!(n-r)!] (순서X) — 5C2 = 10, 5P2 = 20"},
    {"title": "수학 - 벡터 기초", "content": "내적: a·b = |a||b|cos θ / 외적: |a×b| = |a||b|sin θ — 내적=0이면 수직, 외적 결과는 벡터"},
    {"title": "수학 - 극한", "content": "lim(x→0) sin x/x = 1 / lim(x→∞)(1+1/x)ˣ = e / lim(x→0)(eˣ-1)/x = 1 — 부정형 0/0은 로피탈 법칙"},
    {"title": "수학 - 이항정리", "content": "(a+b)ⁿ = Σ C(n,k)·aⁿ⁻ᵏ·bᵏ — (a+b)² = a²+2ab+b² / (a+b)³ = a³+3a²b+3ab²+b³"},
    {"title": "수학 - 삼각함수 공식", "content": "sin(A±B) = sinAcosB ± cosAsinB / cos(A±B) = cosAcosB ∓ sinAsinB / 배각: sin2A = 2sinAcosA"},
    {"title": "수학 - 지수 법칙", "content": "aᵐ·aⁿ = aᵐ⁺ⁿ / aᵐ/aⁿ = aᵐ⁻ⁿ / (aᵐ)ⁿ = aᵐⁿ / a⁰ = 1 / a⁻ⁿ = 1/aⁿ / a^(1/n) = ⁿ√a"},
    {"title": "수학 - 원의 방정식", "content": "표준형: (x-a)² + (y-b)² = r² (중심 (a,b), 반지름 r) / 일반형: x² + y² + Dx + Ey + F = 0"},
    {"title": "수학 - 이차함수", "content": "y = ax² + bx + c — 꼭짓점: (-b/2a, f(-b/2a)) / a>0 아래로 볼록, a<0 위로 볼록 / 축: x = -b/2a"},
    {"title": "수학 - 부등식", "content": "양변에 음수를 곱하면 부등호 방향 바뀜 / |x| < a ⟹ -a < x < a / |x| > a ⟹ x < -a 또는 x > a"},
    {"title": "수학 - 집합", "content": "A∪B (합집합) / A∩B (교집합) / A' (여집합) / A-B (차집합) / 드모르간: (A∪B)' = A'∩B' / (A∩B)' = A'∪B'"},
    {"title": "수학 - 통계 기초", "content": "평균: x̄ = Σxᵢ/n / 분산: σ² = Σ(xᵢ-x̄)²/n / 표준편차: σ = √(분산) — 정규분포: 68-95-99.7 규칙"},
    {"title": "수학 - 수열의 극한", "content": "수렴: lim(n→∞) aₙ = L / 발산: ∞ 또는 진동 — lim 1/n = 0, lim rⁿ: |r|<1이면 0, r=1이면 1, |r|>1이면 발산"},
    {"title": "수학 - 함수의 연속", "content": "f(x)가 x=a에서 연속 ⟺ ①f(a) 존재 ②lim f(x) 존재 ③lim f(x) = f(a) — 중간값 정리: 연속함수는 중간값을 가짐"},
    {"title": "수학 - 미분 활용", "content": "접선의 기울기: f'(a) / 증감: f'>0 증가, f'<0 감소 / 극값: f'=0이고 f''부호 변화 / f''>0 아래로 볼록"},
    {"title": "수학 - 적분 활용", "content": "넓이: ∫ₐᵇ|f(x)|dx / 두 곡선 사이: ∫ₐᵇ|f(x)-g(x)|dx / 회전체 부피: π∫ₐᵇ[f(x)]²dx"},
    {"title": "수학 - 복소수", "content": "i² = -1 / (a+bi)(c+di) = (ac-bd)+(ad+bc)i / |a+bi| = √(a²+b²) / 켤레복소수: a+bi ↔ a-bi"},
    {"title": "수학 - 다항식 나눗셈", "content": "f(x) = q(x)·g(x) + r(x) / 나머지 정리: f(a) = f(x)를 (x-a)로 나눈 나머지 / 인수정리: f(a)=0이면 (x-a)가 인수"},
    {"title": "수학 - 삼각함수 그래프", "content": "y = A·sin(Bx+C)+D — A:진폭, 주기:2π/B, 위상이동:-C/B, 수직이동:D — cos는 sin보다 π/2 앞서감"},
    {"title": "수학 - 경우의 수", "content": "합의 법칙: 동시에 안 일어남 → 더하기 / 곱의 법칙: 동시에 일어남 → 곱하기 — 여사건: n(A') = n(전체) - n(A)"},
    {"title": "수학 - 좌표기하", "content": "두 점 거리: √[(x₂-x₁)²+(y₂-y₁)²] / 중점: ((x₁+x₂)/2, (y₁+y₂)/2) / 직선 기울기: (y₂-y₁)/(x₂-x₁)"},
]


SUBJECTS = {
    "german": GERMAN,
    "japanese": JAPANESE,
    "english": ENGLISH,
    "chinese": CHINESE,
    "math": MATH,
}

SUBJECT_LABELS = {
    "german": "🇩🇪 독일어",
    "japanese": "🇯🇵 일본어",
    "english": "🇺🇸 영어",
    "chinese": "🇨🇳 중국어",
    "math": "📐 수학",
}


def generate_daily_tasks(d: date) -> list[dict]:
    """Generate study tasks for a given date."""
    tasks = []
    order = 0
    for subject_key, pool in SUBJECTS.items():
        idx = _day_index(d, len(pool), subject_key)
        item = pool[idx]
        tasks.append({
            "date": d.isoformat(),
            "subject": SUBJECT_LABELS[subject_key],
            "title": item["title"],
            "content": item["content"],
            "sort_order": order,
        })
        order += 1
    return tasks
