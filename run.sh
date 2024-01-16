nohup python3 face_recognition_script.py &
wait $!
nohup python3 buttons.py &
nohup python3 working_tracking.py &
nohup python3 telegram_command.py &