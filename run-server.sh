export NVM_DIR="~/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
cd $LIZARD_HOME
pm2 start gekko.js -- --ui
