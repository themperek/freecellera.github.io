# Simple Makefile for publishing from website-content repo

# Path to website-content repository
WEBSITE_CONTENT ?= $(PWD)/../website-content

all: github

.phony: check
check: $(WEBSITE_CONTENT)/Makefile

.phony: github
github: check
	$(MAKE) -C $(WEBSITE_CONTENT) publish
	ghp-import -m "Generate Pelican site" -b master $(WEBSITE_CONTENT)/output
	git push origin master

