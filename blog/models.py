from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.conf import settings

univ_list = (
        
        ('가야대학교김해캠퍼스','가야대학교김해캠퍼스'),
        ('가천대학교글로벌캠퍼스','가천대학교글로벌캠퍼스'),
        ('가천대학교메디컬캠퍼스','가천대학교메디컬캠퍼스'),
        ('가톨릭관동대학교','가톨릭관동대학교'),
        ('가톨릭대학교성신교정','가톨릭대학교성신교정'),
        ('가톨릭대학교성심교정','가톨릭대학교성심교정'),
        ('가톨릭대학교성의교정','가톨릭대학교성의교정'),
        ('감리교신학대학교','감리교신학대학교'),
        ('강남대학교','강남대학교'),
        ('강릉영동대학교','강릉영동대학교'),
        ('강릉원주대학교강릉캠퍼스','강릉원주대학교강릉캠퍼스'),
        ('강릉원주대학교원주캠퍼스','강릉원주대학교원주캠퍼스'),
        ('강원관광대학교','강원관광대학교'),
        ('강원대학교도계캠퍼스','강원대학교도계캠퍼스'),
        ('강원대학교삼척캠퍼스','강원대학교삼척캠퍼스'),
        ('강원대학교춘천캠퍼스','강원대학교춘천캠퍼스'),
        ('강원도립대학교','강원도립대학교'),
        ('거제대학교','거제대학교'),
        ('건국대학교글로벌캠퍼스','건국대학교글로벌캠퍼스'),
        ('건국대학교서울캠퍼스','건국대학교서울캠퍼스'),
        ('건양대학교메디컬캠퍼스','건양대학교메디컬캠퍼스'),
        ('건양대학교창의웅합캠퍼스','건양대학교창의웅합캠퍼스'),
        ('건양사이버대학교','건양사이버대학교'),
        ('경기과학기술대학교','경기과학기술대학교'),
        ('경기대학교서울캠퍼스','경기대학교서울캠퍼스'),
        ('경기대학교수원캠퍼스','경기대학교수원캠퍼스'),
        ('경남과학기술대학교','경남과학기술대학교'),
        ('경남도립거창대학','경남도립거창대학'),
        ('경남도립남해대학','경남도립남해대학'),
        ('경남정보대학교','경남정보대학교'),
        ('경동대학교설악제2캠퍼스','경동대학교설악제2캠퍼스'),
        ('경동대학교양주캠퍼스','경동대학교양주캠퍼스'),
        ('경동대학교원주캠퍼스','경동대학교원주캠퍼스'),
        ('경민대학교','경민대학교'),
        ('경복대학교남양주캠퍼스','경복대학교남양주캠퍼스'),
        ('경복대학교포천캠퍼스','경복대학교포천캠퍼스'),
        ('경북대학교대구캠퍼스','경북대학교대구캠퍼스'),
        ('경북대학교상주캠퍼스','경북대학교상주캠퍼스'),
        ('경상대학교가좌캠퍼스','경상대학교가좌캠퍼스'),
        ('경상대학교칠암캠퍼스','경상대학교칠암캠퍼스'),
        ('경성대학교','경성대학교'),
        ('경인교육대학교경기캠퍼스','경인교육대학교경기캠퍼스'),
        ('경인교육대학교인천캠퍼스','경인교육대학교인천캠퍼스'),
        ('경인여자대학교','경인여자대학교'),
        ('경찰대학','경찰대학'),
        ('경희대학교국제캠퍼스','경희대학교국제캠퍼스'),
        ('경희대학교서울캠퍼스','경희대학교서울캠퍼스'),
        ('계명대학교대명캠퍼스','계명대학교대명캠퍼스'),
        ('계명대학교성서캠퍼스','계명대학교성서캠퍼스'),
        ('계명문화대학교','계명문화대학교'),
        ('계원예술대학교','계원예술대학교'),
        ('고구려대학교','고구려대학교'),
        ('고려대학교서울캠퍼스','고려대학교서울캠퍼스'),
        ('고려대학교세종캠퍼스','고려대학교세종캠퍼스'),
        ('고신대학교송도캠퍼스','고신대학교송도캠퍼스'),
        ('고신대학교영도캠퍼스','고신대학교영도캠퍼스'),
        ('고신대학교천안캠퍼스','고신대학교천안캠퍼스'),
        ('공군사관학교','공군사관학교'),
        ('공주교육대학교','공주교육대학교'),
        ('공주대학교신관캠퍼스','공주대학교신관캠퍼스'),
        ('공주대학교예산컴퍼스','공주대학교예산컴퍼스'),
        ('공주대학교옥룡컴퍼스','공주대학교옥룡컴퍼스'),
        ('공주대학교천안캠퍼스','공주대학교천안캠퍼스'),
        ('광신대학교','광신대학교'),
        ('광양보건대학교','광양보건대학교'),
        ('광운대학교','광운대학교'),
        ('광주가톨릭대학교','광주가톨릭대학교'),
        ('광주과학기술원','광주과학기술원'),
        ('광주교육대학교','광주교육대학교'),
        ('광주대학교','광주대학교'),
        ('광주보건대학교','광주보건대학교'),
        ('광주여자대학교','광주여자대학교'),
        ('국군간호사관학교','국군간호사관학교'),
        ('국민대학교','국민대학교'),
        ('국방대학교','국방대학교'),
        ('국제대학교','국제대학교'),
        ('국제예술대학교','국제예술대학교'),
        ('군산간호대학교','군산간호대학교'),
        ('군산대학교미룡캠퍼스','군산대학교미룡캠퍼스'),
        ('군산대학교새만금캠퍼스','군산대학교새만금캠퍼스'),
        ('군장대학교','군장대학교'),
        ('극동대학교','극동대학교'),
        ('금강대학교','금강대학교'),
        ('기독간호대학교','기독간호대학교'),
        ('김포대학교','김포대학교'),
        ('꽃동네대학교','꽃동네대학교'),
        ('나사렛대학교','나사렛대학교'),
        ('남부대학교','남부대학교'),
        ('남서울대학교','남서울대학교'),
        ('농협대학교','농협대학교'),
        ('단국대학교죽전캠퍼스','단국대학교죽전캠퍼스'),
        ('단국대학교천안캠퍼스','단국대학교천안캠퍼스'),
        ('대구가톨릭대학교루가캠퍼스','대구가톨릭대학교루가캠퍼스'),
        ('대구가톨릭대학교유스티노캠퍼스','대구가톨릭대학교유스티노캠퍼스'),
        ('대구경북과학기술원','대구경북과학기술원'),
        ('대구공업대학교','대구공업대학교'),
        ('대구과학대학교','대구과학대학교'),
        ('대구교육대학교','대구교육대학교'),
        ('대구대학교대명동캠퍼스','대구대학교대명동캠퍼스'),
        ('대구보건대학교','대구보건대학교'),
        ('대구한의대학교수성캠퍼스','대구한의대학교수성캠퍼스'),
        ('대덕대학교','대덕대학교'),
        ('대동대학교','대동대학교'),
        ('대림대학교','대림대학교'),
        ('대전가톨릭대학교','대전가톨릭대학교'),
        ('대전과학기술대학교','대전과학기술대학교'),
        ('대전대학교','대전대학교'),
        ('대전보건대학교','대전보건대학교'),
        ('대전신학대학교','대전신학대학교'),
        ('대진대학교','대진대학교'),
        ('덕성여자대학교쌍문캠퍼스','덕성여자대학교쌍문캠퍼스'),
        ('덕성여자대학교종로캠퍼스','덕성여자대학교종로캠퍼스'),
        ('동강대학교','동강대학교'),
        ('동국대학교바이오메디캠퍼스','동국대학교바이오메디캠퍼스'),
        ('동국대학교서울캠퍼스','동국대학교서울캠퍼스'),
        ('동남보건대학교','동남보건대학교'),
        ('동덕여자대학교','동덕여자대학교'),
        ('동명대학교','동명대학교'),
        ('동부산대학교','동부산대학교'),
        ('동서대학교','동서대학교'),
        ('동서울대학교','동서울대학교'),
        ('동신대학교','동신대학교'),
        ('동아대학교구덕캠퍼스','동아대학교구덕캠퍼스'),
        ('동아대학교부민캠퍼스','동아대학교부민캠퍼스'),
        ('동아대학교승학캠퍼스','동아대학교승학캠퍼스'),
        ('동아방송예술대학교','동아방송예술대학교'),
        ('동아보건대학교','동아보건대학교'),
        ('동양대학교북서울캠퍼스','동양대학교북서울캠퍼스'),
        ('동양미래대학교','동양미래대학교'),
        ('동원과학기술대학교','동원과학기술대학교'),
        ('동원대학교','동원대학교'),
        ('동의과학대학교','동의과학대학교'),
        ('동의대학교가야캠퍼스','동의대학교가야캠퍼스'),
        ('동의대학교양정캠퍼스','동의대학교양정캠퍼스'),
        ('동주대학교','동주대학교'),
        ('두원공과대학교안성캠퍼스','두원공과대학교안성캠퍼스'),
        ('두원공과대학교파주캠퍼스','두원공과대학교파주캠퍼스'),
        ('루터대학교','루터대학교'),
        ('명지대학교인문캠퍼스','명지대학교인문캠퍼스'),
        ('명지대학교자연캠퍼스','명지대학교자연캠퍼스'),
        ('명지전문대학','명지전문대학'),
        ('목원대학교','목원대학교'),
        ('목포가톨릭대학교','목포가톨릭대학교'),
        ('목포과학대학교','목포과학대학교'),
        ('목포대학교남악캠퍼스','목포대학교남악캠퍼스'),
        ('목포대학교도림캠퍼스','목포대학교도림캠퍼스'),
        ('목포대학교목포캠퍼스','목포대학교목포캠퍼스'),
        ('목포대학교신해양산업단지캠퍼스','목포대학교신해양산업단지캠퍼스'),
        ('목포해양대학교','목포해양대학교'),
        ('배재대학교','배재대학교'),
        ('배화여자대학교','배화여자대학교'),
        ('백석대학교','백석대학교'),
        ('백석문화대학교','백석문화대학교'),
        ('백석예술대학교','백석예술대학교'),
        ('백제예술대학교','백제예술대학교'),
        ('부경대학교대연캠퍼스','부경대학교대연캠퍼스'),
        ('부경대학교용당캠퍼스','부경대학교용당캠퍼스'),
        ('부산가톨릭대학교메리놀교정','부산가톨릭대학교메리놀교정'),
        ('부산가톨릭대학교신학교정','부산가톨릭대학교신학교정'),
        ('부산가톨릭대학교지산교정','부산가톨릭대학교지산교정'),
        ('부산경상대학교','부산경상대학교'),
        ('부산과학기술대학교','부산과학기술대학교'),
        ('부산교육대학교','부산교육대학교'),
        ('부산대학교밀양캠퍼스','부산대학교밀양캠퍼스'),
        ('부산대학교부산캠퍼스','부산대학교부산캠퍼스'),
        ('부산대학교양산캠퍼스','부산대학교양산캠퍼스'),
        ('부산디지털대학교','부산디지털대학교'),
        ('부산여자대학교','부산여자대학교'),
        ('부산예술대학교','부산예술대학교'),
        ('부산외국어대학교','부산외국어대학교'),
        ('부산장신대학교','부산장신대학교'),
        ('부천대학교','부천대학교'),
        ('삼육대학교','삼육대학교'),
        ('삼육보건대학교','삼육보건대학교'),
        ('상명대학교서울캠퍼스','상명대학교서울캠퍼스'),
        ('상명대학교천안캠퍼스','상명대학교천안캠퍼스'),
        ('상지대학교','상지대학교'),
        ('상지영서대학교','상지영서대학교'),
        ('서강대학교','서강대학교'),
        ('서경대학교','서경대학교'),
        ('서영대학교광주캠퍼스','서영대학교광주캠퍼스'),
        ('서영대학교파주캠퍼스','서영대학교파주캠퍼스'),
        ('서울과학기술대학교','서울과학기술대학교'),
        ('서울교육대학교','서울교육대학교'),
        ('서울기독대학교','서울기독대학교'),
        ('서울대학교관악캠퍼스','서울대학교관악캠퍼스'),
        ('서울대학교연건캠퍼스','서울대학교연건캠퍼스'),
        ('서울시립대학교','서울시립대학교'),
        ('서울신학대학교','서울신학대학교'),
        ('서울여자간호대학교','서울여자간호대학교'),
        ('서울여자대학교','서울여자대학교'),
        ('서울예술대학교','서울예술대학교'),
        ('서울장신대학교','서울장신대학교'),
        ('서울한영대학교','서울한영대학교'),
        ('서원대학교','서원대학교'),
        ('서일대학교','서일대학교'),
        ('서정대학교','서정대학교'),
        ('서해대학','서해대학'),
        ('선문대학교','선문대학교'),
        ('성균관대학교인문사회캠퍼스','성균관대학교인문사회캠퍼스'),
        ('성균관대학교자연과학캠퍼스','성균관대학교자연과학캠퍼스'),
        ('성신여자대학교수정캠퍼스','성신여자대학교수정캠퍼스'),
        ('성신여자대학교운정그린캠퍼스','성신여자대학교운정그린캠퍼스'),
        ('세경대학교','세경대학교'),
        ('세명대학교','세명대학교'),
        ('세종대학교','세종대학교'),
        ('세한대학교당진캠퍼스','세한대학교당진캠퍼스'),
        ('세한대학교영암캠퍼스','세한대학교영암캠퍼스'),
        ('솔브릿지국제경영대학교','솔브릿지국제경영대학교'),
        ('송곡대학교','송곡대학교'),
        ('송원대학교','송원대학교'),
        ('송호대학교','송호대학교'),
        ('수성대학교','수성대학교'),
        ('수원과학대학교','수원과학대학교'),
        ('수원여자대학교','수원여자대학교'),
        ('숙명여자대학교','숙명여자대학교'),
        ('순복음총회신학교','순복음총회신학교'),
        ('순천대학교','순천대학교'),
        ('순천제일대학교','순천제일대학교'),
        ('순천향대학교','순천향대학교'),
        ('숭실대학교','숭실대학교'),
        ('숭의여자대학교','숭의여자대학교'),
        ('신구대학교','신구대학교'),
        ('신라대학교','신라대학교'),
        ('신성대학교','신성대학교'),
        ('신안산대학교','신안산대학교'),
        ('아세아연합신학대학교','아세아연합신학대학교'),
        ('아주대학교','아주대학교'),
        ('아주자동차대학교','아주자동차대학교'),
        ('안산대학교','안산대학교'),
        ('안양대학교강화캠퍼스','안양대학교강화캠퍼스'),
        ('안양대학교안양캠퍼스','안양대학교안양캠퍼스'),
        ('여주대학교','여주대학교'),
        ('연성대학교','연성대학교'),
        ('연세대학교국제캠퍼스','연세대학교국제캠퍼스'),
        ('연세대학교신촌캠퍼스','연세대학교신촌캠퍼스'),
        ('연세대학교원주캠퍼스','연세대학교원주캠퍼스'),
        ('연암공과대학교','연암공과대학교'),
        ('연암대학교','연암대학교'),
        ('영남이공대학교','영남이공대학교'),
        ('영산대학교양산캠퍼스','영산대학교양산캠퍼스'),
        ('영산대학교해운대캠퍼스','영산대학교해운대캠퍼스'),
        ('영산선학대학교','영산선학대학교'),
        ('영진사이버대학교','영진사이버대학교'),
        ('영진전문대학교','영진전문대학교'),
        ('예수대학교','예수대학교'),
        ('예원예술대학교양주캠퍼스','예원예술대학교양주캠퍼스'),
        ('예원예술대학교희망캠퍼스','예원예술대학교희망캠퍼스'),
        ('오산대학교','오산대학교'),
        ('용인대학교','용인대학교'),
        ('용인송담대학교','용인송담대학교'),
        ('우석대학교전주캠퍼스','우석대학교전주캠퍼스'),
        ('우석대학교진천캠퍼스','우석대학교진천캠퍼스'),
        ('우송대학교','우송대학교'),
        ('우송정보대학교','우송정보대학교'),
        ('웅지세무대학교','웅지세무대학교'),
        ('원광대학교익산캠퍼스','원광대학교익산캠퍼스'),
        ('원광디지털대학교','원광디지털대학교'),
        ('원광보건대학교','원광보건대학교'),
        ('유원대학교','유원대학교'),
        ('유원대학교아산캠퍼스','유원대학교아산캠퍼스'),
        ('유한대학교','유한대학교'),
        ('육군사관학교','육군사관학교'),
        ('을지대학교성남캠퍼스','을지대학교성남캠퍼스'),
        ('이화여자대학교','이화여자대학교'),
        ('인덕대학교','인덕대학교'),
        ('인제대학교김해캠퍼스','인제대학교김해캠퍼스'),
        ('인제대학교부산캠퍼스','인제대학교부산캠퍼스'),
        ('인천가톨릭대학교강화캠퍼스','인천가톨릭대학교강화캠퍼스'),
        ('인천가톨릭대학교송도국제캠퍼스','인천가톨릭대학교송도국제캠퍼스'),
        ('인천대학교미추홀캠퍼스','인천대학교미추홀캠퍼스'),
        ('인천대학교송도캠퍼스','인천대학교송도캠퍼스'),
        ('인천대학교제물포캠퍼스','인천대학교제물포캠퍼스'),
        ('인천재능대학교국제캠퍼스','인천재능대학교국제캠퍼스'),
        ('인천재능대학교재물포캠퍼스','인천재능대학교재물포캠퍼스'),
        ('인하공업전문대학교','인하공업전문대학교'),
        ('인하대학교','인하대학교'),
        ('장로회신학대학교','장로회신학대학교'),
        ('장안대학교','장안대학교'),
        ('전남과학대학교','전남과학대학교'),
        ('전남대학교여수캠퍼스','전남대학교여수캠퍼스'),
        ('전남대학교용봉캠퍼스','전남대학교용봉캠퍼스'),
        ('전남대학교학동캠퍼스','전남대학교학동캠퍼스'),
        ('전남도립대학교','전남도립대학교'),
        ('전북과학대학교','전북과학대학교'),
        ('전북대학교고창캠퍼스','전북대학교고창캠퍼스'),
        ('전북대학교새만금캠퍼스','전북대학교새만금캠퍼스'),
        ('전북대학교익산캠퍼스','전북대학교익산캠퍼스'),
        ('전북대학교전주캠퍼스','전북대학교전주캠퍼스'),
        ('전주교육대학교','전주교육대학교'),
        ('전주기전대학','전주기전대학'),
        ('전주대학교전주캠퍼스','전주대학교전주캠퍼스'),
        ('전주비전대학교','전주비전대학교'),
        ('정화예술대학교','정화예술대학교'),
        ('제주관광대학교','제주관광대학교'),
        ('제주국제대학교','제주국제대학교'),
        ('제주대학교사라캠퍼스','제주대학교사라캠퍼스'),
        ('제주대학교아라캠퍼스','제주대학교아라캠퍼스'),
        ('제주한라대학교','제주한라대학교'),
        ('조선간호대학교','조선간호대학교'),
        ('조선대학교','조선대학교'),
        ('조선이공대학교','조선이공대학교'),
        ('중부대학교','중부대학교'),
        ('중부대학교고양캠퍼스','중부대학교고양캠퍼스'),
        ('중앙대학교서울캠퍼스','중앙대학교서울캠퍼스'),
        ('중앙대학교안성캠퍼스','중앙대학교안성캠퍼스'),
        ('중앙승가대학교','중앙승가대학교'),
        ('중원대학교','중원대학교'),
        ('진주교육대학교','진주교육대학교'),
        ('진주보건대학교','진주보건대학교'),
        ('차의과학대학교','차의과학대학교'),
        ('청강문화산업대학교','청강문화산업대학교'),
        ('청암대학교','청암대학교'),
        ('청운대학교인천캠퍼스','청운대학교인천캠퍼스'),
        ('청운대학교홍성캠퍼스','청운대학교홍성캠퍼스'),
        ('청주교육대학교','청주교육대학교'),
        ('청주대학교','청주대학교'),
        ('초당대학교','초당대학교'),
        ('추계예술대학교','추계예술대학교'),
        ('충남대학교','충남대학교'),
        ('충남도립대학교','충남도립대학교'),
        ('충북대학교','충북대학교'),
        ('침례신학대학교','침례신학대학교'),
        ('칼빈대학교','칼빈대학교'),
        ('케이씨대학교','케이씨대학교'),
        ('평택대학교','평택대학교'),
        ('한경대학교','한경대학교'),
        ('한국골프대학교','한국골프대학교'),
        ('한국과학기술원(KAIST)','한국과학기술원(KAIST)'),
        ('한국관광대학교','한국관광대학교'),
        ('한국교원대학교','한국교원대학교'),
        ('한국교통대학교의왕캠퍼스','한국교통대학교의왕캠퍼스'),
        ('한국교통대학교증평캠퍼스','한국교통대학교증평캠퍼스'),
        ('한국교통대학교충주캠퍼스','한국교통대학교충주캠퍼스'),
        ('한국국제대학교','한국국제대학교'),
        ('한국기술교육대학교제1캠퍼스','한국기술교육대학교제1캠퍼스'),
        ('한국기술교육대학교제2캠퍼스','한국기술교육대학교제2캠퍼스'),
        ('한국농수산대학교','한국농수산대학교'),
        ('한국방송통신대학교','한국방송통신대학교'),
        ('한국복지대학교','한국복지대학교'),
        ('한국산업기술대학교','한국산업기술대학교'),
        ('한국성서대학교','한국성서대학교'),
        ('한국승강기대학교','한국승강기대학교'),
        ('한국영상대학교','한국영상대학교'),
        ('한국예술종합학교대학로캠퍼스','한국예술종합학교대학로캠퍼스'),
        ('한국예술종합학교서초캠퍼스','한국예술종합학교서초캠퍼스'),
        ('한국예술종합학교석관캠퍼스','한국예술종합학교석관캠퍼스'),
        ('한국외국어대학교글로벌캠퍼스','한국외국어대학교글로벌캠퍼스'),
        ('한국외국어대학교서울캠퍼스','한국외국어대학교서울캠퍼스'),
        ('한국전통문화대학교','한국전통문화대학교'),
        ('한국체육대학교','한국체육대학교'),
        ('한국폴리텍6대학달성캠퍼스','한국폴리텍6대학달성캠퍼스'),
        ('한국폴리텍Ⅳ대학교대전캠퍼스','한국폴리텍Ⅳ대학교대전캠퍼스'),
        ('한국폴리텍Ⅳ대학교아산캠퍼스','한국폴리텍Ⅳ대학교아산캠퍼스'),
        ('한국폴리텍Ⅳ대학교청주캠퍼스','한국폴리텍Ⅳ대학교청주캠퍼스'),
        ('한국폴리텍Ⅳ대학교충주캠퍼스','한국폴리텍Ⅳ대학교충주캠퍼스'),
        ('한국폴리텍Ⅳ대학교홍성캠퍼스','한국폴리텍Ⅳ대학교홍성캠퍼스'),
        ('한국폴리텍III대학강릉캠퍼스','한국폴리텍III대학강릉캠퍼스'),
        ('한국폴리텍III대학원주캠퍼스','한국폴리텍III대학원주캠퍼스'),
        ('한국폴리텍III대학춘천제1캠퍼스','한국폴리텍III대학춘천제1캠퍼스'),
        ('한국폴리텍III대학춘천제2캠퍼스','한국폴리텍III대학춘천제2캠퍼스'),
        ('한국폴리텍II대학남인천캠퍼스','한국폴리텍II대학남인천캠퍼스'),
        ('한국폴리텍II대학안성캠퍼스','한국폴리텍II대학안성캠퍼스'),
        ('한국폴리텍II대학인천캠퍼스','한국폴리텍II대학인천캠퍼스'),
        ('한국폴리텍II대학화성캠퍼스','한국폴리텍II대학화성캠퍼스'),
        ('한국폴리텍I대학성남캠퍼스','한국폴리텍I대학성남캠퍼스'),
        ('한국폴리텍I대학제주캠퍼스','한국폴리텍I대학제주캠퍼스'),
        ('한국폴리텍V대학김제캠퍼스','한국폴리텍V대학김제캠퍼스'),
        ('한국폴리텍V대학익산캠퍼스','한국폴리텍V대학익산캠퍼스'),
        ('한국폴리텍대학교','한국폴리텍대학교'),
        ('한국폴리텍대학교광주캠퍼스','한국폴리텍대학교광주캠퍼스'),
        ('한국폴리텍대학교대전캠퍼스','한국폴리텍대학교대전캠퍼스'),
        ('한국폴리텍대학교부산캠퍼스','한국폴리텍대학교부산캠퍼스'),
        ('한국폴리텍대학교항공캠퍼스','한국폴리텍대학교항공캠퍼스'),
        ('한국폴리텍대학대구캠퍼스','한국폴리텍대학대구캠퍼스'),
        ('한국폴리텍대학목포캠퍼스','한국폴리텍대학목포캠퍼스'),
        ('한국폴리텍대학섬유패션캠퍼스','한국폴리텍대학섬유패션캠퍼스'),
        ('한국폴리텍대학진주캠퍼스','한국폴리텍대학진주캠퍼스'),
        ('한국폴리텍특성화대학교바이오캠퍼스','한국폴리텍특성화대학교바이오캠퍼스'),
        ('한국항공대학교','한국항공대학교'),
        ('한국해양대학교','한국해양대학교'),
        ('한남대학교','한남대학교'),
        ('한라대학교','한라대학교'),
        ('한려대학교','한려대학교'),
        ('한림대학교','한림대학교'),
        ('한림성심대학교','한림성심대학교'),
        ('한밭대학교','한밭대학교'),
        ('한서대학교서산캠퍼스','한서대학교서산캠퍼스'),
        ('한서대학교태안캠퍼스','한서대학교태안캠퍼스'),
        ('한성대학교','한성대학교'),
        ('한세대학교','한세대학교'),
        ('한신대학교','한신대학교'),
        ('한양대학교서울캠퍼스','한양대학교서울캠퍼스'),
        ('한양대학교에리카','한양대학교에리카'),
        ('한양여자대학교','한양여자대학교'),
        ('한영대학','한영대학'),
        ('한일장신대학교','한일장신대학교'),
        ('한전공과대학교','한전공과대학교'),
        ('협성대학교','협성대학교'),
        ('호남대학교광산캠퍼스','호남대학교광산캠퍼스'),
        ('호남대학교쌍촌캠퍼스','호남대학교쌍촌캠퍼스'),
        ('호서대학교당진산업화학융합캠퍼스','호서대학교당진산업화학융합캠퍼스'),
        ('호서대학교아산캠퍼스','호서대학교아산캠퍼스'),
        ('호서대학교천안캠퍼스','호서대학교천안캠퍼스'),
        ('호원대학교군산캠퍼스','호원대학교군산캠퍼스'),
        ('홍익대학교서울캠퍼스','홍익대학교서울캠퍼스'),
        ('홍익대학교세종캠퍼스','홍익대학교세종캠퍼스'),
        ('화신사이버대학교','화신사이버대학교'),

    )

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    age = models.IntegerField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Blog(models.Model):
    text = models.TextField()

