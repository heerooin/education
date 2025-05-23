import pytest
import coverage
import os
import sys


def run_coverage():
    # Start coverage
    cov = coverage.Coverage()
    cov.start()

    # Run pytest
    print("Running tests...")
    pytest.main(['-v', 'tests/test_category.py'])

    # Stop coverage
    cov.stop()
    cov.save()

    # Generate report
    print("\nCoverage report:")
    cov.report()

    # Generate HTML report
    print("\nGenerating HTML report...")
    cov.html_report()
    print("HTML report generated in the 'coverage_html_report' directory.")


if __name__ == "__main__":
    run_coverage()
