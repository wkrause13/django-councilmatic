# Build Tools for Councilmatic

## Requirements
- Ansible installed locally
- Virtualbox
- Vagrant 1.7 or greater

# Instructions
If you're not familiar with vagrant, just run `vagrant up` when in the build_tools directory. 
If you make changes to the playbook, just run `vagrant provision`

`vagrant ssh` gets you into your local box and `vagrant halt` shuts everything down gracefully. 

## Todo
- [ ] Decouple virtualenv from vagrant so playbook can be used on VPS services, likely need to create a new linux user
