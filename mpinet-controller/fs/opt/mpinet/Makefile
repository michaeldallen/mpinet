include makelib

INVENTORY := --inventory=inventory/mpinet.inventory

ifdef INVENTORY_LIMIT
OPTION_LIMIT := --limit=${INVENTORY_LIMIT}
endif

do.ping :
	ansible ${INVENTORY} -m ping --user=root all ${OPTION_LIMIT}

do.apt :
	ansible-playbook ${INVENTORY} apt.yml ${OPTION_LIMIT}

do.docker :
	ansible-playbook ${INVENTORY} docker.yml ${OPTION_LIMIT}
