# 1.0.0 (2025-04-10)


### Bug Fixes

* add activity factor calculation ([5097fe8](https://github.com/yifattih/rmr-projection-api/commit/5097fe84327a829d5d261cc492abb051d374cfdf))
* add time projection to results dict ([6906b37](https://github.com/yifattih/rmr-projection-api/commit/6906b3712749bc4fa9f9f5c3cd305df2ede22108))
* add unit tests ([00d0432](https://github.com/yifattih/rmr-projection-api/commit/00d04328c37a09dc6b0fdefbf930bb8240d429a7))
* **api:** add output data model in schemas.py for pydantic validation ([be73871](https://github.com/yifattih/rmr-projection-api/commit/be73871825eea17c16f4e98842f1d5349045419f))
* **api:** rename input data model to align with updated pydantic schema ([0853a8a](https://github.com/yifattih/rmr-projection-api/commit/0853a8aaf2026f85b0c8b87cbd6c8ee347f7cb8b))
* **api:** update equations module error handler to include invalid input in error ([464ac3f](https://github.com/yifattih/rmr-projection-api/commit/464ac3fa1d0389405252332bc68f5e6202c8d070))
* **app-bmr calculator:** change package structure ([8d027c7](https://github.com/yifattih/rmr-projection-api/commit/8d027c7d2bf44ea0d0654d1e977d8cceb53e973e))
* **backend:** change back sex male for men ([e9394c3](https://github.com/yifattih/rmr-projection-api/commit/e9394c3a035028bc453c8d8b2894a994167aac2d))
* change badges ([283a38a](https://github.com/yifattih/rmr-projection-api/commit/283a38a081085612dfee7d4aedd9cd7488c8dce6))
* **core:** isolate monolith backend into microservice ([a878e07](https://github.com/yifattih/rmr-projection-api/commit/a878e0735bb84f0181e65c11a42cb1c1f6a9e851))
* **devcontainer:** update postCreateCommand with correct syntax ([f89df71](https://github.com/yifattih/rmr-projection-api/commit/f89df71005102546ffa9611a494ab7132ea1802f))
* **Dockerfile:** add layer to copy config file and update entrypoint for honcho ([cfd6c93](https://github.com/yifattih/rmr-projection-api/commit/cfd6c93f642a360727ce7e89b6c1af20bf5faf94))
* **form-handler:** add confirmation message ui ([ba22ced](https://github.com/yifattih/rmr-projection-api/commit/ba22cedb5df0e935eb9541c8cbf71030e08d65ed)), closes [#12](https://github.com/yifattih/rmr-projection-api/issues/12)
* **Makefile:** adjust git log format to prevent line mixing with tac ([6620a3a](https://github.com/yifattih/rmr-projection-api/commit/6620a3afcf23acf960cdae0ebae2000324ce2247))
* **Makefile:** correct parameter name typo ([c20f109](https://github.com/yifattih/rmr-projection-api/commit/c20f10920f578586259ca78153b8abb84ba32db5))
* **Makefile:** update command to suppress git success messages ([5ecbd54](https://github.com/yifattih/rmr-projection-api/commit/5ecbd5470532f0ddce373788a6b7cf59c361e502))
* remove not needed tests ([e744cb5](https://github.com/yifattih/rmr-projection-api/commit/e744cb5b861609e32b037142135a1915aa061eb5))
* rename files; remove image pushing ([dc44eb2](https://github.com/yifattih/rmr-projection-api/commit/dc44eb218a7e4b5c0a840f48fcda4a9ed4006dee))
* **routes:** correct module import ([860e726](https://github.com/yifattih/rmr-projection-api/commit/860e7263767a9d8f0249866b77db5138a58eba1f))
* **service/main:** update endpoint to return 422 status code for unprocessable entity ([#78](https://github.com/yifattih/rmr-projection-api/issues/78)) ([2aaca77](https://github.com/yifattih/rmr-projection-api/commit/2aaca77ab32fd1efa697e8e07ba0e3f9957ef0b5))
* **submit-button:** integrate AJAX submission ([d44c8b5](https://github.com/yifattih/rmr-projection-api/commit/d44c8b592ffc7aee4a4e68e9d962495c85d51ebd)), closes [#10](https://github.com/yifattih/rmr-projection-api/issues/10)
* **ui-cards:** add activity factor cards ([c010ab8](https://github.com/yifattih/rmr-projection-api/commit/c010ab8a1a67aa7a683a373a221ec803b64f58b8))
* **ui-cards:** add interactivity and color scheme ([7674271](https://github.com/yifattih/rmr-projection-api/commit/76742716c07babfd9d5c69aa71084513d6c27152))
* **ui-cards:** add padding plots section ([2a4fcf0](https://github.com/yifattih/rmr-projection-api/commit/2a4fcf0006adc1ab8693a633b84f8da00e91cad7))
* **ui-cards:** add second activity factor card ([4ba7b11](https://github.com/yifattih/rmr-projection-api/commit/4ba7b11580f377fa79ef84a8aee76fd186a054e6))
* **ui-cards:** add tooltips ([a73682f](https://github.com/yifattih/rmr-projection-api/commit/a73682fe17af4ad4bdd6d92320d347710b0d00c1))
* **ui-cards:** change css positioning ([1fed89a](https://github.com/yifattih/rmr-projection-api/commit/1fed89a68dfd28818aa1eb3df2ef1346cd867bc5))
* **ui-cards:** change ui layout to flex ([9f52e12](https://github.com/yifattih/rmr-projection-api/commit/9f52e123ea1c6731b8c2c6493643d8107c3e722f))
* **ui-cards:** format main sections and styles ([7f88617](https://github.com/yifattih/rmr-projection-api/commit/7f886175876883082edc0981cfdeb3e13871aa3c))
* **ui-cards:** integrate dynamic changes with js ([75f8870](https://github.com/yifattih/rmr-projection-api/commit/75f887091ee3a382f8497562394c08781af9c491))
* **ui-chart:** change flake8 error handling ci pipeline ([ede3e7a](https://github.com/yifattih/rmr-projection-api/commit/ede3e7a54719951e4d1bd47d79cab8c9793963f7))
* **ui-chart:** module imports ([7332bc6](https://github.com/yifattih/rmr-projection-api/commit/7332bc675f9a2e9cb3335b27fa0729b27111e9d7))
* update documentation ([68fc6ea](https://github.com/yifattih/rmr-projection-api/commit/68fc6ea84c82a5e17c3c9de61ab2bf941b13266a))


### Features

* add endpoint to expose observability metrics ([95edcda](https://github.com/yifattih/rmr-projection-api/commit/95edcda2ebac261c9060f230b2e7b7af41335a3a))
* add prometheus instrumentation to the API [skip actions] ([d6e9099](https://github.com/yifattih/rmr-projection-api/commit/d6e9099d1599091cebfaed707101b3e147577a41))
* add prometheus to the stack [skip actions] ([7426555](https://github.com/yifattih/rmr-projection-api/commit/742655511302d5bd6bace001987ab46159e305fa))
* **form-handler:** add submit route ([0cfe90e](https://github.com/yifattih/rmr-projection-api/commit/0cfe90e8cdecd5535c7985b744aea7abc87033ba)), closes [#11](https://github.com/yifattih/rmr-projection-api/issues/11)
* **health:** add endpoint to allow health status check  ([#76](https://github.com/yifattih/rmr-projection-api/issues/76)) ([826b883](https://github.com/yifattih/rmr-projection-api/commit/826b88392ee34390331a8f39fa80d26ec32dd582))
* **service:** add OpenTelemetry configuration and instrumentation ([#81](https://github.com/yifattih/rmr-projection-api/issues/81)) ([7e821c1](https://github.com/yifattih/rmr-projection-api/commit/7e821c18e15c1f9b1a80d27fb3b379487be3af43)), closes [#61](https://github.com/yifattih/rmr-projection-api/issues/61) [#64](https://github.com/yifattih/rmr-projection-api/issues/64) [#67](https://github.com/yifattih/rmr-projection-api/issues/67) [#71](https://github.com/yifattih/rmr-projection-api/issues/71) [#74](https://github.com/yifattih/rmr-projection-api/issues/74) [#76](https://github.com/yifattih/rmr-projection-api/issues/76) [#77](https://github.com/yifattih/rmr-projection-api/issues/77) [#78](https://github.com/yifattih/rmr-projection-api/issues/78) [#80](https://github.com/yifattih/rmr-projection-api/issues/80)


### Reverts

* Revert "Add gbr Target to Automate Git Branch Listing in Makefile ([#56](https://github.com/yifattih/rmr-projection-api/issues/56))" ([#57](https://github.com/yifattih/rmr-projection-api/issues/57)) ([dade5f3](https://github.com/yifattih/rmr-projection-api/commit/dade5f3491950e25385825b488572a494a03190e))
* Revert "feat(service): add OpenTelemetry configuration and instrumentation ([#81](https://github.com/yifattih/rmr-projection-api/issues/81))" ([#82](https://github.com/yifattih/rmr-projection-api/issues/82)) ([4432f46](https://github.com/yifattih/rmr-projection-api/commit/4432f468978ada4f79d6b5087c6f7989014f7f9f))

# 1.0.0-alpha.1 (2025-04-10)


### Bug Fixes

* add activity factor calculation ([5097fe8](https://github.com/yifattih/rmr-projection-api/commit/5097fe84327a829d5d261cc492abb051d374cfdf))
* add time projection to results dict ([6906b37](https://github.com/yifattih/rmr-projection-api/commit/6906b3712749bc4fa9f9f5c3cd305df2ede22108))
* add unit tests ([00d0432](https://github.com/yifattih/rmr-projection-api/commit/00d04328c37a09dc6b0fdefbf930bb8240d429a7))
* **api:** add output data model in schemas.py for pydantic validation ([be73871](https://github.com/yifattih/rmr-projection-api/commit/be73871825eea17c16f4e98842f1d5349045419f))
* **api:** rename input data model to align with updated pydantic schema ([0853a8a](https://github.com/yifattih/rmr-projection-api/commit/0853a8aaf2026f85b0c8b87cbd6c8ee347f7cb8b))
* **api:** update equations module error handler to include invalid input in error ([464ac3f](https://github.com/yifattih/rmr-projection-api/commit/464ac3fa1d0389405252332bc68f5e6202c8d070))
* **app-bmr calculator:** change package structure ([8d027c7](https://github.com/yifattih/rmr-projection-api/commit/8d027c7d2bf44ea0d0654d1e977d8cceb53e973e))
* **backend:** change back sex male for men ([e9394c3](https://github.com/yifattih/rmr-projection-api/commit/e9394c3a035028bc453c8d8b2894a994167aac2d))
* change badges ([283a38a](https://github.com/yifattih/rmr-projection-api/commit/283a38a081085612dfee7d4aedd9cd7488c8dce6))
* **core:** isolate monolith backend into microservice ([a878e07](https://github.com/yifattih/rmr-projection-api/commit/a878e0735bb84f0181e65c11a42cb1c1f6a9e851))
* **devcontainer:** update postCreateCommand with correct syntax ([f89df71](https://github.com/yifattih/rmr-projection-api/commit/f89df71005102546ffa9611a494ab7132ea1802f))
* **Dockerfile:** add layer to copy config file and update entrypoint for honcho ([cfd6c93](https://github.com/yifattih/rmr-projection-api/commit/cfd6c93f642a360727ce7e89b6c1af20bf5faf94))
* **form-handler:** add confirmation message ui ([ba22ced](https://github.com/yifattih/rmr-projection-api/commit/ba22cedb5df0e935eb9541c8cbf71030e08d65ed)), closes [#12](https://github.com/yifattih/rmr-projection-api/issues/12)
* **Makefile:** adjust git log format to prevent line mixing with tac ([6620a3a](https://github.com/yifattih/rmr-projection-api/commit/6620a3afcf23acf960cdae0ebae2000324ce2247))
* **Makefile:** correct parameter name typo ([c20f109](https://github.com/yifattih/rmr-projection-api/commit/c20f10920f578586259ca78153b8abb84ba32db5))
* **Makefile:** update command to suppress git success messages ([5ecbd54](https://github.com/yifattih/rmr-projection-api/commit/5ecbd5470532f0ddce373788a6b7cf59c361e502))
* remove not needed tests ([e744cb5](https://github.com/yifattih/rmr-projection-api/commit/e744cb5b861609e32b037142135a1915aa061eb5))
* rename files; remove image pushing ([dc44eb2](https://github.com/yifattih/rmr-projection-api/commit/dc44eb218a7e4b5c0a840f48fcda4a9ed4006dee))
* **routes:** correct module import ([860e726](https://github.com/yifattih/rmr-projection-api/commit/860e7263767a9d8f0249866b77db5138a58eba1f))
* **service/main:** update endpoint to return 422 status code for unprocessable entity ([#78](https://github.com/yifattih/rmr-projection-api/issues/78)) ([2aaca77](https://github.com/yifattih/rmr-projection-api/commit/2aaca77ab32fd1efa697e8e07ba0e3f9957ef0b5))
* **submit-button:** integrate AJAX submission ([d44c8b5](https://github.com/yifattih/rmr-projection-api/commit/d44c8b592ffc7aee4a4e68e9d962495c85d51ebd)), closes [#10](https://github.com/yifattih/rmr-projection-api/issues/10)
* **ui-cards:** add activity factor cards ([c010ab8](https://github.com/yifattih/rmr-projection-api/commit/c010ab8a1a67aa7a683a373a221ec803b64f58b8))
* **ui-cards:** add interactivity and color scheme ([7674271](https://github.com/yifattih/rmr-projection-api/commit/76742716c07babfd9d5c69aa71084513d6c27152))
* **ui-cards:** add padding plots section ([2a4fcf0](https://github.com/yifattih/rmr-projection-api/commit/2a4fcf0006adc1ab8693a633b84f8da00e91cad7))
* **ui-cards:** add second activity factor card ([4ba7b11](https://github.com/yifattih/rmr-projection-api/commit/4ba7b11580f377fa79ef84a8aee76fd186a054e6))
* **ui-cards:** add tooltips ([a73682f](https://github.com/yifattih/rmr-projection-api/commit/a73682fe17af4ad4bdd6d92320d347710b0d00c1))
* **ui-cards:** change css positioning ([1fed89a](https://github.com/yifattih/rmr-projection-api/commit/1fed89a68dfd28818aa1eb3df2ef1346cd867bc5))
* **ui-cards:** change ui layout to flex ([9f52e12](https://github.com/yifattih/rmr-projection-api/commit/9f52e123ea1c6731b8c2c6493643d8107c3e722f))
* **ui-cards:** format main sections and styles ([7f88617](https://github.com/yifattih/rmr-projection-api/commit/7f886175876883082edc0981cfdeb3e13871aa3c))
* **ui-cards:** integrate dynamic changes with js ([75f8870](https://github.com/yifattih/rmr-projection-api/commit/75f887091ee3a382f8497562394c08781af9c491))
* **ui-chart:** change flake8 error handling ci pipeline ([ede3e7a](https://github.com/yifattih/rmr-projection-api/commit/ede3e7a54719951e4d1bd47d79cab8c9793963f7))
* **ui-chart:** module imports ([7332bc6](https://github.com/yifattih/rmr-projection-api/commit/7332bc675f9a2e9cb3335b27fa0729b27111e9d7))
* update documentation ([68fc6ea](https://github.com/yifattih/rmr-projection-api/commit/68fc6ea84c82a5e17c3c9de61ab2bf941b13266a))


### Features

* add endpoint to expose observability metrics ([95edcda](https://github.com/yifattih/rmr-projection-api/commit/95edcda2ebac261c9060f230b2e7b7af41335a3a))
* add prometheus instrumentation to the API [skip actions] ([d6e9099](https://github.com/yifattih/rmr-projection-api/commit/d6e9099d1599091cebfaed707101b3e147577a41))
* add prometheus to the stack [skip actions] ([7426555](https://github.com/yifattih/rmr-projection-api/commit/742655511302d5bd6bace001987ab46159e305fa))
* **form-handler:** add submit route ([0cfe90e](https://github.com/yifattih/rmr-projection-api/commit/0cfe90e8cdecd5535c7985b744aea7abc87033ba)), closes [#11](https://github.com/yifattih/rmr-projection-api/issues/11)
* **health:** add endpoint to allow health status check  ([#76](https://github.com/yifattih/rmr-projection-api/issues/76)) ([826b883](https://github.com/yifattih/rmr-projection-api/commit/826b88392ee34390331a8f39fa80d26ec32dd582))


### Reverts

* Revert "Add gbr Target to Automate Git Branch Listing in Makefile ([#56](https://github.com/yifattih/rmr-projection-api/issues/56))" ([#57](https://github.com/yifattih/rmr-projection-api/issues/57)) ([dade5f3](https://github.com/yifattih/rmr-projection-api/commit/dade5f3491950e25385825b488572a494a03190e))
