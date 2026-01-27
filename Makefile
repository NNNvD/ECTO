log:
	python scripts/log_today.py

log-add:
	python scripts/log_add.py --type "$(TYPE)" --title "$(TITLE)" --links "$(LINKS)" --context "$(CONTEXT)" --result "$(RESULT)" --followups "$(FOLLOWUPS)"

adr:
	python scripts/adr_new.py --title "$(TITLE)" --owner "$(OWNER)" --status "$(STATUS)"

log-index:
	python scripts/logbook_index.py
