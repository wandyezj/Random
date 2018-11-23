# Scripts

* Use Command line parameters, do not prompt the user
    * This makes it substantially easier to debug programs
    * if possible allow a .json file to include the parameters
    * have all input be determined up front
* By default show help
    * Accidentaly clicks should not run the script
    * help should include the command line parameter options and example usage
* Have intermediate output or logging to help debug the script later
    * it helps if the script is broken into discrete stages
* scripts must be deterministic


# typescript standard
* use npm
* use ts-node to execute typescript
* use tslint to enforce rules
* place inputs into 