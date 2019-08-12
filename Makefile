init:
	npm install --global concurrently
	npm install --global --unsafe-perm node-sass
	npm install --global node-sass-watcher
	npm install --global postcss-cli autoprefixer

run:
	@concurrently "dev_appserver.py . --port=9090 --host=home # nosync"
