# ===============================================================
# 1. PROJECT DEPENDENCIES (requirements.txt)
# ===============================================================
# Core Automation Framework
pytest-playwright

# Reporting & Dashboards
allure-pytest

# Environment & Secret Management (API Keys, URLs)
python-dotenv

# Execution Performance (Parallel Testing)
pytest-xdist

# Stability (Auto-retry flaky UI tests)
pytest-rerunfailures

# ===============================================================
# 2. INSTALLATION & VERIFICATION
# ===============================================================
# STEP 1: Activate your virtual environment:
#    Windows: .venv\Scripts\activate
#    Mac/Linux: source .venv/bin/activate
#
# STEP 2: Install all dependencies:
#    pip install -r requirements.txt
#
# STEP 3: Download Browser Binaries (CRITICAL for new projects):
#    playwright install
#
# STEP 4: Confirm installation:
#    pip list | findstr "pytest allure playwright"

# ===============================================================
# 3. PLAYWRIGHT & ALLURE COMMAND CHEAT SHEET
# ===============================================================

# --- RUNNING TESTS ---
# Run all tests and store results:
# pytest --alluredir=allure-results

# Run in Parallel (2 workers) to save time:
# pytest -n 2 --alluredir=allure-results --clean-alluredir

# Run a specific test case:
# pytest -k "test_login_function" --alluredir=allure-results

# --- REPORTING ---
# Generate and open report immediately (Local):
# allure serve allure-results

# Build a permanent report folder (for CI/CD):
# allure generate allure-results --clean -o allure-report

# --- DEBUGGING FLAGS ---
# --headed                : See the browser in action (slows down execution)
# --slowmo 500            : Adds 500ms delay to watch execution closely
# --screenshot=on         : Takes a screenshot of every step
# --trace retain-on-failure : Records a full trace for debugging failures
# ===============================================================