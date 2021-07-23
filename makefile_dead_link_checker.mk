## Testing Production systems will check outside links
## Testing non-Production systems will not check outside links & HAWK cookie
## will be used.
TEST_ENV ?= DEV
BASIC_AUTH := $(shell echo -n $($(TEST_ENV)_BASICAUTH_USER):$($(TEST_ENV)_BASICAUTH_PASS) | base64)
ifeq ($(TEST_ENV),PROD)
	AUTH=
	TEST_OUTSIDE=--test-outside
else
	ifeq ($(TEST_ENV),Beta)
		AUTH=--header='Authorization: Basic ${BASIC_AUTH}'
		TEST_OUTSIDE=
	endif
	ifeq ($(TEST_ENV),STAGE)
		AUTH=--header='Authorization: Basic ${BASIC_AUTH}'
		TEST_OUTSIDE=
	endif
	ifeq ($(TEST_ENV),DEV)
		AUTH=--header='Authorization: Basic ${BASIC_AUTH}'
		TEST_OUTSIDE=
	endif
endif
