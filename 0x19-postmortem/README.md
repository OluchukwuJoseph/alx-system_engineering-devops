# Error 500 outage incident report
Posted: Sunday, January 21, 2024

By the Software Engineering Team

## Issue Summary
On August 19th, 2024, our service experienced an outage that lasted 1 hour and 35 minutes, from 2:04 PM WAT to 3:39 PM WAT. During this period, the entire service was down, affecting 100% of our users. Users were unable to access the website due to a fatal error in the system. The root cause was a typo in the wp-settings.php file after a recent update, where "php" was mistakenly written as "phpp".

## Timeline
2:04 PM WAT: The issue was detected 2 minutes after deployment, triggered by a monitoring alert from Datadog and a customer complaint.
2:10 PM WAT: The engineering team began investigating the source files, suspecting that the issue might have originated from there.
2:25 PM WAT: The team focused on checking the backend files, assuming the error was related to the backend.
3:00 PM WAT: After testing the backend files in a staged environment and confirming they worked correctly, the team ruled out backend issues.
3:20 PM WAT: The team expanded the investigation to plugins and configuration files.
3:30 PM WAT: The typo in the wp-settings.php file was discovered and corrected.
3:39 PM WAT: The corrected file was deployed, and the service was restored.
## Root Cause and Resolution
Imagine you’re writing a crucial document, but your keyboard decides to prank you by adding an extra letter in a key word. That’s pretty much what happened here. The innocent typo "phpp" instead of "php" in the wp-settings.php file brought our entire service to its knees. Once we stopped blaming the backend and checked the config files, we spotted the issue, corrected the typo, and deployed the fix, returning to business as usual.

## Corrective and Preventative Measures
To prevent similar incidents in the future, the following actions will be taken:

Implement Code Review Protocols: Introduce mandatory code reviews before deploying updates to production, specifically checking for syntax errors in critical files like wp-settings.php.
Enhance Monitoring: Add more granular monitoring alerts that can differentiate between frontend and backend issues, reducing time spent on incorrect debugging paths.
Automate Testing: Implement automated tests that check for common syntax errors in configuration files before deployment.
Team Training: Conduct a training session on the importance of checking all areas, including configuration files, when investigating an issue.
Documentation Update: Update the deployment documentation to include a checklist that ensures all files, especially configuration files, are double-checked for errors.
These steps will help us avoid similar outages and improve the overall resilience of our system.

![The team after restoring service](./happy-team.jpg)
After restoring service
