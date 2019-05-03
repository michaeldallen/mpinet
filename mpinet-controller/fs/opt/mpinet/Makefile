include makelib

INVENTORY := --inventory=inventory/mpinet.inventory

ifdef INVENTORY_LIMIT
OPTION_LIMIT := --limit=${INVENTORY_LIMIT}
endif

%.natick :
	env INVENTORY_LIMIT=natick $(MAKE) $(basename $@ .natick)

%.brookline :
	env INVENTORY_LIMIT=natick $(MAKE) $(basename $@ .brookline)

do.ping :
	ansible-playbook ${INVENTORY} ping.yml ${OPTION_LIMIT}

do.apt :
	ansible-playbook ${INVENTORY} apt.yml ${OPTION_LIMIT}

do.docker :
	ansible-playbook ${INVENTORY} docker.yml ${OPTION_LIMIT}
