## Day 8：效能測試（Performance Test）

在 CI/CD Pipeline 中加入效能測試，確保系統不只「正確」，還能「撐得住」。

### 快速檢查清單
- [ ] 建立 `tests/perf/locustfile.py`、`requirements-perf.txt`、`reports/`  
- [ ] Makefile 加 `perf` 目標  
- [ ] 新增 `.github/workflows/perf.yml`，在 Secrets 設 `TARGET_BASE_URL`  
- [ ] 本機測一次：`TARGET_BASE_URL=http://localhost:8000 make perf`  
- [ ] 看 `reports/locust-report.html` 是否有數據  
- [ ] 開 PR，確認 CI 能產生 artifact，且**不達標會 fail**  

### 使用方式
本機：
```bash
export TARGET_BASE_URL=http://localhost:8000
make perf
# 產出 reports/locust-report.html
