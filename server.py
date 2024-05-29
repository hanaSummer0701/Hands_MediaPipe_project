from flask import Flask, render_template, Response, jsonify
import cv2
import mediapipe as mp
import numpy as np
import os
from classgo import Moving
from recognition_lib import util
from recognition_part import recognition
from tensorflow.keras.models import load_model
from game1 import generate_frames, get_score, get_position

app = Flask(__name__)

# score = 0

# 글로벌 변수로 설정
toggle = 0

game_data = {
    '그림자 놀이터': {
        'title': '그림자 놀이터',
        'image': 'game1.png',
        'description': '손으로 동물과 모양을 만들어 보세요!'
    },
    '두더지 잡기': {
        'title': '두더지 잡기',
        'image': 'game1.png',
        'description': '주어진 단어와 같은 단어를 가지고 있는 두더지를 잡아보세요!'
    },
    '산성비': {
        'title': '산성비',
        'image': 'game1.png',
        'description': '제시된 알파벳과 같은 글자를 고르는 게임입니다.'
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game/<game_name>')
def game(game_name):
    global game_data
    if game_name in game_data:
        return render_template('game.html', game=game_data[game_name])
    else:
        return "Game not found", 404
    
@app.route('/game_play/<game_name>')
def game_play(game_name):
    global game_data
    if game_name in game_data:
        return render_template('game_video.html', game=game_data[game_name], score=get_score(), position=get_position())
    else:
        return "Game not found", 404

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/get_position')
# def get_position():
#     # 여기서 실시간으로 좌표 데이터를 업데이트
#     global position
#     return jsonify(position)

# toggle 값을 반환하는 엔드포인트 추가
@app.route('/toggle_status')
def toggle_status():
    global toggle
    return jsonify({'toggle': toggle})

if __name__ == '__main__':
    app.run(debug=True)