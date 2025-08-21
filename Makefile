.PHONY: perf
perf:
	@mkdir -p reports
	@python -m pip install --upgrade pip >/dev/null
	@pip install -r requirements-perf.txt
	@locust -f tests/perf/locustfile.py \
	  --headless -u $${USERS:-50} -r $${SPAWN_RATE:-10} --run-time $${DURATION:-2m} \
	  --host $${TARGET_BASE_URL:-http://localhost:8000} \
	  --html reports/locust-report.html --csv reports/locust
