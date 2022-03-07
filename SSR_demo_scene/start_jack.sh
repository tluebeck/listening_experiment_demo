# Configuration for iMacPro "Lab10"
# with Antelope Orion 32 interface
# Chalmers University of Technology
COMMAND="jackd -d coreaudio -r 48000"
#COMMAND="jackd -d coreaudio -d 'com.antelope.23e5a04014100000.Orion 32' -r 48000"

# On macOS, use this:
osascript -e "tell app \"Terminal\" to do script \"${COMMAND}\""
