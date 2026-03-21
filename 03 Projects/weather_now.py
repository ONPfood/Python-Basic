"""
매일 아침 날씨 알림 프로그램
- Open-Meteo API 사용 (무료, API 키 불필요)
- 매일 지정한 시간에 자동으로 날씨 알림
- 터미널 + 시스템 알림 (선택) 지원
"""

import urllib.request
import urllib.parse
import json
import time
import datetime
import sys

# ─────────────────────────────────────────
#  설정 (여기만 수정하세요)
# ─────────────────────────────────────────
#CITY_NAME   = "Livermore, CA"
CITY_NAME   = "Anchorage, ALASKA"

LATITUDE    = 61.16483    # 위도
LONGITUDE   = -149.87411  # 경도
ALARM_HOUR  = 7         # 알림 시각 (24시간 기준, 7 = 오전 7시)
ALARM_MIN   = 0
# ─────────────────────────────────────────

WMO_CODES = {
    0: "맑음 ☀️",
    1: "대체로 맑음 🌤️", 2: "부분적으로 흐림 ⛅", 3: "흐림 ☁️",
    45: "안개 🌫️", 48: "짙은 안개 🌫️",
    51: "가벼운 이슬비 🌦️", 53: "이슬비 🌦️", 55: "강한 이슬비 🌧️",
    61: "가벼운 비 🌧️", 63: "비 🌧️", 65: "강한 비 🌧️",
    71: "가벼운 눈 🌨️", 73: "눈 🌨️", 75: "강한 눈 ❄️",
    77: "싸락눈 🌨️",
    80: "소나기 🌦️", 81: "강한 소나기 🌧️", 82: "매우 강한 소나기 ⛈️",
    85: "눈 소나기 🌨️", 86: "강한 눈 소나기 ❄️",
    95: "뇌우 ⛈️", 96: "우박 동반 뇌우 ⛈️", 99: "강한 뇌우 ⛈️",
}

def fetch_weather():
    """Open-Meteo에서 날씨 데이터를 가져옵니다."""
    params = urllib.parse.urlencode({
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "current": "temperature_2m,apparent_temperature,relative_humidity_2m,weathercode,windspeed_10m",
        "daily": "weathercode,temperature_2m_max,temperature_2m_min,precipitation_probability_max,sunrise,sunset",
        "timezone": "Asia/Seoul",
        "forecast_days": 1,
    })
    url = f"https://api.open-meteo.com/v1/forecast?{params}"

    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"  ⚠️  날씨 정보를 가져오는 데 실패했습니다: {e}")
        return None

def format_report(data):
    """날씨 데이터를 보기 좋은 문자열로 변환합니다."""
    now   = data["current"]
    daily = data["daily"]

    temp       = now["temperature_2m"]
    feels_like = now["apparent_temperature"]
    humidity   = now["relative_humidity_2m"]
    wind       = now["windspeed_10m"]
    code       = now["weathercode"]
    condition  = WMO_CODES.get(code, f"날씨코드 {code}")

    max_t  = daily["temperature_2m_max"][0]
    min_t  = daily["temperature_2m_min"][0]
    rain_p = daily["precipitation_probability_max"][0]
    rise   = daily["sunrise"][0].split("T")[1]
    sset   = daily["sunset"][0].split("T")[1]

    today  = datetime.datetime.now().strftime("%Y년 %m월 %d일 %A")
    line   = "─" * 44

    report = f"""
{line}
  🌍  {CITY_NAME} 날씨  |  {today}
{line}
  현재 날씨   {condition}
  기온        {temp}°C  (체감 {feels_like}°C)
  최고 / 최저 {max_t}°C  /  {min_t}°C
  습도        {humidity}%
  바람        {wind} km/h
  강수 확률   {rain_p}%
  일출 / 일몰 {rise}  /  {sset}
{line}"""

    # 간단한 옷차림 조언
    tips = []
    if rain_p >= 60:
        tips.append("☂️  우산을 챙기세요!")
    if feels_like <= 5:
        tips.append("🧥  두꺼운 외투가 필요합니다.")
    elif feels_like <= 15:
        tips.append("🧣  가벼운 겉옷을 걸치세요.")
    elif feels_like >= 30:
        tips.append("🧴  자외선 차단제를 바르세요.")
    if wind >= 40:
        tips.append("💨  강풍 주의!")
    if tips:
        report += "\n  " + "  ".join(tips) + "\n" + line

    return report

def notify_system(message):
    """운영체제 알림을 보냅니다 (선택 기능)."""
    try:
        if sys.platform == "darwin":          # macOS
            safe = message.replace('"', '\\"').replace('\n', ' ')
            import subprocess
            subprocess.run(
                ["osascript", "-e",
                 f'display notification "{safe}" with title "오늘의 날씨"'],
                check=False
            )
        elif sys.platform.startswith("linux"):
            import subprocess
            subprocess.run(
                ["notify-send", "오늘의 날씨", message[:100]],
                check=False
            )
        elif sys.platform == "win32":
            # Windows: plyer 라이브러리 필요 (pip install plyer)
            try:
                from plyer import notification
                notification.notify(title="오늘의 날씨", message=message[:200], timeout=10)
            except ImportError:
                pass
    except Exception:
        pass  # 알림 실패해도 프로그램 계속 실행

def run_once():
    """날씨를 한 번 가져와서 출력합니다."""
    print("  날씨 정보를 가져오는 중...", end="\r")
    data = fetch_weather()
    if data:
        report = format_report(data)
        print(report)
        notify_system(report)
    return data is not None

def run_scheduler():
    """매일 지정한 시각에 날씨 알림을 실행합니다."""
    print(f"\n  ✅  날씨 알림 스케줄러 시작")
    print(f"     매일 {ALARM_HOUR:02d}:{ALARM_MIN:02d} 에 {CITY_NAME} 날씨를 알려드립니다.")
    print(f"     종료하려면 Ctrl+C 를 누르세요.\n")

    last_run_date = None

    while True:
        now = datetime.datetime.now()
        today = now.date()

        if (now.hour == ALARM_HOUR and now.minute == ALARM_MIN
                and last_run_date != today):
            print(f"\n  ⏰  알림 시각 도달: {now.strftime('%H:%M')}")
            success = run_once()
            if success:
                last_run_date = today

        # 1분마다 확인 (정각을 놓치지 않도록)
        next_check = 60 - now.second
        time.sleep(next_check)

# ─────────────────────────────────────────
#  실행
# ─────────────────────────────────────────
if __name__ == "__main__":
    if "--now" in sys.argv:
        # 즉시 실행 모드: python daily_weather.py --now
        run_once()
    else:
        # 스케줄러 모드 (기본)
        try:
            run_scheduler()
        except KeyboardInterrupt:
            print("\n\n  👋  날씨 알림 프로그램을 종료합니다.\n")