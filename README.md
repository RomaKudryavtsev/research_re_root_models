# Research re root models
Projects contains two Flask servers which use the same model contained in root directory.

## Instructions to run
  - Ensure local PostgreSQL is running on port 5032
  - Create database "root_models"
  - Create one user with id 1
  - Run both servers as modules
    <pre>python -m new_root.server1.app</pre>
    <pre>python -m new_root.server2.app</pre>

## Useful resources
  - https://stackoverflow.com/questions/30669474/beyond-top-level-package-error-in-relative-import
  - https://stackoverflow.com/questions/6323860/sibling-package-imports
  - https://stackoverflow.com/questions/14132789/relative-imports-for-the-trilli%d0%benth-time/14132912#14132912
  - https://napuzba.com/attempted-relative-import-beyond-top-level-package/
