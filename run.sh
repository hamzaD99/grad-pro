source .venv/car_monitor/bin/activate
nohup python3 buttons.py &
nohup python3 face_recognition_script.py &
nohup python3 telegram_command.py &