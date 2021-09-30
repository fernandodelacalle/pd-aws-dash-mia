

aws configure
output text


source venv/bin/activate
python3.7 -m uvicorn app:app --host 0.0.0.0 --port 80



scp -i test.pem extracted_2018_RV_TICK_A_MFII_RV_TICK_A_20180319.TXT ec2-user@ec2-52-47-111-77.eu-west-3.compute.amazonaws.com:/home/ec2-user