class Tags(models.Model):
    tag = models.CharField(max_length=10)

class Items(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    auto_increment_id = models.AutoField(primary_key=True)
    cost = models.IntegerField()
    tag = models.CharField(max_length=10)
    lat = models.DecimalField(max_digits=13, decimal_places=10)
    lng = models.DecimalField(max_digits=13, decimal_places=10)
    loca = models.CharField(verbose_name='소속대학', max_length=15, choices=univ_list)
    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='like_user_set',through='Like')

    @property
    def like_count(self):
      return self.like_user_set.count()

class Like(models.Model):
    item = models.ForeignKey('Items', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    content = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            ('author', 'item')
        )

class CustomUser(AbstractUser):     
    GENDERS = (
        ('M', '남성'),
        ('W', '여성'),
    )
    auto_increment_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    gender = models.CharField(verbose_name='성별', max_length=1, choices=GENDERS)
    name = models.CharField(verbose_name='이름', max_length=10)
    Access_path = (
        ('a', 'SNS'),
        ('b', '네이버 광고'),
        ('c', '학교 커뮤니티'),
        ('d', '교내홍보팀'),
        ('e', '오픈카톡방'),
        ('f', '기타'),
    )
    job = models.CharField(verbose_name='직업', max_length=1, choices=Access_path)

