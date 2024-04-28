from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def upload():
    if request.method == 'POST':
        # POST 요청에서 JSON 데이터 추출
        data = request.json

        statusCode = data.get('statusCode')

        if statusCode == 1:
            # 받아온 data 확인
            print(data)

            # 스타일 생성기 호출 부분
            # voice_vector = styleGenerator(images)
            voice_vector = title + " & " + str(statusCode)
            return voice_vector
        elif statusCode == 2:
            # 받아온 data 확인
            print(data)

            # 스타일 생성기 호출 부분
            # TTS_audio = TTS(data.get('voiceVector'))
            TTS_audio = "audio.wav"
            
            return TTS_audio
    else:
        return '이 페이지는 POST 요청만 지원합니다.'

if __name__ == '__main__':
    app.run(debug=True)
