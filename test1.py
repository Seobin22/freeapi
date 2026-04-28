from openai import OpenAI

# ==========================================
# 1. 설정 및 변수 (여기만 수정해서 사용하세요!)
# ==========================================

# [내 API 정보]
MY_API_KEY = ""
BASE_URL = "https://factchat-cloud.mindlogic.ai/v1/gateway"

# [질문 설정] - 그때그때 질문 내용을 바꾸세요
USER_QUESTION = "영남대 컴퓨터공학과 2학년이 해야할일을 4000자 내외로 알려줘."

# [모델 선택] - 아래 주석의 모델 ID 중 하나를 골라 넣으세요
# (예: 'claude-sonnet-4-6', 'gpt-5.4-nano', 'gemini-2.5-pro' 등)
TARGET_MODEL = "gpt-5.4-nano"
#  "gpt-5.4-nano":0크레딧  "gemini-2.5-pro":9크레딧
# ==========================================
# 🔍 사용 가능한 모델 리스트 (복사해서 위 TARGET_MODEL에 넣으세요)
# ==========================================
"""
확인된 모델들: ['gpt-5.3-chat-latest', 'gpt-5.5', 'gpt-5.4', 'gpt-5.4-mini', 'gpt-5.4-nano', 'gpt-5.2-chat-latest', 'gpt-5.2', 'gpt-5.1-chat-latest', 'gpt-5.1', 'gpt-5-chat-latest', 'gpt-5', 'gpt-5-mini', 'accounts/fireworks/models/gpt-oss-120b', 'gpt-5.3-codex', 'gpt-5.1-codex-max', 'gpt-5.2-codex', 'claude-sonnet-4-6', 'claude-sonnet-4-5-20250929', 'claude-opus-4-7', 'claude-opus-4-6', 'claude-opus-4-5-20251101', 'claude-haiku-4-5-20251001', 'gemini-3.1-pro-preview', 'gemini-3.1-flash-lite-preview', 'gemini-3-flash-preview', 'gemini-2.5-flash', 'gemini-2.5-pro', 'grok-4-1-fast', 'grok-3-mini', 'grok-4', 'google/gemma-4-31B-it', 'google/gemma-3-27b-it', 'meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8', 'sonar-pro', 'sonar-reasoning-pro', 'solar-pro3', 'solar-pro2', 'LGAI-EXAONE/K-EXAONE-236B-A23B']
________
[클로드 계열 - 똑똑하고 논리적임]
- 'claude-sonnet-4-6' (문서 추천 모델)
- 'claude-opus-4-7' (가장 고성능)
- 'claude-haiku-4-5-20251001' (빠르고 가벼움)

[GPT 계열 - 범용성이 좋음]
- 'gpt-5.5' / 'gpt-5.4'
- 'gpt-5.4-mini' / 'gpt-5.4-nano' (크레딧 아끼기용)

[구글 제미나이 - 긴 문맥 이해에 강함]
- 'gemini-2.5-pro' 
- 'gemini-3.1-pro-preview'

[기타 특수 모델]
- 'LGAI-EXAONE/K-EXAONE-236B-A23B' (국산 모델, 한국어 특화)
- 'grok-4' / 'sonar-pro' (최신 트렌드/검색 특화)
"""

# ==========================================
# 2. 실행 로직 (수정할 필요 없음)
# ==========================================

client = OpenAI(api_key=MY_API_KEY, base_url=BASE_URL)

def run_test():
    print(f"🚀 테스트 시작!")
    print(f"📍 사용 모델: {TARGET_MODEL}")
    print(f"❓ 질문 내용: {USER_QUESTION}")
    print("-" * 50)

    try:
        response = client.chat.completions.create(
            model=TARGET_MODEL,
            messages=[{"role": "user", "content": USER_QUESTION}]
        )
        
        # 답변 출력
        answer = response.choices[0].message.content
        print(f"🤖 AI 답변:\n{answer}")
        
        # 영수증(토큰) 출력
        print("-" * 50)
        print(f"📊 사용 리포트")
        print(f" - 소모 토큰: {response.usage.total_tokens} (질문: {response.usage.prompt_tokens}, 답변: {response.usage.completion_tokens})")

    except Exception as e:
        print(f"❌ 에러가 발생했습니다: {e}")
        
        
def run_free_check(count=5):
    """무료 구간 확인용 함수: 짧은 질문을 여러 번 던짐"""
    print(f"🧪 [무료 체크 모드] {count}회 반복 호출 시작...")
    print(f"📍 현재 모델: {TARGET_MODEL}")
    print("이 작업이 끝나고 웹사이트의 크레딧 변화를 확인하세요.")
    print("-" * 50)

    for i in range(1, count + 1):
        try:
            # 아주 짧은 토큰만 사용하도록 설정
            response = client.chat.completions.create(
                model=TARGET_MODEL,
                messages=[{"role": "user", "content": "hi"}],
                max_tokens=5 # 답변 길이를 강제로 제한해서 토큰을 아낍니다
            )
            print(f"[{i}/{count}] 호출 성공 - 소모 토큰: {response.usage.total_tokens}")
        except Exception as e:
            print(f"[{i}/{count}] 실패: {e}")        

if __name__ == "__main__":
    now_credit=2924
    print(now_credit,"\n")
    #런테스트는 일반질문용
   # run_test()
   # 무료 구간(1점이라도 깎이는지)을 확인하고 싶을 때는 아래 줄을 사용
    #run_free_check(count=100) # 100번 반복 호출해봅니다
