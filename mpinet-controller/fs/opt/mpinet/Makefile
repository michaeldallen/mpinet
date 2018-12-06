include makelib

INVENTORY := --inventory=inventory/mpinet.inventory

inventory_ping :
	ansible ${INVENTORY} -m ping --user=root all


do_docker :
	ansible-playbook ${INVENTORY} docker.yml
