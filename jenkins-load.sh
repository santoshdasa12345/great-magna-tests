### START ARGUMENT AND FLAG VALIDATION ###
while getopts ":e:t:u:s:r:" option; do
  case $option in
    e)
      ENV="$OPTARG"
      ;;
    t)
      TEST="$OPTARG"
      ;;
    u)
      USERS="$OPTARG"
      ;;
    s)
      SPAWN="$OPTARG"
      ;;
    r)
      RUN="$OPTARG"
      ;;
    *)
      echo "Usage: $0 [-e environment] [-t test] [-u users] [-s spawn] [-r run]"
      exit 1
      ;;
  esac
done

incorrect_init(){
echo "#######################################################\n\n\
Please pass an environment with the -e flag and test with the -t flag.\n\n\
Useage example ./start-docker -e local -t load
Environemnt options are:\n\n\
- dev\n\
- uat\n\
- prod\n\n\
Test options are:\n\n\
- load\n\
- smoke\n\
- browser\n\
- functional\n\n\
#######################################################\n\n"
}


### END ARGUMENT AND FLAG VALIDATION ###


case $TEST in
    load | smoke | browser | functional)
        getEnvs="${processingSecretsPrefix}${TEST}${processingSecretsSuffix}"
        ;;
    *)
        incorrect_init
        exit 1
        ;;
esac

case $ENV in
    dev | uat | prod)
        echo "#!/usr/bin/env bash\nexport TEST_ENV=${ENV}" > compose/.env
        ;;
    *)
        incorrect_init
        exit 1
        ;;
esac
### END CF AUTH ###

locust_error (){
echo "#######################################################\n\n \
Locust error \n\n\
#######################################################\n\n"
}


run_load_test (){
echo "#######################################################\n\n \
Running load lests
#######################################################\n\n"

export NUM_USERS="$USERS"
export SPAWN_RATE="$SPAWN"
export RUN_TIME="$RUN"
export LOCUST_FILE="locustfile_domestic.py"
export HTML_FILE="loadtest_report.html"

{ 
    make locust
    open ./loadtest_report.html
} || { 
    locust_error 
}

}

case "$TEST" in
    load )
        run_load_test
        ;;
    *)
        echo "Unknown test type: ${TEST}"
        ;;
esac

echo "#######################################################\n\n \
*** Tests complete *** \n\n\
#######################################################\n\n"
exit 1





