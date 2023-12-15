install: # Install poetry project
	poetry install

brain-games: # Run module "brain_games"
	poetry run brain-games

build: # Build poetry project
	poetry build

publish: # Imitate project publishing
	poetry publish --dry-run

package-install: # Install package in user environment
	python3 -m pip install --user dist/*.whl

package-reinstall: # Reinstall package in user environment
	python3 -m pip install --user dist/*.whl --force-reinstall
