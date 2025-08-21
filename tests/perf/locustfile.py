from locust import HttpUser, task, between, events
import os

THRESHOLD_RT_P95_MS = int(os.getenv("THRESHOLD_RT_P95_MS", "200"))
THRESHOLD_ERROR_RATE = float(os.getenv("THRESHOLD_ERROR_RATE", "0.01"))

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task(2)
    def health(self):
        self.client.get("/health")

    @task(3)
    def add_api(self):
        self.client.get("/add?a=10&b=20")

@events.test_stop.add_listener
def validate_thresholds(environment, **kwargs):
    stats = environment.runner.stats
    total = stats.total
    p95 = total.get_response_time_percentile(0.95) if total.num_requests else 0
    error_rate = (total.num_failures / total.num_requests) if total.num_requests else 0.0
    print(f"[THRESHOLDS] p95={p95}ms  error_rate={error_rate:.4f}")

    violations = []
    if p95 > THRESHOLD_RT_P95_MS:
        violations.append(f"P95 {p95}ms > {THRESHOLD_RT_P95_MS}ms")
    if error_rate > THRESHOLD_ERROR_RATE:
        violations.append(f"Error rate {error_rate:.4f} > {THRESHOLD_ERROR_RATE:.4f}")

    if violations:
        for v in violations:
            print(f"[THRESHOLD VIOLATION] {v}")
        environment.process_exit_code = 1  # 讓 CI fail
