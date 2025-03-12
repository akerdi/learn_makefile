# usage: make ANDROID_NDK=/mnt/c/Users/shaohong.jiang/AppData/Local/Android/Sdk/ndk/android-ndk-r25c-linux CMAKE_BUILD_TYPE=MinSizeRel NEED_TEST=1 -f ./sample/makefile_for_asdk.mk

# "ARTIFACTORY_TO_PASS": "${CHENGDU_PASS}", # deploy password
# "NEED_TEST": "1", # enable testing after build
# "CMAKE_BUILD_TYPE": "MinSizeRel", # build type
# "ANDROID_NDK": "/mnt/c/Users/shaohong.jiang/AppData/Local/Android/Sdk/ndk/android-ndk-r25c-linux", # specify NDK
# "build_data_version": "Mazda_25074A_test" # optional, change variable

MK_FILE_DIR := $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
include ${MK_FILE_DIR}/conf.mk
ROOT_DIR := ${PWD}

project_dir := asdk
build_date := $(shell date +'%Y%m%d')
build_data_version := $(shell cd ${project_dir}/data && ./script/get_version.sh)
build_sdk_version := $(shell cd ${project_dir} && ./get_version.sh)

build_post_test := 1
build_dir := cmake-build-x64-${CMAKE_BUILD_TYPE}

all: print_build_info build_data_and_sdk
	${MAKE} -f ${MK_FILE_DIR}/makefile_for_asdk.mk build_post
	@echo "Success!"

print_build_info:
	@echo "build_date: ${build_date}"
	@echo "build_data_version: ${build_data_version}"
	@echo "build_sdk_version: ${build_sdk_version}"

build_data_and_sdk: build_data build_asdk

build_data: verify_dp_nlu
	cd ${project_dir}/data && ASDK_DIR=${ROOT_DIR} ./script/release.sh
	echo "data" > ${project_dir}/data/data.txt

build_post: test deploy_task

build_asdk:
	python3 ${project_dir}/build_sdk.py
	echo "sdk" > ${project_dir}/sdk.txt

verify_dp_nlu:
	cd ${project_dir}/data && ./script/verify_files.py

deploy_task:
	SDK_VERSION=${build_sdk_version} \
	DATA_VERSION=${build_data_version} \
	CUR_DATE=${build_date} \
	ARTI_TO_PASS=$${ARTIFACTORY_TO_PASS} \
	${MK_FILE_DIR}/release_to_artifactory.py

get_cur_date:
	@echo "${build_date}"

get_db_version:
	@echo "${build_data_version}"

get_sdk_version:
	@echo "${build_sdk_version}"

test:
ifeq (${build_post_test},1)
	echo "testing"
endif

clean:
	echo "Done clean"
