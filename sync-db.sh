KEYPATH="~/.ssh/garage01.pem"
REMOTE="ubuntu@ec2-18-217-99-159.us-east-2.compute.amazonaws.com"

mkdir history
rsync -avz -e "ssh -i $KEYPATH" --progress $REMOTE:/home/ubuntu/gekko/history/ ./history/

