var log = require('../core/log');

const DECISION_LONG = 'long'
const DECISION_SHORT = 'short'
const DECISION_HODL = 'hodl'

// Let's create our own strat
var strat = {};

// Prepare everything our method needs
strat.init = function() {
  this.input = 'candle';
  this.requiredHistory = 0;
  this.decision = DECISION_HODL;
}

// What happens on every new candle?
strat.update = function(candle) {
  // Nothing to do
}

// For debugging purposes.
strat.log = function() {
  log.debug('DECISION BRAINS HATH SPOKEN:');
  log.debug('\t', this.decision);
}

// Based on the newly calculated
// information, check if we should
// update or not.
strat.check = function() {
  var cp = require('child_process');
  var py = cp.spawnSync('python', ['decisionbrains/interface.py'], { encoding : 'utf8' });
  this.decision = py.stdout;
  if(this.decision === DECISION_HODL) {
    this.advice();
  } else {
    this.advice(this.dicision);
  }
}

module.exports = strat;
