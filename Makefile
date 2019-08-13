init:
	npm install --global concurrently
	npm install --global --unsafe-perm node-sass
	npm install --global node-sass-watcher
	npm install --global postcss-cli autoprefixer

run:
	@concurrently \
		"node-sass-watcher static/app.css.sass --command 'make sass-to-css file=<input>'" \
		"dev_appserver.py . --port=9090 --host=home # nosync"

ci-test:
	@flake8 --exclude=natrix.py
	@python test.py

sass-to-css:
	@node-sass $(file) `echo $(file) | sed 's#\.sass$$##'` \
		--indented-syntax                                    \
		--output-style expanded                              \
		--include-path `echo $(file) | sed 's#/[^/]\+$$##'`  \
		--include-path `npm root --global`
	@postcss `echo $(file) | sed 's#\.sass$$##'`   \
		--output `echo $(file) | sed 's#\.sass$$##'` \
		--use autoprefixer --no-map
