all:
	echo "Use 'make cw' to create coursework template or 'make lab' to create labwork template"

cw: ## Init the new coursework repo
	test -s main.tex && { echo "main.tex exist! Aborting."; exit 1; } || echo "Copying files"
	cp -r templates/images .
	cp templates/cw/* .
	cp -f templates/gitignore.template .gitignore
	cp -f templates/Makefile.template Makefile

lab: ## Init the new labwork repo
	test -s main.tex && { echo "main.tex exist! Aborting."; exit 1; } || echo "Copying files"
	cp -r templates/images .
	cp templates/cw/* .
	cp templates/lab/* .
	cp -f templates/gitignore.template .gitignore
	cp -f templates/Makefile.template Makefile
