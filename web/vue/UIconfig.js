// This config is used in both the
// frontend as well as the web server.

// see https://github.com/askmike/gekko/blob/stable/docs/installing_gekko_on_a_server.md

const DEBUG_CONFIG = {
  headless: true,
  api: {
    host: '127.0.0.1',
    port: 3000,
    timeout: 120000 // 2 minutes
  },
  ui: {
    ssl: false,
    host: 'localhost',
    port: 3000,
    path: '/'
  },
  adapter: 'sqlite'
}

const PRODUCTION_CONFIG = {
  headless: true,
  api: {
    host: '127.0.0.1',
    port: 3000,
    timeout: 120000 // 2 minutes
  },
  ui: {
    ssl: true,
    host: 'ec2-18-217-99-159.us-east-2.compute.amazonaws.com',
    port: 443,
    path: '/'
  },
  adapter: 'sqlite'
}

getExports = function (options) {
  var debug = !!options && !!options.debug ? options.debug : false
  if(!!debug) {
    return DEBUG_CONFIG
  }
  else {
    return PRODUCTION_CONFIG
  }
};

if(typeof window === 'undefined'){
  module.exports = getExports
}
else {
  window.CONFIG = getExports({debug: true})
}
