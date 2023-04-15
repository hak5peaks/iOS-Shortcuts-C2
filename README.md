# iOS-C2

iOS C2 Beta 

Windows Setup Requirements: 

1. Ensure OpenSSH Server is installed on the machine, go to Settings -> Apps -> Optional Features, Search to see if open SSH server is installed, if not use "Add a Feature and install open SSH Server"
2. Once install verify that open SSH Server and OpenSSH Authentication Agent is running inside services
3. Ensure you have changed your sshd_config files and have these settings selected | AllowAgentForwarding yes | AllowTcpForwarding yes |  PermitTTY yes | PermitTunnel yes
4. Make sure there are in and outbound firewall rules to prevent firewalls preventing SSH
5. Install the paramiko python package in the same directory as the python script

-----------------------------------------------------------------------------
