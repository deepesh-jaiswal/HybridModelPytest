rem Sanity on Chrome

pytest -v -s -m "sanity" --html=Reports\sanityChromeReport.html --capture=sys testCases --browser Chrome

rem Sanity on Firefox

pytest -v -s -m "sanity" --html=Reports\sanityFirefoxReport.html --capture=sys testCases --browser Firefox

rem Sanity and Regression on Chrome

rem pytest -v -s -m "sanity and regression" --html=Reports\sanityAndRegressionChromeReport.html --capture=sys testCases --browser Chrome

