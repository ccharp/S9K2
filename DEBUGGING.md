# Debug API server and Website Simultaneously

## Dependencies
1. VSCode
2. Chrome

## Launch the API server in the VSCode debugger
1. Open VSCode at project root.
2. Click Debug tab of VSCode.
3. Choose "Launch API Debug" as debugging configuration.
4. Hit F5 or click the "play" button to start debugging API server (opens on port 3000).
5. You should now see logs appearing in the "DEBUG CONSOLE" of the VSCode debugger.

## Lauch the Website in Chrome debugger
1. Click the "TERMINAL" tab (next to the "DEBUG CONSOLE" tab you just saw API server logs coming out of).
2. Enter the command:
```
./run-website-debug.sh
```
3. Chrome should open up with the site's homepage on port 8080.
4. Hit F12 to open the Chrome debugger.
5. Under the "Sources" tab, expand the webpack:// folder to see the *.vue scripts and set breakpoints in them. Note that many of these are sourcemaps and other webpack internal files, setting breakpoints in them won't be useful. Look for the original source files and put your breakpoints there.

## For Great Justice
You should now be able to hit breakpoints in the API (through VSCode) and breakpoints in the website (through Chrome) simultaneously.
