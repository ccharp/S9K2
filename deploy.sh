KEYPATH="~/.ssh/garage01.pem"
REMOTE="ubuntu@ec2-18-217-99-159.us-east-2.compute.amazonaws.com"

rsync -avz -e "ssh -i $KEYPATH" --progress ./ $REMOTE:~/lizard/

RUN_LIZARD_RUN='cd /home/ubuntu/lizard; ./run_server.sh'
ssh -t -i $KEYPATH $REMOTE $RUN_LIZARD_RUN

