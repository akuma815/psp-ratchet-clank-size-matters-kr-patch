"""Update translation_patches.json with comprehensive dialogue and quest audit findings."""
import json
from pathlib import Path

BASE = Path("g:/Downloads/Korean Traslate Project/Games/Ratchet  Clank - Size Matters")
PATCHES_FILE = BASE / "workspace/translation/translation_patches.json"

NEW_PATCHES = [
    # ---------------- Cutscenes & Dialogues (Clank voice, typos, humor) ----------------
    {
        "file": "localdat",
        "id": 5005,
        "original": "야, 지금 나 무시하냐?",
        "patched": "저기, 제 말 무시하시는 겁니까?",
        "reason": "클랭크 신사적 경어체 복원 (라쳇에게 시비조 반말 -> 정중한 존댓말)",
        "category": "tier3_dialogue_voice"
    },
    {
        "file": "localdat",
        "id": 5013,
        "original": "15분 뒤에 출동하라는 연락이 왔는데<ELLIPSIS>\n뭐, 까짓거. 몸 푸는 셈 치지.",
        "patched": "다음 은하 구출 스케줄까지 15분 남았는데<ELLIPSIS>\n뭐, 어때. 몸이나 풀지 뭐.",
        "reason": "15 minutes till next save schedule 오역 교정 및 라쳇 성격 반영",
        "category": "tier3_dialogue_voice"
    },
    {
        "file": "localdat",
        "id": 5042,
        "original": "나는 믿어. 바로 이게 그 사실을 증명할 거야. 그래서 로봇들도 이걸 얻으려도 소녀를 노린 거라구.",
        "patched": "나는 믿어. 바로 이게 그 사실을 증명할 거야. 그래서 로봇들도 이걸 얻으려고 소녀를 노린 거라구.",
        "reason": "'얻으려도' -> '얻으려고' 오타 교정",
        "category": "tier3_dialogue_typo"
    },
    {
        "file": "localdat",
        "id": 5073,
        "original": "식물을 맞추면 그들이 따라오지. 그런 다음 전자 토양에 뿌리면 그들은 플랫폼으로 들어가서 형태를 바꾼 후 네가 원하는 크리처가 되지.",
        "patched": "식물을 맞추면 녀석들이 따라오지. 그런 다음 전자 토양에 뿌리면 발판 속으로 들어가 형태를 바꿔서 네가 원하는 생물이 되지.",
        "reason": "번역투 대명사 '그들이' 교정 및 용어 순화",
        "category": "tier3_dialogue_voice"
    },
    {
        "file": "localdat",
        "id": 5074,
        "original": "너도 들었지, 라쳇? 그거 아주 유용하겠는데!",
        "patched": "들으셨죠, 라쳇? 그거 아주 유용하겠어요!",
        "reason": "클랭크 신사적 존댓말 회복",
        "category": "tier3_dialogue_voice"
    },
    {
        "file": "localdat",
        "id": 5079,
        "original": "이 갈라진 틈을 이용하면 될 것 같아. 잠깐만 기다려. 내가 문을 열테니까.",
        "patched": "이 갈라진 틈을 이용하면 될 것 같아요. 잠깐만 기다리세요. 제가 문을 열 테니까요.",
        "reason": "클랭크 존댓말 회복 및 '열 테니까' 띄어쓰기 교정",
        "category": "tier3_dialogue_voice"
    },
    {
        "file": "localdat",
        "id": 5080,
        "original": "좋도록 해. 늙어 죽기 전까진 끝내라구!",
        "patched": "마음대로 해. 늙어 죽기 전엔 끝내라구!",
        "reason": "'Be my guest' 오역 '좋도록 해' 교정",
        "category": "tier3_dialogue_voice"
    },
    {
        "file": "localdat",
        "id": 5087,
        "original": "테크노마이트 지도야.\n그들이 살고 있었던 행성들을 보여주는 거지.",
        "patched": "테크노마이트 지도야.\n녀석들이 살았던 행성들을 보여주는 거지.",
        "reason": "번역투 '그들이' 교정",
        "category": "tier3_dialogue_voice"
    },
    {
        "file": "localdat",
        "id": 5092,
        "original": "뭔가 이상해. 너무 쉽잖아.",
        "patched": "뭔가 이상해요. 너무 쉽잖아요.",
        "reason": "클랭크 존댓말 회복",
        "category": "tier3_dialogue_voice"
    },
    {
        "file": "localdat",
        "id": 5093,
        "original": "쉬워?! 그럼 나는 쉴 테니 혼자 좀 싸워라.",
        "patched": "쉽다고?! 그럼 넌 싸우고 난 낮잠이나 잘란다.",
        "reason": "원문 라쳇의 유머 대사 자연스러운 말투로 교정",
        "category": "tier3_dialogue_voice"
    },
    {
        "file": "localdat",
        "id": 5094,
        "original": "그게 아니라 모습을 드러내기를 꺼리는 테크노마이트를\n우리가 너무 쉽게 찾고 있잖아.",
        "patched": "그게 아니라 은둔자 같은 테크노마이트를\n우리가 너무 쉽게 찾고 있잖아요.",
        "reason": "클랭크 존댓말 회복",
        "category": "tier3_dialogue_voice"
    },
    {
        "file": "localdat",
        "id": 5098,
        "original": "Faux-Family.com? 뭔가 수상하지 않아?",
        "patched": "Faux-Family.com? 뭔가 수상하지 않나요?",
        "reason": "클랭크 존댓말 회복",
        "category": "tier3_dialogue_voice"
    },
    {
        "file": "localdat",
        "id": 5136,
        "original": "와, 엄청난 덩치군. 하지만 이제 시작이야. 끔찍한 장면이 싫으면 눈을 감어.",
        "patched": "와, 엄청난 덩치군. 하지만 이제 시작이야. 끔찍한 장면이 싫으면 눈을 감아.",
        "reason": "'눈을 감어' -> '눈을 감아' 비표준 구어 오타 교정",
        "category": "tier3_dialogue_typo"
    },
    {
        "file": "localdat",
        "id": 5140,
        "original": "라쳇, 일어나!",
        "patched": "라쳇, 일어나세요!",
        "reason": "클랭크 존댓말 회복",
        "category": "tier3_dialogue_voice"
    },
    {
        "file": "localdat",
        "id": 5141,
        "original": "죽으면 안 돼! 아직 할 일이 산더미야!",
        "patched": "죽으시면 안 돼요! 아직 할 일이 산더미라고요!",
        "reason": "클랭크 존댓말 회복",
        "category": "tier3_dialogue_voice"
    },
    {
        "file": "localdat",
        "id": 5142,
        "original": "난 처음부터 루나가 수상했어.",
        "patched": "전 처음부터 루나가 수상했어요.",
        "reason": "클랭크 존댓말 회복",
        "category": "tier3_dialogue_voice"
    },
    {
        "file": "localdat",
        "id": 5143,
        "original": "다 내 잘못이야.",
        "patched": "다 제 잘못이에요.",
        "reason": "클랭크 존댓말 회복",
        "category": "tier3_dialogue_voice"
    },
    {
        "file": "localdat",
        "id": 5144,
        "original": "죽으면 안 돼! 아직 할 일이 산더미야!",
        "patched": "죽으시면 안 돼요! 아직 할 일이 산더미란 말이에요!",
        "reason": "클랭크 존댓말 회복",
        "category": "tier3_dialogue_voice"
    },
    {
        "file": "localdat",
        "id": 5145,
        "original": "난 처음부터 루나가 수상했어. 모두 내 잘못이야.",
        "patched": "전 처음부터 루나가 수상했어요. 다 제 잘못이에요.",
        "reason": "클랭크 존댓말 회복",
        "category": "tier3_dialogue_voice"
    },
    {
        "file": "localdat",
        "id": 5153,
        "original": "사건의 전말을 파해치려면\n우선 여길 나가서 루나를 찾아야 돼.",
        "patched": "사건의 전말을 파헤치려면\n우선 여길 나가서 루나를 찾아야 돼.",
        "reason": "'파해치려면' -> '파헤치려면' 맞춤법 오타 교정",
        "category": "tier3_dialogue_typo"
    },
    {
        "file": "localdat",
        "id": 5167,
        "original": "배달이 완료되면 연락 드리겠습니다. 그럼.",
        "patched": "배달이 완료되면 연락드리겠습니다. 그럼.",
        "reason": "'연락 드리겠습니다' -> '연락드리겠습니다' 붙여쓰기",
        "category": "tier3_dialogue_typo"
    },
    {
        "file": "localdat",
        "id": 5175,
        "original": "아니에요. 감사합니다.",
        "patched": "아뇨, 사양하겠습니다.",
        "reason": "제안 거절 'No thanks' 오역 교정",
        "category": "tier3_dialogue_voice"
    },
    {
        "file": "localdat",
        "id": 5203,
        "original": "뛰어나든 아니든 공장 좌표를 얻으려면 반드시 루나를<ELLIPSIS>어<ELLIPSIS>작동불능으로 만들어야 돼.",
        "patched": "뛰어나든 아니든 공장 좌표를 얻으려면 반드시 루나를<ELLIPSIS>어<ELLIPSIS>작동 불능으로 만들어야 돼.",
        "reason": "'작동불능' -> '작동 불능' 띄어쓰기 교정",
        "category": "tier3_dialogue_typo"
    },
    {
        "file": "localdat",
        "id": 5226,
        "original": "루나를 해킹하면서 회로가 끊어졌었어.",
        "patched": "루나를 해킹하다가 회로가 끊어졌었어요.",
        "reason": "클랭크 존댓말 회복",
        "category": "tier3_dialogue_voice"
    },
    {
        "file": "localdat",
        "id": 5227,
        "original": "아마 레벨 9 접속 프로토콜이 장착됐던 것 같아. 그래서 내가 접속하는 순간 반작용으로<ELLIPSIS>",
        "patched": "아마 레벨 9 보안 프로토콜이 걸려 있었나 봐요. 접속하는 순간 피드백으로<ELLIPSIS>",
        "reason": "클랭크 존댓말 회복 및 자연스러운 용어",
        "category": "tier3_dialogue_voice"
    },
    {
        "file": "localdat",
        "id": 5230,
        "original": "그런 바보 같은 실수를 하다니 난 멍청인가 봐.",
        "patched": "그런 바보 같은 실수를 하다니, 제 처리장치도 녹슬었나 봐요.",
        "reason": "클랭크 캐릭터다운 자책 대사로 교정",
        "category": "tier3_dialogue_voice"
    },
    {
        "file": "localdat",
        "id": 5233,
        "original": "어떻게 이럴수가! 또 막다른 길이야.",
        "patched": "어떻게 이럴 수가! 또 막다른 길이야.",
        "reason": "'이럴수가' -> '이럴 수가' 띄어쓰기 교정",
        "category": "tier3_dialogue_typo"
    },
    {
        "file": "localdat",
        "id": 5235,
        "original": "역시 예상 대로군.",
        "patched": "역시 예상대로군.",
        "reason": "'예상 대로군' -> '예상대로군' 조사 붙여쓰기 교정",
        "category": "tier3_dialogue_typo"
    },
    {
        "file": "localdat",
        "id": 5245,
        "original": "이것이 바로 모든 내 노력의 대가다. 나는 한 방에 있는 생명체의 지식을 다른 방의 생명체로 옮기는 기술을 개발했다.",
        "patched": "이것이 바로 내 모든 노력의 결실이다. 나는 한 방에 있는 생명체의 지식을 다른 방의 생명체로 옮기는 기술을 개발했다.",
        "reason": "자연스러운 한국어 어순 교정",
        "category": "tier3_dialogue_voice"
    },
    {
        "file": "localdat",
        "id": 5247,
        "original": "이 클론들이 완전히 자라면 나는 라쳇 군대를 이용해 태양계의 모든 지식을 끌어 모을 것이다. 그런 뒤 나는 모든 지식을 흡수해 우주 최고의 두뇌가 될 것이다.",
        "patched": "이 클론들이 완전히 자라면 나는 라쳇 군대를 이용해 온 은하계의 모든 지식을 끌어모을 것이다. 그런 뒤 나는 모든 지식을 흡수해 우주 최고의 두뇌가 될 것이다.",
        "reason": "'태양계' -> '은하계' 원작 설정 반영 및 '끌어모을' 붙여쓰기",
        "category": "tier3_dialogue_voice"
    },
    {
        "file": "localdat",
        "id": 5265,
        "original": "쿼크의 진짜 부모님은 따로 계셨어. 스크런치 말로는 테크노마이트의 고장난 장비 때문에 돌아가셨대.",
        "patched": "쿼크의 진짜 부모님은 따로 계셨어. 스크런치 말로는 테크노마이트의 고장 난 장비 때문에 돌아가셨대.",
        "reason": "'고장난' -> '고장 난' 띄어쓰기 교정",
        "category": "tier3_dialogue_typo"
    },
    {
        "file": "localdat",
        "id": 5283,
        "original": "잘 됐네. 이제 가도 되겠지? 한시간 이내에 <COL:02>포키타루<COL:01>로 오라는 메시지를 받았거든.",
        "patched": "잘 됐네. 이제 가도 되겠지? 한 시간 이내에 <COL:02>포키타루<COL:01>로 오라는 메시지를 받았거든.",
        "reason": "'한시간' -> '한 시간' 띄어쓰기 교정",
        "category": "tier3_dialogue_typo"
    },

    # ---------------- In-game missions, developer extras, weapons, system strings ----------------
    {
        "file": "localdat",
        "id": 497,
        "original": "이것은 우리의 게임에서 창조된 몇가지 실제적인 컨셉아트 입니다.  여기에서 당신은 괴물들과 캐릭터들의 다양함을, 혹은 그들이 모델화 되기전에 어떻게 표현되었는지 볼 수 있을 것이다. ",
        "patched": "이것은 게임 제작 초기에 그린 컨셉 아트입니다. 캐릭터와 몬스터들이 3D 모델로 만들어지기 전에 어떻게 디자인되었는지 한눈에 살펴볼 수 있습니다.",
        "reason": "번역투 직역 투박한 컨셉아트 설명문 자연스러운 개발 비화 해설로 전면 윤문",
        "category": "tier3_flavor_desc"
    },
    {
        "file": "localdat",
        "id": 511,
        "original": "버다닥틸은 초기의 움직이는 '목표물들' 중의 하나이다(우리는 모비스라고 불렀다). 또한 첫번째 시연을 위해 만들어 졌다. 그(그녀?)가 프로토 타입으로 만들어 진 이후로 진행하는데 상당히 많은 돈이 들었다. 만약 우리가 게임에 그를 넣었다면 프레임이 떨어졌을 것이다. 불쌍한 친구, 약간 과체중이라네!",
        "patched": "버다닥틸은 초기에 만든 움직이는 오브젝트(우리는 '모비'라고 부릅니다) 중 하나로, 첫 시연을 위해 제작되었습니다. 하지만 데이터가 너무 정밀해서 연산 부하가 심해 프레임이 떨어졌습니다. 불쌍한 녀석, 용량 초과에 걸린 셈이죠!",
        "reason": "'expensive to run'을 '돈이 들었다'로 오역한 대표적 기계번역 교정",
        "category": "tier3_flavor_desc"
    },
    {
        "file": "localdat",
        "id": 568,
        "original": "<COL:02>흡입 대포<COL:01>는 작은 적들을 빨아인 후, 원소 변환 기술로 강력한 탄환으로 만들어 발사하는 무기입니다. 인기 No.1!",
        "patched": "<COL:02>흡입 대포<COL:01>는 작은 적들을 빨아들인 후, 원소 변환 기술로 강력한 탄환으로 만들어 발사하는 무기입니다. 인기 No.1!",
        "reason": "'빨아인 후' -> '빨아들인 후' 명백한 비문/오타 교정",
        "category": "tier3_weapon_desc"
    },
    {
        "file": "localdat",
        "id": 647,
        "original": "<COL:02>칼리돈에는 테크노마이트 공장이 숨겨져 있는 것 같아요! 단서를 찾기 위해 칼리돈<COL:01> 행성 표면을 탐사하세요.",
        "patched": "<COL:02>칼리돈<COL:01>에는 테크노마이트 공장이 숨겨져 있는 것 같아요! 단서를 찾기 위해 행성 표면을 탐사하세요.",
        "reason": "컬러 태그 범위 비정상 덮어쓰기 교정",
        "category": "tier2_highlight_collision"
    },
    {
        "file": "localdat",
        "id": 649,
        "original": "프로 스카이 보더는 당신에게 자신을 증명하고 싶어하는군요. 그에게 당신의 경주 테크닉을 보여주고 상품도 얻도록 하세요.",
        "patched": "프로 스카이보더가 경주로 승부를 가리고 싶어 합니다. 멋진 레이싱 실력을 보여주고 상품도 획득하세요.",
        "reason": "영어 3인칭 직역투 교정 및 용어 통일",
        "category": "tier3_mission_desc"
    },
    {
        "file": "localdat",
        "id": 653,
        "original": "클랭크는 <COL:02>메탈리스<COL:01>에 고철로 버려졌다! 로봇 검투사를 무찌르고 행성을 빠져나갈 수 있는 방법을 찾으세요.",
        "patched": "클랭크가 <COL:02>메탈리스<COL:01>의 폐기장에 버려졌습니다! 로봇 검투사를 무찌르고 행성을 탈출할 방법을 찾으세요.",
        "reason": "해라체/하십시오체 혼재 문체 통일 및 자연스러운 번역",
        "category": "tier3_mission_desc"
    },
    {
        "file": "localdat",
        "id": 654,
        "original": "굉장한 현금과 상을 획득하세요(선택사양).",
        "patched": "엄청난 볼트와 상품을 획득하세요! (선택 임무)",
        "reason": "'현금' -> 시리즈 고유 화폐 '볼트' 통일 및 TV 쇼 풍 유머 복원",
        "category": "tier3_mission_desc"
    },
    {
        "file": "localdat",
        "id": 655,
        "original": "혹성 <COL:02>메탈리스<COL:01>의 전투 경기장에서 구식 보스를 해치우고 돈과 아이템을 벌도록 하세요.",
        "patched": "행성 <COL:02>메탈리스<COL:01>의 전투 경기장에서 구식 보스를 물리치고 볼트와 아이템을 획득하세요.",
        "reason": "'혹성' -> '행성', '돈' -> '볼트' 용어 표준화",
        "category": "tier3_mission_desc"
    },
    {
        "file": "localdat",
        "id": 661,
        "original": "<JA93:0C>여기<JA93:0D>모든 전 세계의 무대, 그리고 모든 남자들과 여자들 단지 플레이어일 뿐입니다.<JA93:0C>에서<JA93:0D>그들 모두는 나가는 곳과 들어오는 곳을 가지고 있고, <JA93:0C>빠져<JA93:0D>잘나가는 한남자는 많은 부분에서 활동합니다. <JA93:0C>나가<JA93:0D>!",
        "patched": "<JA93:0C>여기<JA93:0D> 온 세상은 무대요, 모든 남녀는 배우일 뿐.<JA93:0C>에서<JA93:0D> 모두 퇴장하고 등장하며, 한 사람이 생애 동안<JA93:0C>빠져<JA93:0D> 여러 역할을 맡는다. <JA93:0C>나가라<JA93:0D>!",
        "reason": "셰익스피어 'As You Like It' 번역기 수준 직역을 품격 있는 문학적 번역과 암호 구절('여기에서 빠져나가라!')로 완성",
        "category": "tier3_mission_desc"
    },
    {
        "file": "localdat",
        "id": 666,
        "original": "의료 시설에서 탈출 하세요. ",
        "patched": "의료 시설에서 탈출하세요.",
        "reason": "'탈출 하세요' -> '탈출하세요' 띄어쓰기 교정",
        "category": "tier3_mission_desc"
    },
    {
        "file": "localdat",
        "id": 679,
        "original": "<COL:02>대이니 문<COL:01>까지 루나를 몰아 붙였어요! 그녀를 붙잡아 어째서 당신을 속였는지 알아내도록 하세요!",
        "patched": "<COL:02>대이니 문<COL:01>까지 루나를 몰아붙였어요! 그녀를 붙잡아 어째서 속였는지 알아내도록 하세요!",
        "reason": "'몰아 붙였어요' -> '몰아붙였어요' 붙여쓰기 및 번역투 정리",
        "category": "tier3_mission_desc"
    },
    {
        "file": "localdat",
        "id": 680,
        "original": "루나를 무력하게 하세요",
        "patched": "루나의 기능을 정지시키세요.",
        "reason": "영어 원문/일문 '機能停止' 맥락 반영 ('무력하게 하세요' -> '기능을 정지시키세요')",
        "category": "tier3_mission_desc"
    },
    {
        "file": "localdat",
        "id": 681,
        "original": "루나에게서 복제 공장의 좌표를 얻었어요. 자, 이제 그녀의 기능을 가능한 한 많이 정지시키도록 하세요!",
        "patched": "루나에게서 복제 공장의 좌표를 얻었습니다. 이제 루나의 기능을 정지시키세요!",
        "reason": "어색한 문장 정리 및 간결화",
        "category": "tier3_mission_desc"
    },
    {
        "file": "localdat",
        "id": 685,
        "original": "테크노마이트 병사들을 모두 처치하기 전에는 경비병이 클랭크를 다시 움직이게 할 수 없어요.테크노마이트 병사들을 모두 해치워서 클랭크를 부활시키도록 하세요.",
        "patched": "테크노마이트 병사들을 모두 처치하기 전에는 경비병이 클랭크를 다시 가동할 수 없습니다. 테크노마이트 병사들을 모두 해치워서 클랭크를 가동시키세요.",
        "reason": "마침표 뒤 띄어쓰기 누락 교정 및 자연스러운 로봇 기동 표현",
        "category": "tier3_mission_desc"
    },
    {
        "file": "localdat",
        "id": 689,
        "original": "오토 디스트럭트 황제는 테크노마이트 건물내 어디엔가 있어요. 그를 찾으세요!",
        "patched": "오토 디스트럭트 황제는 테크노마이트 건물 내 어딘가에 있습니다. 그를 찾으세요!",
        "reason": "'건물내' -> '건물 내' 띄어쓰기 교정",
        "category": "tier3_mission_desc"
    },
    {
        "file": "localdat",
        "id": 710,
        "original": "%d <COL:02>듀얼 래서레이터 <COL:01>탄약",
        "patched": "%d <COL:02>듀얼 래서레이터<COL:01> 탄약",
        "reason": "공백 위치 컬러 태그 외부 이동",
        "category": "tier2_highlight_collision"
    },
    {
        "file": "localdat",
        "id": 711,
        "original": "%d <COL:02>듀얼 래서레이터 <COL:01>탄약",
        "patched": "%d <COL:02>듀얼 래서레이터<COL:01> 탄약",
        "reason": "공백 위치 컬러 태그 외부 이동",
        "category": "tier2_highlight_collision"
    },
    {
        "file": "localdat",
        "id": 718,
        "original": "%d 산성폭격기 탄약 ",
        "patched": "%d <COL:02>산성 폭격기<COL:01> 탄약",
        "reason": "무기명 하이라이트 컬러 태그 누락 보정",
        "category": "tier2_highlight_collision"
    },
    {
        "file": "localdat",
        "id": 719,
        "original": "%d 산성폭격기 탄약 ",
        "patched": "%d <COL:02>산성 폭격기<COL:01> 탄약",
        "reason": "무기명 하이라이트 컬러 태그 누락 보정",
        "category": "tier2_highlight_collision"
    },
    {
        "file": "localdat",
        "id": 952,
        "original": "보호막을 무너뜨리면 적군기지에 유도 신호기를 장착할수 있습니다.",
        "patched": "보호막을 무너뜨리면 적군 기지에 유도 신호기를 장착할 수 있습니다.",
        "reason": "'적군기지', '장착할수' 띄어쓰기 교정",
        "category": "tier3_typo"
    },
    {
        "file": "localdat",
        "id": 966,
        "original": "당신의 영웅적인 행동으로 'DAN'으로 게임할수 있는 자격이 주어집니다.",
        "patched": "영웅적인 활약으로 'DAN'으로 플레이할 수 있는 자격이 주어집니다.",
        "reason": "'게임할수' -> '플레이할 수' 및 자연스러운 문장 교정",
        "category": "tier3_typo"
    },
    {
        "file": "localdat",
        "id": 1696,
        "original": "섬 방사능 반응 물질로 부터 파워 셀을 회수하라. 파워 셀을 회수하여 당신의 발전기를 작동시켜라. 당신 팀의 모든 발전기의 동력을 높여서 탈출 우주선까지 갈수 있도록 하고 적들보다 먼저 행성을 떠나라.",
        "patched": "섬의 방사능 구역에서 파워 셀을 회수하라. 파워 셀을 회수하여 아군의 발전기를 작동시켜라. 아군 팀의 모든 발전기를 가동하여 탈출선까지 갈 수 있도록 하고 적들보다 먼저 행성을 떠나라.",
        "reason": "'당신의 발전기', '갈수' 번역투 및 띄어쓰기 교정",
        "category": "tier3_typo"
    },
    {
        "file": "localdat",
        "id": 1700,
        "original": "네 앞의 모든 적들을 무찔러라. 목표사살수에 첫번째로 도달하여 승리하라. 모든 적군을 무찌르고 왕관을 써라. 지난 장소는 버려지게 된다! ",
        "patched": "눈앞의 모든 적을 쓰러뜨려라. 목표 처치 수에 첫 번째로 도달하여 승리하라. 가장 많은 적을 쓰러뜨려 왕관을 차지하라!",
        "reason": "'목표사살수', '첫번째' 부자연스러운 군사 번역투 교정",
        "category": "tier3_typo"
    },
    {
        "file": "localdat",
        "id": 1702,
        "original": "네 앞의 모든 적들을 무찔러라. 목표사살수에 첫번째로 도달하여 승리하라. 모든 적군을 무찌르고 왕관을 써라. 지난 장소는 버려지게 된다! ",
        "patched": "제한 시간 동안 최대한 많은 적을 쓰러뜨려라. 목표 처치 수에 첫 번째로 도달하여 승리하라. 가장 많은 적을 쓰러뜨려 왕관을 차지하라!",
        "reason": "시간제한 모드 맥락 반영 및 문장 정비",
        "category": "tier3_typo"
    },
    {
        "file": "localdat",
        "id": 1703,
        "original": "네 앞의 모든 적들을 무찔러라. 목표사살수에 첫번째로 도달하여 승리하라. 모든 적군을 무찌르고 왕관을 써라. 지난 장소는 버려지게 된다! ",
        "patched": "제한 시간 동안 최대한 많은 적을 쓰러뜨려라. 목표 처치 수에 첫 번째로 도달하여 승리하라. 가장 많은 적을 쓰러뜨려 왕관을 차지하라!",
        "reason": "시간제한 모드 맥락 반영 및 문장 정비",
        "category": "tier3_typo"
    },
    {
        "file": "localdat",
        "id": 1836,
        "original": "Memory Stick Duo<SYM_TM>가 제거되었습니다. 자동 저장 기능을 사용할수 없습니다.",
        "patched": "Memory Stick Duo<SYM_TM>가 제거되었습니다. 자동 저장 기능을 사용할 수 없습니다.",
        "reason": "'사용할수' -> '사용할 수' 띄어쓰기 교정",
        "category": "tier3_typo"
    }
]

def main():
    existing = json.loads(PATCHES_FILE.read_text(encoding="utf-8"))
    existing_keys = {(p["file"], p["id"]) for p in existing}

    added = 0
    for np in NEW_PATCHES:
        key = (np["file"], np["id"])
        if key not in existing_keys:
            existing.append(np)
            added += 1
        else:
            # Update existing if already present
            for idx, item in enumerate(existing):
                if (item["file"], item["id"]) == key:
                    existing[idx] = np
                    break

    # Sort by file then id
    existing.sort(key=lambda x: (x["file"], x["id"]))

    PATCHES_FILE.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Added {added} new patches. Total patches in catalog: {len(existing)}")

if __name__ == "__main__":
    main()
