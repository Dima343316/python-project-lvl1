install:#Обновление
	poetry install
brain-games:#запуск скрипта
	poetry run brain-games
build:#создание билда
	poetry build
publish:#chmod
	poetry publish --dry-run
package-install:#package
	python3 -m pip install --user dist/*.whl

