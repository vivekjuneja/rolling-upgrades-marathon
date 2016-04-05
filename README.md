# rolling-upgrades-marathon
Test Graceful Rolling upgrades using Marathon

We demonstrate how rolling upgrade is implemented by Marathon for a Mesos Cluster. We have two simple Python flask applications - Caller and Callee. The Caller application is provided with the location of the Callee. The Callee application returns a test JSON message, with a configurable delay, measured in number of seconds.

Caller invokes Callee. Both applications are deployed as Docker Containers. Using Caller and Callee, we can test scenario where the Caller application is upgraded through rolling mechanism via Marathon, in the midst of transaction. The goal is to have a graceful upgrade of the Caller application, without causing an ongoing transaction with Callee application to break. 


