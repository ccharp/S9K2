var fork = require('child_process').fork;

module.exports = (mode, config, callback) => {
  // If we don't set execArgv to some value, it will inherit the
  // parent's execArgv. When debugging, this includes the flag
  // "--inspect-brk=3593" which breaks the child script.
  var child = fork(__dirname + '/child', [], {execArgv: []});

  // How we should handle client messages depends
  // on the mode of the Pipeline that is being ran.
  var handle = require('./messageHandlers/' + mode + 'Handler')(callback);

  var message = {
    what: 'start',
    mode: mode,
    config: config
  }

  child.on('message', function(m) {

    if(m === 'ready')
      return child.send(message);

    handle.message(m);
  });

  child.on('exit', handle.exit);

  return child;
}