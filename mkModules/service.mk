.PHONY: run build

run: ##	Run the service
##	|Usage:
##	|	$ make run
    @ echo
    @ $(call headercan,"SERICE RUNNING")
    @ export ENV="dev"; \
	honcho start -d service -f Procfile
    @ echo

build: ## Build the service
##	|Usage:
##	|	$ make build
    @echo
    @ $(call headercan,"BUILDING SERVICE")
    @ docker build -t $(ARG1) ./service
    @ $(call inform,"Service built successfully")
    @ echo

push: ## Push the service image to the Docker Hub repository
##	|Usage:
##	|	$ make push <string:service-name>
    @ echo
    @ $(call headercan,"PUSHING SERVICE TO DOCKER HUB")
    @ docker push $(ARG1)
    @ $(call inform,"Service pushed successfully")
    @ echo