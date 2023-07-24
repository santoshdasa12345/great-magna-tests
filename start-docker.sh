### START ARGUMENT AND FLAG VALIDATION ###
while getopts ":e:t:" option; do
  case $option in
    e)
      ENV="$OPTARG"
      ;;
    t)
      TEST="$OPTARG"
      ;;
    *)
      echo "Usage: $0 [-e environment] [-t test]"
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


### START ENVS ###

get_load_envs (){
cf ssh great-cms-$ENV -c \
    "python -c \
        'import os, json; \
        secrets=[ \
            \"AWS_ACCESS_KEY_ID\", \
            \"AWS_ACCESS_KEY_ID_DATA_SCIENCE\", \
            \"AWS_COGNITO_POOL_ID\", \
            \"AWS_S3_HOST\", \
            \"AWS_S3_REGION_NAME\", \
            \"AWS_S3_REGION_NAME_DATA_SCIENCE\", \
            \"AWS_S3_TIMEOUT\", \
            \"AWS_SECRET_ACCESS_KEY\", \
            \"AWS_SECRET_ACCESS_KEY_DATA_SCIENCE\", \
            \"AWS_STORAGE_BUCKET_NAME\", \
            \"AWS_STORAGE_BUCKET_NAME_DATA_SCIENCE\", \
        ]; \
        vars={key:value for (key,value) in os.environ.items()}; \
        v=\" \".join(\"{}={}\".format(s, vars[s]) for s in secrets); \
        print(v)'"
}

add_secrets_to_template (){
    echo "add_secrets_called with $1"
    # vars=($1)
    # for var in "${vars[@]}"
    #     do
    #         echo $var >> ./env_vars/$TEST/secrets-do-not-commit
    #     done
}

echo "#######################################################\n\n \
Creating secrets... \n\n\
#######################################################\n\n"
processingSecretsPrefix="add_"
processingSecretsSuffix="_envs"

case "$TEST" in
    load | smoke | browser | functional)
        getEnvs="${processingSecretsPrefix}${TEST}${processingSecretsSuffix}"
        add_secrets_to_template "$getEnvs"
        ;;
    *)
        echo "Unknown test type: ${TEST}"
        ;;
esac

### END ENVS ###

### START CF AUTH ###
cf_cli_not_found(){
echo "#######################################################\n\n \
Cloud Foundry CLI could not be found. Please install to continue. \n\n\
#######################################################\n\n"
exit 1 
}

cloud_foundry_signin_sso () {
echo "#######################################################\n\n \
Lets get you signed into Cloud Foundry. \n\n\
#######################################################\n\n"

make cf-signin-sso ${user_email}

}

echo "#######################################################\n\n \
Lets get started \n\n\
#######################################################\n\n"

echo "Enter Your Email: "
read user_email

echo "\n#######################################################\n\n \
Welcome ${user_email}! \n\n\
#######################################################\n\n"

echo "#######################################################\n\n \
Checking for Cloud Foundry CLI... \n\n\
#######################################################\n\n"
cf logout || cf_cli_not_found

case $TEST in
    load | smoke | browser | functional)
        getEnvs="${processingSecretsPrefix}${TEST}${processingSecretsSuffix}"
        add_secrets_to_template "$getEnvs"
        ;;
    *)
        incorrect_init
        exit 1
        ;;
esac

case $ENV in
    dev | uat | prod)
        echo "#!/usr/bin/env bash\nexport EMAIL=${user_email}\nexport TEST_ENV=${ENV}" > compose/.env
        ;;
    *)
        incorrect_init
        exit 1
        ;;
esac

make cf-$TEST-$ENV-signin-sso ${user_email}

### END CF AUTH ###


echo "#######################################################\n\n \
Starting docker build... \n\n\
#######################################################\n\n"
make build compose/docker-compose-$TEST.yml

echo "#######################################################\n\n \
Logout of Cloud Foundry \n\n\
#######################################################\n\n"
cf logout

locust_error (){
echo "#######################################################\n\n \
Locust error \n\n\
#######################################################\n\n"
}


run_load_test (){
echo "#######################################################\n\n \
Running load lests
#######################################################\n\n"

read -p 'Number of concurrent users: ' number_of_concurrent_user
read -p 'Spawn rate: ' spawn_rate
read -p 'Runtime (eg 20s): ' run_time

export NUM_USERS="$number_of_concurrent_user"
export SPAWN_RATE="$spawn_rate"
export RUN_TIME="$run_time"
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





