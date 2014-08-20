# How to package a Python Application in a DevOps Approach

All that DevOps attempts to do is deliver turn-key services to businesses.  All else is vanity.

Ideally, this process needs to start before the first line of code is written.

If a Dev team, in this case writing a Python application, can deliver a fully functional package which 
the Ops team can deploy as simply as Apache or Mongo, then the config management layer will be as simple as:

* Add business repository
* Install package
* Configure package (set active runlevels, add configuration files)
* Start service

This reduces complexity at the deployment stage, which remains the highest risk stage to the business.

## Project Contents

### Build

Instructions for listing and installing dependencies.

### Test

Instructions for unit and functional testing.

### Package

Instructions for packaging, and pre/post install/uninstall scripts.

### Deploy

Instructions for deploying a local service (on the developer's machine) and a remote service (not populated by default)

### Clone

A utility script for creating a new, renamed, repository from this one.

### Lib

Holding area for pip dependencies.

### Logs

Holding area for logs.  This directory is removed at package install and replaced with a symlink to a location under /var/logs/.

### Service

The System V init script.  This will be symlinked at install of the package to the /etc/init.d location appropriate for your package name.

Later, the SystemD script will be added.

### Source

Your project code.  Initially, a simple Hello World application is provided.

## Cloning

To create a repository of your own, run this script with a single parameter, which will be the name of the project.

This will remove the clone directory and the git information, then rename the project and re-initialise a git repository ready for use.

Optionally, you can specify an upstream location and clone will also execute the first push.

## Build Order


