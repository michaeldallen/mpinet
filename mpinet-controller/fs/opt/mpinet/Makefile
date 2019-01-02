include makelib

INVENTORY := --inventory=inventory/mpinet.inventory

inventory_ping :
	ansible ${INVENTORY} -m ping --user=root all

do.apt :
	ansible-playbook ${INVENTORY} apt.yml ${LIMIT}

do.docker :
	ansible-playbook ${INVENTORY} docker.yml ${LIMIT}
