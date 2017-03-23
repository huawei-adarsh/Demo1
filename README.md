# Demo1
This is the test app for testing L3VPN Demo1.

ONOS Setup scripts are present in "/yangdemo/demo1/src/main/resources/Onos_Env_Setup_Scripts"
# PREREQUISITE
# onos and onos-yang-tools should be in /home/root1
# keep yangdemo app in /home/root1
# put setup.sh in /home/root1
# build onos and onos-yang-tools
# run setup.sh 
#!/usr/bin/env bash
On CLI do "ok clean "
Activate below apps:
app activate org.onosproject.yang
app activate org.onosproject.yangdemo
app activate org.onosproject.yms
app activate org.onosproject.config
app activate org.onosproject.restconf
app activate org.onosproject.protocols.restconfserver



L3VPN Yang files are present in "DEMO1/yangdemo/yangmodel/src/main/yang/".
Json files with test cases and prerequiste's are availbale in "Demo1/yangdemo/demo1/src/main/resources".
